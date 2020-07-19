App Service に SSL 証明書を適用するノート
===

公式ドキュメントはここ。

- https://docs.microsoft.com/ja-jp/azure/app-service/configure-ssl-certificate

## 無料版

`api.example.com` -> `example.azurewebsites.net` とする。

1. Onamae で cname 設定: `api` | `example.azurewebsites.net`
1. Onamae で txt 設定: `asuid.api` | `EXAMPLEFJ20Q348R2Q303JD0Q293847R08Q23UEHJD982Q3JD0Q92830890DWEDD(ドメイン検証 ID)`
    - ドメイン検証 ID(Custom Domain Verification ID): App Service > 左ペイン > Custom domains > Custom Domain Verification ID
1. App Service で左ペイン > Custom domains
    - Add custom domain > `api.example.com` を設定 > Validate > Add custom domain
1. App Service で左ペイン > TLS/SSL settings
    - Private Key Certificates > Create App Service Managed Certificates > create
1. 再び Custom domains
    - Add binding

## 有料版

`*.example.com` とする。

1. App Service Certificate を作る
    - Naked Domain Host Name: `*.example.com`
    - SKU: Wild Card
    - その他はてきとうでいいよ。
1. Certificate で左ペイン > Certificate Configuration
    - Store をクリック > Create key vault
    - Verify をクリック > 手動の検証を選ぶ。ほんで Onamae へ行く。
1. Onamae で txt 設定: `@` | [↑そこに書いてある文字列]
1. App Service で左ペイン > Settings > TLS/SSL settings
    - Private key certificates(.pfx)タブ > Import App Service Certificate > いま作った Certificate を選択
1. App Service で左ペイン > Custom domains
    - Add binding

## ひとつの SSL 証明書のみ、 custom domain にバインドできる

SSL 証明書は複数 TLS/SSL settings に追加できるが、実際に適用できるのはひとつだけ。

1. 左ペイン > Custom domains > Add binding

(2020-07-18)ん……? Custom domains ではないわ。もしかしたら、一番最初はそこでもいいのかも。

1. TLS/SSL settings > pfx タブ > 複数の証明書がある
1. Bindings タブ > ドメインをクリックして、ラジオボタンから好きな証明書を選ぶ
