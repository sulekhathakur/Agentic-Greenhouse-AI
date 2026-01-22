# Agentic AI – Greenhouse Emissions Intelligence 🌱

This project is a **research-oriented Agentic AI system** designed to analyze greenhouse gas emissions data and generate structured, data-driven insights.

Unlike traditional dashboards or chatbots, this system behaves as an **autonomous AI agent** — it understands a goal, plans analytical steps, performs analysis, and delivers insights using reasoning-based workflows.

## Project Overview

The application allows users to define an analytical objective related to greenhouse emissions.  
The agent then:

- Interprets the goal using an LLM  
- Plans the analysis autonomously  
- Processes greenhouse emissions data  
- Identifies patterns and contributors  
- Generates insights and recommendations  

The focus is on **agentic reasoning**, not UI-heavy visualization.

## Why This Project

Climate datasets are complex and difficult to interpret at scale.  
This project demonstrates how **Agentic AI architectures** can support:

- Environmental data analysis  
- Research assistance  
- Policy-oriented insights  
- Autonomous analytical reasoning  

It also serves as a practical implementation of **LangChain + LangGraph**.


## Tech Stack

- Python  
- Streamlit  
- LangChain  
- LangGraph  
- Groq LLM  
- Pandas  

## Project Structure

Agentic_Greenhouse_AI/
│
├── app.py
├── Greenhouse.csv
├── requirements.txt
│
├── agent/
│   ├── llm.py
│   ├── graph.py
│   ├── state.py
│   └── tools.py

## How to Run Locally

1. Install dependencies:

pip install -r requirements.txt

2. Set the Groq API key:

set GROQ_API_KEY=your_api_key

3. Run the application:

streamlit run app.py

## Deployment

The application is deployed using **Streamlit Cloud** and uses environment-based API key management for security.


## Author

**Sulekha Thakur**  
B.Sc. Computer Science  
Interests: Agentic AI, Applied AI Research, Data Intelligence


## License

This project is licensed under the **MIT License**.

