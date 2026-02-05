

# 📄 README.md 

````markdown
# AI Ops Assistant – GenAI Internship Assignment

AI Operations Assistant built using a multi-agent architecture (Planner, Executor, Verifier).

The system accepts natural language tasks, generates a structured execution plan using an LLM, integrates real third-party APIs (GitHub & OpenWeather), and produces a complete end-to-end structured response.

---

## 🚀 Features

- Multi-agent architecture:
  - Planner Agent (LLM-based planning with structured JSON output)
  - Executor Agent (API execution layer)
  - Verifier Agent (Output validation and formatting)
- Uses LLM for structured planning
- Integrates 2 real APIs:
  - GitHub Search API
  - OpenWeather API
- Runs locally via FastAPI
- Produces structured JSON responses
- No hardcoded responses

---

## 🏗 Architecture Overview

### 1️⃣ Planner Agent
- Accepts natural language task
- Uses LLM to generate a structured JSON plan:
  ```json
  {
    "steps": [
      {
        "tool": "github_search",
        "parameters": {...}
      }
    ]
  }
````

### 2️⃣ Executor Agent

* Iterates over planned steps
* Calls appropriate tool:

  * GitHub tool
  * Weather tool
* Collects results

### 3️⃣ Verifier Agent

* Validates tool results
* Ensures response completeness
* Returns final structured output

---

## 🛠 Integrated APIs

1. GitHub REST API

   * Endpoint: `https://api.github.com/search/repositories`
   * Used to fetch top repositories by stars

2. OpenWeather API

   * Endpoint: `https://api.openweathermap.org/data/2.5/weather`
   * Used to fetch real-time weather by city

---

## ⚙ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-ops-assistant.git
cd ai-ops-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_google_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

`.env.example` is provided for reference.

---

## ▶ Running the Project

Run using:

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoint

### POST `/query`

Request body:

```json
{
  "task": "Find top 2 AI repositories and tell weather in Mumbai"
}
```

Response:

```json
{
  "summary": "Found 2 repositories. Weather in Mumbai retrieved.",
  "details": {
    "github": [...],
    "weather": {...}
  }
}
```

---

## 🧪 Example Prompts

1. Find top 3 AI repositories
2. Tell weather in Delhi
3. Find top 2 machine learning repositories and weather in London
4. Get weather in New York
5. Find top 1 Python repository

---

## 📦 Project Structure

```
ai_ops_assistant/
│
├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
│
├── tools/
│   ├── github_tool.py
│   └── weather_tool.py
│
├── llm/
│   └── llm_client.py
│
├── main.py
├── schemas.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚠ Known Limitations / Tradeoffs

* LLM output parsing depends on proper structured response.
* No caching layer implemented.
* API rate limits may affect execution.
* Sequential tool execution (no parallel processing).
* No authentication for GitHub API (public endpoints only).

---

## ✅ Assignment Requirements Checklist

* [x] Multi-agent design (Planner, Executor, Verifier)
* [x] Uses LLM with structured output
* [x] Integrates 2 real third-party APIs
* [x] Produces complete end-to-end result
* [x] No hardcoded responses
* [x] Runs locally with single command

---

## 👨‍💻 Author

Arnav Gupta
B.Tech CSE (IoT)

---

```

---

