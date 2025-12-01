import feedparser
from bs4 import BeautifulSoup

# RSS フィード URL（日本語ニュース）
RSS_FEED_URL = "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE5mTTJRU0FtcGhLQUFQAQ?hl=ja&gl=JP&ceid=JP:ja"


def fetch_news():
    """
    GoogleニュースRSSから最新の日本語ニュースを取得
    """
    try:
        feed = feedparser.parse(RSS_FEED_URL)
    except Exception as e:
        raise RuntimeError(f"RSSフィードの取得に失敗しました: {e}")

    if not feed.entries:
        return []

    articles = []
    for entry in feed.entries:
        raw_description = getattr(entry, "summary", "")
        soup = BeautifulSoup(raw_description, "html.parser")

        # <li>ごとに分けてプレーンテキストのリストを作成
        description_list = [li.get_text(strip=True) for li in soup.find_all("li")]

        articles.append({
            "title": entry.title,
            "description": description_list,
        })

    return articles
