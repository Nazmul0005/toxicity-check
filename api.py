from fastapi import FastAPI
from pydantic import BaseModel
from model import classifier

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    text: str
    is_toxic: bool
    toxicity_score: float

@app.post("/check-toxicity", response_model=TextResponse)
async def check_toxicity(request: TextRequest):
    result = classifier(request.text)[0]
    return TextResponse(
        text=request.text,
        is_toxic=result['score'] >= 0.49,
        toxicity_score=result['score']
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)