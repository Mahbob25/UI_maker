from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from backend.agent.registry import current_state 
from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.utils.system_context_builder import SystemContextBuilder
from backend.agent.feature_extraction_agent import FeatureExtractionAgent
from backend.workflow.loop_workflow import LoopWorkflow
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks
from .settings import GENERATED_DIR

import os
app = FastAPI()

templates = Jinja2Templates(directory="frontend")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post("/generate")
async def generate(request: Request, prompt: str = Form(...)):
    current_state.raw_user_prompt = str(prompt)
    print("="*50)
    print(f"successufly received Stored Prompt: {current_state.raw_user_prompt}")
    print("="*50)

    # # Generating Workflow
    # PromptEngineeringAgent().run()
    # print(f"successufly Engineered the Prompt.....")
    # print("\n" + "="*50)

    
    # SystemContextBuilder().build()
    # print(f"successufly built the context and output Rules.....")
    # print("\n" + "="*50)

    # FeatureExtractionAgent().run()
    # print(f"successufly Extracted features form user spec.....")
    # print("\n" + "="*50)
    # print(current_state.project_metadata.feature_files)
    
    LoopWorkflow().run()
    print(f"successufly Generated Files.....")
    print("\n Generated files (state.files_json):")
    print("\n" + "="*50)


    return templates.TemplateResponse(
        request=request, name="download.html"
    )

@app.get("/download")
def download_project(background_tasks: BackgroundTasks):
    
    ZIP_PATH = GENERATED_DIR.with_suffix(".zip")
    #delet automatically after downloading.
    background_tasks.add_task(os.remove, str(ZIP_PATH))

    response = FileResponse(
        path=ZIP_PATH,
        media_type="application/zip",
        filename="generated_project.zip"
    )

    return response