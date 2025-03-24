from fastapi import FastAPI, Request
from app.model import generate

app = FastAPI()

@app.post("/generate")
async def generate_text(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    output = generate(prompt)
    return {"response": output}
