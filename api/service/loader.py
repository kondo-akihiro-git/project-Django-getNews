import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def loadPrompt(name: str) -> str:
    path = os.path.join(BASE_DIR, "prompts", f"{name}.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
