from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    original_prompt: str
    enhanced_prompt: str

def load_preprocessed_dataset(file_path="processed_data.json"):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def enhance_prompt_with_model(prompt: str, dataset):
    for entry in dataset:
        if prompt.lower() in entry["input"].lower():
            return entry["output"]
    return "No suitable enhancement found."

dataset = load_preprocessed_dataset()

@router.post("/enhance_prompt", response_model=PromptResponse)
async def enhance_prompt(request: PromptRequest):
    try:
        enhanced_prompt = enhance_prompt_with_model(request.prompt, dataset)
        return PromptResponse(original_prompt=request.prompt, enhanced_prompt=enhanced_prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enhancing prompt: {str(e)}")