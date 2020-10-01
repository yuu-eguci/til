AzureFunctionsNote
===

## Document

- https://docs.microsoft.com/ja-jp/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python

## はじめかた

- VSCode で Azure Functions 拡張機能をインストール。
- `npm i -g azure-functions-core-tools`
- プロジェクト追加
    - コマンドパレットで Azure Functions: Create Function
    - Python 選択
    - HTTP trigger 選択
    - 承認レベルには Anonymous

## 実行しかた

- F5
- あるいは `func start --functions FUNCTION_NAME FUNCTION_NAME`

***

- HttpTrigger についてはフツーに url を開く。
- TimerTrigger についてはしばらく待つ
    - `"schedule": "0 */1 * * * *"` にすれば分に1回実行される。

## 問題: You must have the Azure Functions Core Tools installed to debug your local functions.

azure-functions-core-tools をインストールしたのにずっとこれが出続ける現象がある。以前はできたんだけどなー。でも↑に示した `func start` は動いたのでこれを使ってくれ。

```bash
# これでもだめ
brew tap azure/functions
brew install azure-functions-core-tools@3

# これでもだめ
npm install -g azure-functions-core-tools
```
