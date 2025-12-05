from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from backend.agent.registry import current_state 
from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.utils.system_context_builder import SystemContextBuilder
from backend.utils.code_search import CodeSearch
from backend.workflow.loop_workflow import LoopWorkflow
from pathlib import Path
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.background import BackgroundTasks
from backend.workflow.user_feedback_workflow import UserFeedbackWorkflow
from .settings import GENERATED_DIR
from .auto_script import delete_exist_files
from backend.utils.load_response import load_response_folder
import base64
import tempfile
import shutil
import os
app = FastAPI()

templates = Jinja2Templates(directory="frontend")

class SavePageRequest(BaseModel):
    page_id: str
    html: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],     # VERY IMPORTANT
    allow_headers=["*"],     # VERY IMPORTANT
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    for error in errors:
        if error.get("type") == "string_too_long":
             return JSONResponse(status_code=413, content={"message": "Prompt is too large. Maximum allowed is 50,000 characters."})
    return JSONResponse(status_code=422, content={"detail": errors})

"""we do not need them now, we are testing generate api"""
# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="index.html"
#     )

# @app.post("/generate")
# async def generate(
#     request: Request,
#     prompt: str = Form(...),
#     theme: str = Form(...),
#     ):
    
#     current_state.raw_user_prompt = str(prompt)
#     current_state.user_selected_theme = str(theme)
#     print(current_state.user_selected_theme)
#     print("="*50)
#     print(f"successufly received Stored Prompt: {current_state.raw_user_prompt}")
#     print("="*50)
#     delete_exist_files("generated_output\\src\\app")
    
#     LoopWorkflow().run(prompt=str(prompt), theme=str(theme))
#     print(f"successufly Generated Files.....")
#     print("\n Generated files (state.files_json):")
#     print("\n" + "="*50)

#     pages = current_state.project_metadata.feature_files

#     return templates.TemplateResponse(
#     "download.html",
#     {
#         "request": request,
#         "pages": pages
#     }
# )


# @app.get("/download")
# def download_project(background_tasks: BackgroundTasks):
    
#     ZIP_PATH = GENERATED_DIR.with_suffix(".zip")
#     #delet automatically after downloading.
    

#     response = FileResponse(
#         path=ZIP_PATH,
#         media_type="application/zip",
#         filename="generated_project.zip"
#     )

#     return response
# @app.post("/modify")
# async def modify_project(
#     modify_prompt: str = Form(...),
#     pages_name: str = Form(None)
#     ):
#     current_state.modify_prompt = modify_prompt
#     current_state.page_to_be_modified = pages_name
    
#     UserFeedbackWorkflow().run()
#     return RedirectResponse(url="/download", status_code=303)
    

# @app.post("/save-page")
# def save_page(req: SavePageRequest):
#     print("hejj")
#     os.makedirs("saved_pages", exist_ok=True)
#     file_path = f"saved_pages/{req.page_id}.html"

#     print("Saving to:", os.path.abspath(file_path))

#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(req.html)

#     return {"status": "ok"}



class UserInput(BaseModel):
    prompt: str = Field(..., max_length=50000, description="User prompt with a hard limit of 50,000 characters to prevent abuse.")
    theme: str
    model: Optional[str] = None

@app.post("/api/zip/generate")
async def generate(data: UserInput):
    prompt = data.prompt
    theme = data.theme
    model = data.model

    # Run the workflow which generates and writes files to GENERATED_DIR
    LoopWorkflow().run(prompt=str(prompt), theme=str(theme), model=model)

    # Path for the zip file
    zip_filename = "generated_project"
    zip_path = GENERATED_DIR.parent / zip_filename
    
    # Create zip archive (shutil.make_archive adds .zip extension automatically)
    shutil.make_archive(str(zip_path), 'zip', GENERATED_DIR)
    
    # The actual file path will have .zip appended
    final_zip_path = zip_path.with_suffix(".zip")

    return FileResponse(
        path=final_zip_path,
        media_type="application/zip",
        filename="generated_project.zip"
    )


@app.post("/api/json/generate")
async def generate(data: UserInput):
    prompt = data.prompt
    theme = data.theme
    model = data.model

    # Run the workflow which generates and writes files to GENERATED_DIR
    LoopWorkflow().run(prompt=str(prompt), theme=str(theme), model=model)

    return load_response_folder(GENERATED_DIR)
