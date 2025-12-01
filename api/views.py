# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.line.format import format_message
from api.line.line import send_message
from api.service.news import fetch_news
from api.service.summary import getSummary


@api_view(['GET'])
def get_news(request):

    # ニュース取得
    try:
        print("ニュース取得開始")
        articles = fetch_news()
        print(f"ニュース取得完了 (記事数={len(articles)})")
    except RuntimeError as e:
        print(f"ニュース取得エラー: {e}")
        return Response(
            {"エラー詳細": str(e)},
            status=status.HTTP_502_BAD_GATEWAY
        )
    if not articles:
        print("取得記事無しエラー")
        return Response(
            {"エラー詳細": "RSSフィードに記事が見つかりませんでした"},
            status=status.HTTP_502_BAD_GATEWAY
        )

    # 要約生成
    try:
        print("要約生成開始")
        article_summaries = getSummary(articles)
        print(f"要約生成完了 (要約数={len(article_summaries)})")
    except RuntimeError as e:
        ### **JSON パース失敗などGeminiエラー** ###
        print(f"要約生成: {e}")
        return Response(
            {"エラー詳細": str(e)},
            status=status.HTTP_502_BAD_GATEWAY
        )

   # LINE 送信準備
    print("LINEメッセージ整形中")
    formatted_message = format_message(article_summaries)

    # LINE送信
    print("LINE送信開始")
    success = send_message(formatted_message)

    return Response(
        {
            "result": "ok" if success else "line_send_failed",
            "summaries": article_summaries
        },
        status=status.HTTP_200_OK
    )