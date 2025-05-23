# 🧠 AI Brief Series – Autonomous AI Agents for Monitoring Artificial Intelligence

A collection of intelligent agents designed to **collect**, **summarize**, and **distribute** key updates on artificial intelligence — from online discussions to scientific publications.

---

## 🚀 Overview

This project combines Python automation, AI summarization, and email distribution to deliver high-quality, structured summaries from multiple trusted sources:

- 🔍 Reddit (technical discussions and trends)  
- 📰 VentureBeat (AI business and industry news)  
- 📡 ArXiv (academic research – available via [n8n version](#-optional-visual-workflows-with-n8n))

You can either:
- 🧪 Use the **Python scripts** directly (fully customizable)
- 📬 **Receive a daily AI newsletter** — no code required, just subscribe
- ⚙️ Explore the **n8n visual workflows** if you prefer low-code tools

---

## ✨ Features

- **Multi-source aggregation**: Reddit + VentureBeat  
- **AI-powered summarization**: DeepSeek or Gemini  
- **Email delivery**: Daily summaries via Gmail  
- **Modular architecture**: Easy to adapt or extend  

---

## 🐍 Python Scripts

### `reddit_ai_news.py`

- Fetches recent AI-related posts from Reddit  
- Summarizes them using DeepSeek  
- Sends the result by email to listed subscribers  

---

### `venturebeat_ai_news.py`

- Parses the latest articles from VentureBeat’s AI RSS feed  
- Generates a thematic summary using DeepSeek  
- Sends the digest via email  

---

## ⚙️ Setup & Usage (for Developers)

You can run these scripts manually or customize them for your own workflows.

### 🔧 Prerequisites

- Python 3.9+
- Reddit API credentials
- DeepSeek (or Gemini) API key
- Gmail account with [App Password](https://myaccount.google.com/apppasswords)

---

### 📄 Configuration – `.env` file

Create a `.env` file at the root of the project with the following content:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_REFRESH_TOKEN=your_reddit_refresh_token

DEEPSEEK_API_KEY=your_deepseek_api_key

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

---

### 👥 Manage Subscribers

List recipient emails in `subscribers.json`:

```json
{
  "subscribers": [
    "example1@gmail.com",
    "example2@gmail.com"
  ]
}
```

---

### ▶️ Run the Scripts

```bash
python reddit_ai_news.py
python venturebeat_ai_news.py
```

You can modify the prompts or integrate the scripts into your own pipelines.

---

## 📬 Receive the AI Newsletter (No Code Required)

Want to receive a **daily email** summarizing the latest AI discussions and news?

✅ No setup  
✅ No installation  
✅ Just one step:

### ➕ How to Subscribe

1. Fork this repository  
2. Add your email to the `subscribers.json` file:

```json
{
  "subscribers": [
    "your_email@example.com"
  ]
}
```

3. Submit a **Pull Request** with your changes  
4. Once approved, you’ll start receiving the daily digest automatically
 
> You can unsubscribe at any time by removing your email and submitting a new PR.

---

## 🧩 Optional: Visual Workflows with n8n

If you prefer a visual, low-code approach, this project includes an **n8n-based version** in the `n8n-version/` folder. It covers:

- Reddit AI Brief  
- VentureBeat AI Brief  
- ArXiv AI Brief

You can import and run these workflows in [n8n](https://n8n.io/) (self-hosted or cloud) and schedule them as needed.

---

## 📁 Repository Structure

```
.
├── reddit_ai_news.py
├── venturebeat_ai_news.py
├── subscribers.json
├── .env
├── requirements.txt
└── n8n-version/
    ├── reddit-ai-brief/
    ├── venturebeat-ai-brief/
    └── arxiv-ai-brief/
```

---

## 🛠️ Technologies Used

- Python (for automation scripts)  
- DeepSeek / Gemini (for summarization)  
- Reddit API & RSS feeds  
- Gmail SMTP  
- n8n (for optional visual workflows)  

---

## 🪪 License

This project is licensed under the MIT License.

---

## 👤 Author

**Adel Messaoudi**  
📩 amessaoudi.am@gmail.com  
🌍 [github.com/AdelMessaoudi-13](https://github.com/AdelMessaoudi-13)
