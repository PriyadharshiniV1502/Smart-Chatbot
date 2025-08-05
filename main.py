from company_cleaner import clean_company_names
from web_search import search_news
from scraper import extract_article_text
from summarizer import summarize_text
from style_formatter import format_output
from chat_handler import is_small_talk, handle_small_talk

def process_input(user_input, style="formal"):
    if is_small_talk(user_input):
        return handle_small_talk(user_input)
    
    companies = clean_company_names(user_input)
    if not companies:
        return "❌ Couldn't find any valid company names in your input."

    output = ""
    for company in companies:
        output += f"\n🔍 **{company} News**\n"
        news_links = search_news(company)
        if not news_links:
            output += "- No news found.\n"
            continue
        
        for title, link in news_links:
            text = extract_article_text(link)
            summary = summarize_text(text)
            result = format_output(company, summary, link, style)
            output += result + "\n\n"
    
    return output

def main():
    print("🧠 Smart News Chatbot Ready!")
    style = "bullet"  # Change to "formal" or "casual" as needed

    while True:
        user_input = input("Enter company name(s): ")
        print(process_input(user_input, style))

if __name__ == "__main__":
    main()
