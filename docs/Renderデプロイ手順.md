# Django（Gunicorn）を Render にデプロイする手順

## 1. プロジェクト準備

- `requirements.txt` を作成する 

    ```
    pip freeze > requirements.txt
    ``` 


## 2. Render の Web Service を作成

1. Render ダッシュボード から **New Web Service** を選択する
2. GitHub リポジトリを選択する
3. 以下の設定を行う

* **Environment**: Python 3
* **Region**: ※ Singaporeしか選択できなかった気がします。
* **Instance Type**: 無料
* **Branch**: master
* **Root Directory**: 空欄
* **Build Command**: pip install -r requirements.txt
* **Start Command**: gunicorn project.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
  * `$PORT` は Render が自動で割り当てる環境変数です

4. デプロイ実行


## 注意点

* デプロイ後、Render のサブドメインでアクセス確認できるのでcurl -i で叩けます。

  ```
  curl -i https://<your-service>.onrender.com/get/
  ```

* `ALLOWED_HOSTS` に Render のドメインを追加しておくこと（`settings.py`）:

  ```python
  ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "APIのURL",
  ]
  ```

* `requirements.txt` に不要なローカル専用パッケージが入っているとビルド失敗する
