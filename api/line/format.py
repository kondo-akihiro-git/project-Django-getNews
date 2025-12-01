# api/line/formatter.py

def format_message(article_summaries: dict) -> str:
    """
    ニュースメッセージ整形
    """

    if not article_summaries or not isinstance(article_summaries, dict):
        return "ニュースの取得に失敗しました。"

    message_lines = ["【最新のニュース】\n"]

    # 3件固定で整形
    for idx in range(1, 4):
        key = f"article{idx}"
        summary = article_summaries.get(key, "（要約が取得できませんでした）")
        message_lines.append(f"{idx}. {summary}\n")

    return "\n".join(message_lines)
