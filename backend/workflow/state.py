from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


#  Error Structure 
class ErrorDetail(BaseModel):
    file: str = Field(..., description="The path of the file causing the error ")
    type: str = Field(..., description="Type of error: JSON | SECURITY | TS | HTML")
    message: str = Field(..., description="Human-readable explanation of the error")
    severity: str = Field(default="error", description="error | warning")


#  Project Metadata 
class ProjectMetadata(BaseModel):
    name: Optional[str] = None
    angular_version: str = "17"
    requires_routing: bool = True
    


    # NEW: structure info
    base_files: List[str] = Field(
        default_factory=list,
        description="Core Angular files like main.ts, app.component.ts, app.routes.ts"
    )
    feature_files: List[str] = Field(
        default_factory=list,
        description="Dynamic feature-based page components like login.page.ts"
    )


#  GLOBAL STATE 
class AgentState(BaseModel):
    #  User Input 
    raw_user_prompt: str = ""

    #  Specification (from Prompt Engineering Agent) 
    spec_clean: Optional[str] = None  # Structured spec, not JSON or tech based

    #  Code Generation 
    #  Code Generation 
    files_json_raw: Dict[str, str] = Field(default_factory=dict)    # Unvalidated output from LLM
    files_json: Dict[str, str] = Field(default_factory=dict)        # Trusted & validated JSON

    #  Error Handling & Memory 
    errors: List[ErrorDetail] = Field(default_factory=list)
    json_retry_count: int = 0                   # For JSON structure fixes
    code_fix_retry_count: int = 0               # For TS/HTML fixes

    #  Metadata 
    project_metadata: ProjectMetadata = Field(default_factory=ProjectMetadata)

    #  Security Additional Memory 
    security_flags: List[str] = Field(default_factory=list)

    system_context: str | None = None # THis will store the context.

    symbols: list[dict] = Field(default_factory=list) # for the extracted symboles from files. eg==> (class, interface, enum)

    feature_plan: Optional[Dict[str, Any]] = None
