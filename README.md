# 🧠 AI Brief Series – Autonomous AI Agents for Monitoring Artificial Intelligence

A series of **three autonomous AI agents** built with **n8n**, designed to automate monitoring of artificial intelligence, both in current events and scientific research.

## 🚀 Overview

Each agent is capable of:
- 📥 Fetching content from a dedicated source  
- 🧠 Filtering information related to AI  
- ✍️ Generating a concise summary (via Gemini or DeepSeek)  
- 📧 Sending an automated report via email  

---

## 🤖 The Agents

### 🔹 Reddit AI Brief – Powered by an Autonomous Agent  
- **Source**: Reddit  
- **Goal**: Provide daily summaries of relevant discussions on AI from specialized subreddits  

### 🔹 ArXiv AI Brief – Powered by an Autonomous Agent  
- **Source**: ArXiv RSS feed (AI category)  
- **Goal**: Track the latest weekly scientific publications on AI  

### 🔹 AI Brief – Powered by an Autonomous Agent  
- **Source**: VentureBeat RSS feed  
- **Goal**: Weekly summaries of the latest tech news in AI  

---

## 🛠️ Technologies Used

- [n8n](https://n8n.io/) – Workflow orchestration  
- [Google Gemini](https://ai.google.dev/) – Summarization & translation  
- [DeepSeek](https://api-docs.deepseek.com/) – Summarization & translation  
- Reddit / RSS feeds – Data collection  
- Gmail – Automated email delivery  

---

## 📁 Repository Structure

- `reddit-ai-brief/`: contains the `workflow.json` file for the Reddit agent  
- `arxiv-ai-brief/`: contains the `workflow.json` file for the ArXiv agent  
- `venturebeat-ai-brief/`: contains the `workflow.json` file for the VentureBeat agent  

---

## ▶️ How to Use These Agents

1. Clone this GitHub repository  
2. Open [n8n](https://n8n.io/) (local instance or cloud)  
3. Import the corresponding `workflow.json` files  
4. Add your API credentials: Gemini, DeepSeek, Reddit, Gmail…  
5. Schedule executions (daily or weekly)  
6. That’s it! 🤖  

---

## 💡 Vision

This project lays the foundation for an **autonomous personal AI assistant**, designed to streamline technological and scientific monitoring.

---

## 📬 Contact

📩 amessaoudi.am@gmail.com  
🌍 https://github.com/AdelMessaoudi-13
