# 　ニュース取得API

**ニュース取得API** は、Googleニュースから最新記事を取得し、生成AIで要約して LINE に自動送信するためのミニマルな通知システムです。AWS Lambda と EventBridge を利用し、毎日自動でニュースを受け取ることができます。

<kbd>
<img width="420" height="820" alt="sample" src="https://github.com/user-attachments/assets/1c2f2a11-aaaa-bbbb-cccc-111122223333" />
</kbd>
</br></br>

## 特徴

- Googleニュース から最新ニュースを取得
- Gemini API によるニュースの要約生成
- LINE Messaging API を利用して自動でニュース通知

## 使用技術

### バックエンド（APIサーバ）
- **Django REST Framework**: DjangoのAPIフレームワーク
- **feedparser**: Google News RSS のパース
- **BeautifulSoup4**: RSS の HTML テキスト抽出
- **google-genai**: Gemini API への要約指示と JSON 生成  

### 生成AI（要約生成）
- **Gemini 2.5 Flash**: 記事タイトル＋説明文を元に要約を生成  

### LINE 連携
- **LINE Messaging API**: 整形済みニュースをプッシュ通知として送信  

### cron実行（AWS）
- **AWS Lambda**: API サーバの実行
- **AWS EventBridge**: Cron スケジュールで毎日実行  
- **CloudWatch Logs**: Lambda 実行ログを管理


