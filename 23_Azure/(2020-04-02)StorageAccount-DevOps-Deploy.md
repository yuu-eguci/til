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

## Classic editor を使って vue-cli プロジェクトを pipeline でビルド、 release でデプロイする

### Pipeline

- New pipeline で **Use the classic editor** を選ぶ。
- GitHub から repository と branch を選ぶ。
- Select a template で **Empty job** を選ぶ。
- Pipeline で **Name** を決めて、 **Agent pool** と **Agent Specification** あたりをいじる。どれがダメでどれがイイのかはわからんけど、ここは Ubuntu にしといた。
- **Agent job 1** はそのままでいい。
- Agent job1 の横の **+** を押して **Bash** を add する。
  - ビルドのコマンドを書く。 `yarn install` `yarn test:unit` `yarn build`。 dist フォルダにビルドファイルができるように。
- **+** を押して **Copy files** を add する。
    - **Source Folder** に `$(Build.SourcesDirectory)/dist`
    - **Target Folder** に `$(Build.ArtifactStagingDirectory)`
- **+** を押して **Archive files** を add する。
    - そのままでいい。
- **+** を押して **Publish build artifacts** を add する。
    - そのままでいい。
- Triggers で、ブランチに変更があったときと、ブランチに PR があったときを設定する。
- **Save and queue** を押す。

### Release

- New release pipeline。
- Select a template で **Empty job** を選ぶ。
- **Add an artifact** を押して **Source** に先程のビルド pipeline を設定。
- 稲妻マークを押して先程の pipeline をデプロイのトリガーに設定。
- **Tasks** を押す。
- **Agent job** を押して **Agent Specification** を設定。どれがイイのかはわからんけど Ubuntu はダメ。
- **+** を押して **Extract files** を add する。
    - **Archive file patterns** に `**/$(Build.BuildId).zip`
    - **Destination folder** に `$(Build.DefaultWorkingDirectory)/$(Build.BuildId)`
- **+** を押して **Azure CLI** を add する。
    - Storage Account のある **Azure subscription** を選択。
    - **Script Location** に **Inline script**。
    - **Inline Script** に以下のスクリプト。 STORAGE_ACCOUNT_NAME と STORAGE_ACCOUNT_ACCESS_KEY を埋める。
    - **Working Directory** に `$(System.DefaultWorkingDirectory)/$(Build.BuildId)/dist`

```
az storage blob upload-batch --account-name STORAGE_ACCOUNT_NAME --account-key STORAGE_ACCOUNT_ACCESS_KEY --destination '$web' --source ./
```

- **Save** してから **Create release**。