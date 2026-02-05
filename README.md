# MarketMind AI

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-green)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**MarketMind AI** is a multi-agent AI system that analyzes markets in Arabic and generates professional reports in Markdown format.  
It uses **LangChain**, **LangGraph**, **Groq LLM**, and **Tavily Search** to gather data, analyze it, and produce a final report automatically.

---

## 🔹 Project Structure



MarketMind-AI/
│
├─ src/
│ ├─ agents/
│ ├─ tools/
│ ├─ graph.py
│ └─ state.py
│
├─ main.py ← main execution file
├─ reports/ ← saved reports
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
└─ .env ← API keys & environment variables


---

## ⚡ Quick Start

### 1️⃣ Using Python

1. Install dependencies:

```bash
pip install -r requirements.txt


Create .env file:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
REPORT_PATH=reports


Run:

python main.py


Enter any Arabic market topic.

Report is saved to reports/ as Markdown.

2️⃣ Using Docker

Build and run:

docker compose build --no-cache
docker compose up


The app runs inside the container.

Reports appear directly on your machine in reports/ via volume mapping.

✅ Example
Enter the topic you want MarketMind AI to analyze:
Car Market


Report generated:

reports/Market_Report_Car_Market.md

🔧 Future Improvements

Convert CLI to API using FastAPI.

Add PDF export.

Enhance agents for structured JSON output.