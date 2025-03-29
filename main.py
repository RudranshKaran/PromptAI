from fastapi import FastAPI
from routes import router  
import uvicorn

app = FastAPI()

# Only load routes here
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Prompt Optimizer Backend is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)