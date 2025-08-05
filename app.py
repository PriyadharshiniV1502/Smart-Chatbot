import gradio as gr
from company_cleaner import clean_company_names
from web_search import search_company_news
from scraper import extract_article_text
from summarizer import summarize_text
from style_formatter import format_output
from chat_handler import is_small_talk, handle_small_talk

def chatbot_interface(user_input, style):
    if is_small_talk(user_input):
        return handle_small_talk(user_input)

    companies = clean_company_names(user_input)
    final_output = ""

    for company in companies:
        links = search_company_news(company)
        final_output += f"\n\n🔍 **{company} News**\n"
        for link in links:
            article = extract_article_text(link)
            summary = summarize_text(article)
            final_output += format_output(company, summary, link, style) + "\n"

    return final_output

# Launch Gradio interface
gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.Textbox(label="Enter Company Name(s)", placeholder="e.g., Tesla, Google"),
        gr.Radio(["formal", "casual", "bullet"], label="Choose Summary Style", value="bullet")
    ],
    outputs=gr.Markdown(label="Latest News Summary"),
    title="🧠 Smart News Chatbot",
    description="Get real-time AI summaries of company news"
).launch()
