from rapidfuzz import process

COMPANIES = ["Google", "Microsoft", "Apple", "Amazon", "Meta", "Tesla", "Netflix", "Samsung", "Intel"]

def clean_company_names(user_input):
    cleaned = []
    for name in user_input.split(","):
        name = name.strip()
        match, score, _ = process.extractOne(name, COMPANIES)
        if score > 60:
            cleaned.append(match)
    return list(set(cleaned))
