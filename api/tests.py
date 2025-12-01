from django.test import TestCase
from rest_framework.test import APIClient

class GetNewsAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_news(self):
        """
        OKパターン ： /get/ を10回叩いて全て成功の場合OK
        """
        
        url = "/get/"
        for i in range(10):
            print(f"---------- API 呼び出し {i+1} 回目 ----------")

            response = self.client.get(url)
            self.assertEqual(
                response.status_code,
                200,
                msg=f"{i+1}回目で失敗: {response.status_code} / {response.content}"
            )
