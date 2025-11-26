import json
from typing import List, Dict
from google import genai
from api.service.loader import loadPrompt


def getSummary(articles: List[Dict]) -> List[Dict]:
    # プロンプト読み込み              
    prompt = loadPrompt("prompt")  

    # Gemini API 呼び出し用に記事データを整形
    input_articles = []
    for a in articles: 
        input_articles.append({
            "title": a.get("title", ""),
            "description": a.get("description", []),
        })
    input_json = json.dumps(input_articles, ensure_ascii=False)

    # Gemini API 呼び出し
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            "\n\n# 以下、入力記事\n",
            input_json,
        ]
    )

    # Gemini の返却値をパース
    try:
        raw_text = response.text.strip()
        summary = json.loads(raw_text)
    except json.JSONDecodeError:
        # もし壊れた JSON が返ってきたとき
        raise RuntimeError(f"Gemini からの JSON パースに失敗しました: {raw_text[:200]}")

    return summary