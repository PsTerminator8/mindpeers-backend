from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sentiment_analysis_pretrained import get_sentiment
from sentiment_analysis_feedback import send_sa_feedback, get_sentiment_after_feedback
from keyword_extraction import get_keywords

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/v1/test")
def index():
    return {"message": "Connections Successfull!"}

@app.post("/api/v1/sentiment-analysis")
async def send_text_sa(data: dict) -> dict:
    sentiment = get_sentiment(data["text"])
    response = {
        "text": data["text"],
        "sentiment": sentiment
    }
    return { "status": "ok", "response": response }

@app.post("/api/v1/sentiment-analysis-feedback")
async def send_text_label_sa_feedback(data: dict) -> dict:
    predictions = send_sa_feedback(data["text"], data["label"])
    response = {
        "text": data["text"],
        "label": data["label"],
        "improved-sentiment": predictions
    }
    return { "status": "ok", "response": response }

@app.post("/api/v1/sentiment-analysis-feedback-eval")
async def send_text_sa_feedback_eval(data: dict) -> dict:
    sentiment = get_sentiment_after_feedback(data["text"])
    response = {
        "text": data["text"],
        "sentiment": sentiment
    }
    return { "status": "ok", "response": response }

@app.post("/api/v1/keyword-extraction")
async def send_text_ke(data: dict) -> dict:
    keywords = get_keywords(data["text"])
    response = {
        "text": data["text"],
        "keywords": keywords
    }
    return { "status": "ok", "response": response }

@app.post("/api/v1/keyword-extraction-feedback")
async def send_text_label_ke_feedback(data: dict) -> dict:
    return { "status": "ok", "response": "done" }

# register_tortoise(
#     app,
#     db_url="sqlite://database.sqlite3",
#     modules={"models": ["schema"]},
#     generate_schemas=True,
#     add_exception_handlers=True
# )