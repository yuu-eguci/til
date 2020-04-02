Azure の Storage Account へ静的サイトをデプロイするノート
===

こちらは Azure の料金計算ツール。 [https://azure.microsoft.com/ja-jp/pricing/calculator/](https://azure.microsoft.com/ja-jp/pricing/calculator/)

## Storage Account を静的サイト用に作る

- パフォーマンス Standard
    - Premium にすると、「ページ BLOB のみがサポートされます」と出る。
    - どうやら「ページ BLOB」というのは静的サイトではないらしい。
- アカウントの種類  StorageV2
- レプリケーション ローカル冗長ストレージ(LRS)

## npm プロジェクトをビルドしてデプロイする yml

```yaml
trigger:
- dev

pool:
  vmImage: 'windows-latest'

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '10.x'
  displayName: 'Install Node.js'

- script: |
    npm install
  displayName: 'npm install'

- script: |
    npm run build
  displayName: 'npm run build'

- script: |
    npm run test:unit
  displayName: 'npm run test:unit'

- script: |
    dir
  displayName: 'list cwd contents (verify build)'

# @4 occurs error, AzCopy.exe exited with non-zero exit code while uploading files to blob storage
# @3,2 occurs warning, The names of some imported commands from the module 'AzureRM.Websites' include unapproved verbs that might make them less discoverable
# but it cannot be solved. Just ignore it.
- task: AzureFileCopy@3
  inputs:
    SourcePath: 'dist'
    azureSubscription: '...'
    Destination: 'AzureBlob'
    storage: '...'
    ContainerName: '$web'
```

### 出た問題

- There was a resource authorization issue
    - 選んでいる subscription の権限が必要。
- Failed to obtain the Json Web Token(JWT) using service principal client ID.
    - Destination Type を選択していないと出る。上から順番に選びましょう。
