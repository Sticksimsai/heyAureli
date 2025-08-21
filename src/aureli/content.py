import os, random, yaml

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "seed_posts.yaml")

def load_posts():
    if not os.path.exists(DATA_PATH):
        return [], [], []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("posts", []), data.get("replies", []), data.get("hashtags", [])

def craft_post(line, tags=None):
    tags = tags or []
    tag = random.choice(tags) if tags else ""
    text = f"{line} {tag}".strip()
    return text[:280]

class Memory:
    def __init__(self):
        self.last_posts = []
    def seen(self, text):
        return text in self.last_posts
    def remember(self, text, keep=20):
        self.last_posts.append(text)
        if len(self.last_posts) > keep:
            self.last_posts = self.last_posts[-keep:]
