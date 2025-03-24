from llama_cpp import Llama

LLM = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,
    n_gpu_layers=35
)

def generate(prompt: str) -> str:
    output = LLM(prompt, max_tokens=200, stop=["</s>"])
    return output["choices"][0]["text"].strip()
