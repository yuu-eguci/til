Storage Account に SSL 証明書を適用するノート
===

参考: Azure Storage 上の静的 Web サイトに独自ドメインを設定する

- https://avalon-studio.work/blog/azure/azure-storage-https-custom-domain/

## 無料版

`web.example.com` -> `example.azurewebsites.net` とする。

1. Storage Account で左ペイン > Azure CDN > 新しいエンドポイント
    - CDN エンドポイント名: example-cdn(.azureedge.net)
    - 配信元のホスト名: 静的 Web サイトに変更するとこだけ注意。
    - あとはてきとーに。
1. Onamae で cname 設定: `web` | `example-cdn.azureedge.net`
1. 再び Azure CDN
    - カスタムドメイン > カスタムホスト名: `web.example.com`
1. カスタムホスト > カスタムドメイン HTTPS オン
