from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from backend.agent.registry import current_state 
from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.utils.system_context_builder import SystemContextBuilder
from backend.utils.code_search import CodeSearch
from backend.workflow.loop_workflow import LoopWorkflow
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks
from backend.workflow.user_feedback_workflow import UserFeedbackWorkflow
from .settings import GENERATED_DIR
from .auto_script import delete_exist_files

import os
app = FastAPI()

templates = Jinja2Templates(directory="frontend")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post("/generate")
async def generate(
    request: Request,
    prompt: str = Form(...),
    ):
    
    current_state.raw_user_prompt = str(prompt)
    print("="*50)
    print(f"successufly received Stored Prompt: {current_state.raw_user_prompt}")
    print("="*50)
    delete_exist_files("generated_output\\src\\app")
    
    LoopWorkflow().run()
    print(f"successufly Generated Files.....")
    print("\n Generated files (state.files_json):")
    print("\n" + "="*50)

    pages = current_state.project_metadata.feature_files

    return templates.TemplateResponse(
    "download.html",
    {
        "request": request,
        "pages": pages
    }
)


@app.get("/download")
def download_project(background_tasks: BackgroundTasks):
    
    ZIP_PATH = GENERATED_DIR.with_suffix(".zip")
    #delet automatically after downloading.
    

    response = FileResponse(
        path=ZIP_PATH,
        media_type="application/zip",
        filename="generated_project.zip"
    )

    return response
@app.post("/modify")
async def modify_project(
    modify_prompt: str = Form(...),
    pages_name: str = Form(None)
    ):
    current_state.modify_prompt = modify_prompt
    current_state.page_to_be_modified = pages_name
    
    UserFeedbackWorkflow().run()
    return RedirectResponse(url="/download", status_code=303)
    