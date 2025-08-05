                                                             🧠 Smart News Chatbot
A smart chatbot that finds and summarizes the latest news about any company in real-time. It supports natural conversations, different output styles,and works entirely using free, open-source tools — no paid APIs

🚀 Features


🔎 Accepts any company name(s) (e.g., Google, Tesla, Infosys)

🌐 Searches the internet in real-time (DuckDuckGo scraping)

📰 Extracts & summarizes latest news articles

💬 Supports casual chat, greetings, and non-company queries

🎨 Choose your output style:
Bullet points
Formal business summary
Casual conversational style
✅ Uses only free, open-source AI models
🌍 Simple UI built with Gradio

🛠️ Tech Stack
<img width="478" height="314" alt="image" src="https://github.com/user-attachments/assets/d7f50e4c-83cd-4d9d-b620-3d45fc217c0c" />

Folder Structures:
smart_news_chatbot/
│
├── app.py                        # Gradio UI application entry point
├── main.py                       # CLI version to run chatbot (optional)
│
├── chat_handler.py               # Handles small talk and greetings
├── company_cleaner.py            # Cleans and processes company name input
├── scraper.py                    # Extracts article content (e.g., with trafilatura)
├── style_formatter.py            # Formats summaries based on selected style
├── summarizer.py                 # Summarizes article text using HuggingFace model
├── web_search.py                 # Performs DuckDuckGo search for news links
│
├── requirements.txt              # List of Python dependencies

Install dependencies
pip install -r requirements.txt

Run the App
python app.py

Sample company names:
TCS
Infosys
tesla
zoho

Output:
<img width="781" height="364" alt="image" src="https://github.com/user-attachments/assets/a96aa7de-18ee-4a50-95ed-01cb43b8eadd" />
<img width="1523" height="770" alt="Screenshot 2025-08-05 163717" src="https://github.com/user-attachments/assets/13ca6610-cf81-4273-be62-a7c5e4e6d4f8" />



