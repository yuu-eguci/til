App Service Logging Note
===

App Service のログをずっと保存するために色々試したよ

## Log Analytics へ保存

- 左ペイン Diagnostic settings(preview) > Add diagnostic setting
- log: 欲しいログを足す。
    - Linux コンテナで足せるものはここの表に書いてある
    - https://docs.microsoft.com/ja-jp/azure/app-service/troubleshoot-diagnostic-logs#supported-log-types
- Destination details: Send to Log Analytics workspace

ここで Log Analytics resource を足すわけだけど、これは先に用意しておいたほうがいい。
でないとデフォルトのめちゃくちゃな名前のやつが自動で作られちゃうからね。 Resource group も自動的に割り当てられちゃうし。

- 左ペイン Logs
- ここで KQL を使ってログを検索したりできる。 KQL 構文は、エディタの中で予測で出してくれるから勘でいける。

```kql
AppServiceConsoleLogs 
| where TimeGenerated > datetime(2021-02-09T04:00:00Z) and TimeGenerated < datetime(2021-02-09T12:00:00Z)
| where ResultDescription !contains "debug: xxxx"
| where ResultDescription != " "
| limit 200
```

- 上のメニュー Export から CSV ダウンロードが可能。カラムを絞ったりもできる。
- ダウンロードできた CSV は改行だらけで見づらいので、置換とかで改行を削除すると Excel でまだ見やすくなるかも。

### Retention 設定

- Log Analytics resource > 左ペイン Usage and estimated consts > 上メニューの Data Retention から設定できる


## Storage Account へ保存

Destination details を選ぶ前までは上と同じ。

- Destination details: Archive to a storage account

ここで Storage Account を足すわけだけど、やはりこれも先に用意しておいたほうがいいと思う。
StorageV2 か Blob storage かって話だけど MS 推奨は StorageV2 っぽい。

### Retention 設定

- Storage Account の場合は Add diagnostic setting に日数を記述するトコがある
