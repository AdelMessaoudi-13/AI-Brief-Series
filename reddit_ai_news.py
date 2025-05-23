import praw
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def search_reddit():
    # Check if environment variables are set
    required_vars = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_REFRESH_TOKEN"]
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    # Reddit API configuration
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="AI News Aggregator",
            refresh_token=os.getenv("REDDIT_REFRESH_TOKEN")
        )
    except Exception as e:
        raise Exception(f"Failed to initialize Reddit API: {str(e)}")

    # Subreddits to search
    subreddits = "ArtificialIntelligence+MachineLearning+OpenAI+DeepLearning+aipapers+LocalLLaMA+HuggingFace+AI_Startup"

    try:
        # Search for posts
        posts = reddit.subreddit(subreddits).search("Artificial Intelligence", sort="new", limit=20)

        # Extract only text from posts
        all_text = ""
        for post in posts:
            all_text += post.selftext + "\n\n"

        if not all_text.strip():
            print("Warning: No content found in Reddit posts")

        return all_text
    except Exception as e:
        raise Exception(f"Error fetching Reddit posts: {str(e)}")

def generate_ai_summary(text):
    # Check if DeepSeek API key is set
    if not os.getenv("DEEPSEEK_API_KEY"):
        raise ValueError("Missing required environment variable: DEEPSEEK_API_KEY")

    # AI prompt
    prompt = f"""You are an AI research assistant tasked with curating the most important scientific and technological updates about artificial intelligence from Reddit.

You are given a collection of Reddit posts and comments:

{text}

Write a structured summary in fluent English, focusing on content that is relevant to scientific or technical monitoring. Your goal is to help researchers and engineers stay up to date with the latest important developments.

Prioritize:
- New AI models and benchmark results
- Research publications, technical reports or major papers
- Open-source tools, frameworks, or libraries
- Scientific discussions with real implications
- Major shifts in regulation, funding, or applications of AI

Whenever a source is mentioned (e.g., blog, research paper, GitHub repo, official report, interview, or tool), include the **link** if available or clearly mention the **source name** (e.g., `(source)`, `(arXiv link)`, `(GitHub)`, etc.).

Ignore anecdotal, humorous, speculative or off-topic posts unless they reveal a significant trend.

Group your summary by themes if possible, and write clearly and concisely in paragraph form (no bullet points). Stay under 700 words.
"""

    # Call to DeepSeek API (or other LLM model)
    headers = {
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions",
                                headers=headers,
                                json=data)  # Remove timeout as DeepSeek API can be slow

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error calling DeepSeek API: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error when calling DeepSeek API: {str(e)}")

def convert_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def send_email(html_content, recipients):
    # Check if email credentials are set
    required_vars = ["EMAIL_SENDER", "EMAIL_PASSWORD"]
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    # Email configuration
    sender_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    # Formatted date
    today = datetime.datetime.now().strftime("%d %b %Y")

    try:
        # Send email via Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)

            for recipient in recipients:
                # Create message
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = f"📬 Daily AI News (Reddit) – {today}"

                # Email body
                email_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🧠 Daily AI Flash — Reddit AI News Summary</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 30px;">
  <div style="max-width: 700px; margin: auto; background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h2 style="color: #4A90E2;">🧠 Daily AI Flash — Reddit AI News Summary</h2>
    <p style="color: #666; font-size: 14px;">
      Report from <strong>{today}</strong>
    </p>
    <div style="margin-top: 20px; color: #333; line-height: 1.6; font-size: 15px;">
      {html_content}
    </div>
    <hr style="margin-top: 30px; border: none; border-top: 1px solid #eee;" />
    <p style="font-size: 13px; color: #999;">
      This summary was generated by an AI agent built by Adel Messaoudi, based on Reddit content.
      <br />
      📡 A daily, focused briefing on artificial intelligence designed to deliver only what matters.
      <br />

    </p>
  </div>
</body>
</html>
"""

                msg.attach(MIMEText(email_body, "html"))
                server.send_message(msg)
                print(f"Email sent to {recipient}")
    except smtplib.SMTPException as e:
        raise Exception(f"Error sending email: {str(e)}")

def load_subscribers():
    try:
        # Use absolute path for better reliability, especially with GitHub Actions
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subscribers_path = os.path.join(script_dir, "subscribers.json")

        with open(subscribers_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, return an empty list
        return {"subscribers": []}

def main():
    # Retrieve Reddit posts
    reddit_text = search_reddit()

    # Generate AI summary
    ai_summary = generate_ai_summary(reddit_text)

    # Convert to HTML
    html_content = convert_to_html(ai_summary)

    # Load subscribers
    subscribers_data = load_subscribers()
    recipients = subscribers_data["subscribers"]

    # Add default address if no subscribers
    if not recipients:
        recipients = ["amessaoudi.am@gmail.com"]

    # Send email
    send_email(html_content, recipients)

    print(f"Email sent successfully to {len(recipients)} recipients!")

if __name__ == "__main__":
    main()
