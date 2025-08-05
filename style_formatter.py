def format_output(company, summary, link, style="formal"):
    if not summary or "Couldn't extract" in summary:
        return f"- {summary}\n🔗 [Read more]({link})"

    if style == "formal":
        return f"- {summary}\n🔗 [Read more]({link})"
    
    elif style == "casual":
        return f"📰 So, here's what's up with {company} — {summary}\n👉 [Check it out]({link})"
    
    elif style == "bullet":
        bullets = "\n".join([f"• {line.strip()}" for line in summary.split('.') if line.strip()])
        return f"{bullets}\n🔗 [Read more]({link})"
    
    else:
        return f"- {summary}\n🔗 [Read more]({link})"
