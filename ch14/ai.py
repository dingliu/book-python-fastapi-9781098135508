from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig


app = FastAPI()

MODEL_NAME = 'google/flan-t5-base'
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
config = GenerationConfig(max_new_tokens=200)


@app.get("/ai")
def prompt(line: str) -> str:
    tokens = tokenizer(line, return_tensors='pt')
    outputs = model.generate(**tokens)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return result[0]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ai:app", reload=True)
