from fastapi import FastAPI
from pydantic import BaseModel
from src.graph import app as marketmind_app
import os
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI(title="MarketMind AI API")


class TopicRequest(BaseModel):
    topic: str


@app.post("/analyze")
def analyze_market(request: TopicRequest):
    inputs = {
        "messages": [
            ("human", f"حلل السوق التالي باللغة العربية فقط وبأسلوب تقرير احترافي: {request.topic}")
        ]
    }

    # MarketMind AI
    final_state = marketmind_app.invoke(inputs)

    report_content = final_state.get("report_content")
    if not report_content:
        report_content = final_state["messages"][-1].content

    # 
    safe_topic = request.topic.replace(" ", "_").replace("/", "_")
    REPORT_DIR = os.getenv("REPORT_PATH", "reports")
    os.makedirs(REPORT_DIR, exist_ok=True)
    filename = os.path.join(REPORT_DIR, f"Market_Report_{safe_topic}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    return {"report": report_content, "saved_file": filename}
