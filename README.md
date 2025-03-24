# Mistral LLM Server with llama.cpp

This is a simple FastAPI wrapper for a quantized Mistral 7B Instruct model using llama.cpp.

## Endpoints

- `POST /generate`  
  Body: `{ "prompt": "your question here" }`

## Deployment on Render

1. Create a new Web Service
2. Choose this repo
3. Set build and start commands:
   - Build: `pip install -r requirements.txt`
   - Start: `bash startup.sh`
4. Use a GPU instance or test on CPU with Q4_K_M quant

## Model

Quantized Mistral from TheBloke:
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
