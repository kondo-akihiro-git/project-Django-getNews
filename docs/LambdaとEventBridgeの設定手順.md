# AWS Lambda と EventBridge を使って LINE 送信を定期実行する手順

## 1. Lambda 関数の作成

1. AWS コンソールで **Lambda** を開く  
2. 右上の **Create function（関数の作成）** をクリック  
3. 以下の設定を入力  
   - **Function name**: sendLineDaily（任意でOK）  
   - **Runtime**: Python 3.x  
   - **Architecture**: x86_64  
5. API呼び出しをLambda 関数にを貼り付け 
6. **Deploy**して**Test**を実行し、動作確認  
7. CloudWatch Logs にログが出ていれば正常

## 2. Lambda のタイムアウト設定変更（重要）

1. Lambda 上部タブから **設定** を選択  
2. **Timeout** を 300 秒に変更  
5. 保存

## 3. EventBridge の設定（定期実行）

1. AWS コンソールで **EventBridge** を開く  
2. **Create rule** をクリック  
3. 以下を入力  
   - **Description**: 毎日12時に Lambda 実行  
   - **Rule type**: Schedule  
   - **Target type**: Lambda 関数  
5. スケジュール設定で 9:00（JST）に実行する
    ``` 0 0 * * ? *  ```

## 注意点
 
- Render API が遅い場合があるので、タイムアウトは必ず延長しておく  
