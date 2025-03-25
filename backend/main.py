from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.model import PromptEnhancer  # Changed to absolute import

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the model
model = PromptEnhancer()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/rephrase")
async def rephrase_prompt(request: PromptRequest):
    try:
        enhanced_prompt = model.enhance_prompt(request.prompt)
        return {"enhanced_prompt": enhanced_prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
