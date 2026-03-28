Jetty Health AI - Personalized Health Assistant

A functional prototype of a stateful, AI-native health partner. Unlike standard stateless chatbots, this project explores how a local LLM can be used to capture and reason about health data over time.

 Vision
This project is inspired by the mission to help individuals with chronic illnesses become their own best advocates. It moves beyond simple Q&A to treat the LLM as a component in a larger system designed for:
- **Stateful Memory:** Persisting conversation context to recognize recurring patterns.
- **Structured Extraction:** Moving from raw text to machine-readable health data (symptoms, severity, duration).
- **Longitudinal Insights:** Surfacing trends from historical data to drive better health outcomes.



 Tech Stack
* **Core Logic:** Python 3.11+
* **Backend Framework:** Flask (with Flask-CORS for frontend integration)
* **AI Inference:** [Ollama](https://ollama.com/) running **TinyLlama** (local, privacy-first execution)
* **Frontend:** Modern HTML5, CSS3 (Premium Dark Theme), and Vanilla JavaScript
* **Data Persistence:** Structured JSON-based memory layer

Key Features
* **Premium Chat Interface:** A smooth, responsive UI with "AI Thinking" indicators and typing effects for a polished user experience.
* **Hybrid Extraction Pipeline:** Uses LLM prompting with a rule-based fallback to ensure high reliability in identifying symptoms and their severity.
* **Pattern Recognition:** An insights engine that analyzes the [memory.json](https://github.com/Ajayreddy18/jetty-health-ai-demo/blob/main/.gitignore) to flag recurring symptoms (e.g., "You reported fatigue 3 times this week").
* **Temporal Tracking:** A dedicated Timeline view that logs the date, symptom, and duration of reported issues.



 Getting Started

1. Prerequisites
* Install [Ollama](https://ollama.com/)
* Pull the model: `ollama pull tinyllama`

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install flask ollama flask-cors
python app.py
