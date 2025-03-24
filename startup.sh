#!/bin/bash
mkdir -p models
if [ ! -f models/mistral-7b-instruct-v0.1.Q4_K_M.gguf ]; then
  echo "Downloading Mistral model..."
  curl -L -o models/mistral-7b-instruct-v0.1.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
fi
uvicorn app.main:app --host 0.0.0.0 --port 10000
