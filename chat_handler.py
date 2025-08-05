def is_small_talk(msg):
    msg = msg.lower().strip()
    return any(word in msg for word in ["hi", "hello", "how are you", "hey", "what's up", "morning", "evening","priya"])

def handle_small_talk(msg):
    return "👋 Hey there! I'm your smart news bot. Just type a company name and I'll get the latest news for you!"
