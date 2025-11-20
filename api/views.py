from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.service.getNews import fetch_news
from google import genai


@api_view(['GET'])
def get_news(request):
    """
    ニュースを取得してJSONで返す
    """
    try:
        articles = fetch_news()

        client = genai.Client()

        response = client.models.generate_content(
        model="gemini-2.5-flash", contents="日本語で最新のニュースを教えてください")
        return Response({
            "output_text": response.text
        })
        
    except RuntimeError as e:
        return Response(
            {"detail": str(e)},
            status=status.HTTP_502_BAD_GATEWAY
        )

    if not articles:
        return Response(
            {"detail": "RSSフィードに記事が見つかりませんでした"},
            status=status.HTTP_502_BAD_GATEWAY
        )
    

    return Response({
        "count": len(articles),
        "articles": articles,
    })
