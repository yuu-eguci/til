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

## 別の Azure アカウントへ App Service Certificate をエクスポート -> インポートする

エクスポートは PowerShell でやらないといけない。(マジクソ)
具体的な手順がここに無いとスゲー面倒だったのでちゃんと書く。(むしろ前に書かなかったのがアホ)

### 参考リンク

- https://stackoverflow.com/questions/38836724/export-azure-ssl-certificate-as-pfx-file
- このページもわかりやすい。 http://raaviblog.com/how-to-create-pfx-certificate-using-azure-app-service-certificate/
- 日本語記事。 https://engineer-ninaritai.com/appservice-pfx-export/

コメントにこうある通り。

> C'mon guys, make this a one button export.

マジでな。
インポートはノリでわかるよ。

- これ↑は2度目でもマジでわかった。ノリでわかる。
- ただ1点だけ、 Upload するのは KeyVault ではないよ。

### 手順

- PowerShell 管理者権限起動。
- `Set-ExecutionPolicy bypass` と打つ。これを打たないとコマンドが実行できない(のかな?)
- `Install-Module -Name AzureRM -AllowClobber` これは必要なのかどうかわかんないが、 AzureRM コマンドを使うから必要らしい。結構時間かかる。
- これ↓↓の長いスクリプトを思考停止で打つ。
    - そのあとこれを聞かれるから、それぞれ打つ。
    - `loginId`
    - `subscriptionId`
    - `resourceGroupName`
    - `name`
- そうするとディレクトリに ptx が出現し、コンソールにはパスワードが表示される。
- それらを、インポート先の AppService TLS/SSL settings にアップロードする。そのときのパスワードを入力する。

```powershell
Param(
[Parameter(Mandatory=$true,Position=1,HelpMessage="ARM Login Url")]
[string]$loginId,
 
[Parameter(Mandatory=$true,HelpMessage="Subscription Id")]
[string]$subscriptionId,
 
[Parameter(Mandatory=$true,HelpMessage="Resource Group Name")]
[string]$resourceGroupName,
 
[Parameter(Mandatory=$true,HelpMessage="Name of the App Service Certificate Resource")]
[string]$name
)
 
###########################################################
 
Login-AzureRmAccount
Set-AzureRmContext -SubscriptionId $subscriptionId
 
## Get the KeyVault Resource Url and KeyVault Secret Name were the certificate is stored
$ascResource= Get-AzureRmResource -ResourceId "/subscriptions/$subscriptionId/resourceGroups/$resourceGroupName/providers/Microsoft.CertificateRegistration/certificateOrders/$name"
$certProps = Get-Member -InputObject $ascResource.Properties.certificates[0] -MemberType NoteProperty
$certificateName = $certProps[0].Name
$keyVaultId = $ascResource.Properties.certificates[0].$certificateName.KeyVaultId
$keyVaultSecretName = $ascResource.Properties.certificates[0].$certificateName.KeyVaultSecretName
 
## Split the resource URL of KeyVault and get KeyVaultName and KeyVaultResourceGroupName
$keyVaultIdParts = $keyVaultId.Split("/")
$keyVaultName = $keyVaultIdParts[$keyVaultIdParts.Length - 1]
$keyVaultResourceGroupName = $keyVaultIdParts[$keyVaultIdParts.Length - 5]
 
## --- !! NOTE !! ----
## Only users who can set the access policy and has the the right RBAC permissions can set the access policy on KeyVault, if the command fails contact the owner of the KeyVault
Set-AzureRmKeyVaultAccessPolicy -ResourceGroupName $keyVaultResourceGroupName -VaultName $keyVaultName -UserPrincipalName $loginId -PermissionsToSecrets get
Write-Host "Get Secret Access to account $loginId has been granted from the KeyVault, please check and remove the policy after exporting the certificate"
 
## Getting the secret from the KeyVault
$secret = Get-AzureKeyVaultSecret -VaultName $keyVaultName -Name $keyVaultSecretName
$pfxCertObject= New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 -ArgumentList @([Convert]::FromBase64String($secret.SecretValueText),"",[System.Security.Cryptography.X509Certificates.X509KeyStorageFlags]::Exportable)
$pfxPassword = -join ((65..90) + (97..122) + (48..57) | Get-Random -Count 50 | % {[char]$_})
$currentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath
[Environment]::CurrentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath
[io.file]::WriteAllBytes(".\appservicecertificate.pfx",$pfxCertObject.Export([System.Security.Cryptography.X509Certificates.X509ContentType]::Pkcs12,$pfxPassword))
 
## --- !! NOTE !! ----
## Remove the Access Policy required for exporting the certificate once you have exported the certificate to prevent giving the account prolonged access to the KeyVault
## The account will be completely removed from KeyVault access policy and will prevent to account from accessing any keys/secrets/certificates on the KeyVault, 
## Run the following command if you are sure that the account is not used for any other access on the KeyVault or login to the portal and change the access policy accordingly.
# Remove-AzureRmKeyVaultAccessPolicy -ResourceGroupName $keyVaultResourceGroupName -VaultName $keyVaultName -UserPrincipalName $loginId
# Write-Host "Access to account $loginId has been removed from the KeyVault"
 
# Print the password for the exported certificate
Write-Host "Created an App Service Certificate copy at: $currentDirectory\appservicecertificate.pfx"
Write-Warning "For security reasons, do not store the PFX password. Use it directly from the console as required."
Write-Host "PFX password: $pfxPassword"
```
