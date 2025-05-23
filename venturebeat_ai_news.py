import feedparser
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

def fetch_rss_feed():
    """Fetch the VentureBeat AI RSS feed"""
    try:
        feed_url = "https://venturebeat.com/category/ai/feed/"
        feed = feedparser.parse(feed_url)
        
        if not feed.entries:
            print("Warning: No entries found in the RSS feed")
            return []
            
        # Limit to first 7 items
        return feed.entries[:7]
    except Exception as e:
        raise Exception(f"Error fetching RSS feed: {str(e)}")

def process_articles(articles):
    """Process and format articles for summarization"""
    processed_articles = []
    
    for article in articles:
        # Extract relevant information
        title = article.get('title', '')
        link = article.get('link', article.get('guid', ''))
        content = article.get('summary', '')
        pub_date = article.get('published', '')
        
        # Format article text
        article_text = f"📄 Titre : {title}\n"
        article_text += f"🔗 Lien : {link}\n"
        article_text += f"📜 Résumé original : {content}\n"
        
        processed_articles.append({
            'fullText': article_text,
            'title': title,
            'link': link,
            'date': pub_date
        })
    
    return processed_articles

def aggregate_articles(articles):
    """Combine all article texts into one string"""
    full_text = ""
    for article in articles:
        full_text += article['fullText'] + "\n\n"
    
    return full_text

def generate_ai_summary(text):
    """Generate a summary using DeepSeek API"""
    # Check if DeepSeek API key is set
    if not os.getenv("DEEPSEEK_API_KEY"):
        raise ValueError("Missing required environment variable: DEEPSEEK_API_KEY")
    
    # AI prompt
    prompt = f"""You are an AI assistant specialized in summarizing high-quality AI news for a technical and professional audience.

You are given a list of article summaries published today on VentureBeat, all focused on artificial intelligence:

{text}

Write a clear, well-structured, and comprehensive summary in fluent English.

Organize the content into **several thematic sections** (e.g., Open Models, Research, Transparency, Industry Trends, etc.), each with a short paragraph (3–6 lines). You can choose the most natural themes based on the articles.

Make sure to:
- Cover all key developments of the day
- Group related articles into meaningful sections
- Write in a neutral, informative tone — like a daily scientific briefing
- Avoid bullet points. Use full sentences and short paragraphs
- Include a **References** section at the end, listing each article title with its link

Stay under 700 words.
"""
    
    # Call to DeepSeek API
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
                                json=data)  # No timeout as DeepSeek API can be slow
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error calling DeepSeek API: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error when calling DeepSeek API: {str(e)}")

def convert_to_html(markdown_text):
    """Convert markdown to HTML"""
    return markdown.markdown(markdown_text)

def send_email(html_content):
    """Send email with the AI summary"""
    # Check if email credentials are set
    required_vars = ["EMAIL_SENDER", "EMAIL_PASSWORD"]
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")
    
    # Email configuration
    sender_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = "amessaoudi.am@gmail.com"
    
    # Formatted date
    today = datetime.datetime.now().strftime("%d %b %Y")
    
    try:
        # Send email via Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            
            # Create message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient
            msg["Subject"] = f"📬 Daily AI News (VentureBeat) – {today}"
            
            # Email body
            email_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🧠 Daily AI Flash — Summary of VentureBeat AI News</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 30px;">
  <div style="max-width: 700px; margin: auto; background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">

    <h2 style="color: #4A90E2;">🧠 Daily AI Flash — Summary of VentureBeat AI News</h2>
    <p style="color: #666; font-size: 14px;">
      Report from <strong>{today}</strong>
    </p>

    <div style="margin-top: 20px; color: #333; line-height: 1.6; font-size: 15px;">
      {html_content}
    </div>

    <hr style="margin-top: 30px; border: none; border-top: 1px solid #eee;" />

    <p style="font-size: 13px; color: #999;">
      This summary was automatically generated from VentureBeat by an AI agent designed by Adel Messaoudi.
      <br />
      📡 A daily briefing on artificial intelligence delivered straight to your inbox.
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

def main():
    # Fetch RSS feed
    articles = fetch_rss_feed()
    
    if not articles:
        print("No articles found. Exiting.")
        return
    
    # Process articles
    processed_articles = process_articles(articles)
    
    # Aggregate articles
    full_text = aggregate_articles(processed_articles)
    
    # Generate AI summary
    ai_summary = generate_ai_summary(full_text)
    
    # Convert to HTML
    html_content = convert_to_html(ai_summary)
    
    # Send email
    send_email(html_content)
    
    print(f"Email sent successfully with a summary of VentureBeat articles!")

if __name__ == "__main__":
    main()
