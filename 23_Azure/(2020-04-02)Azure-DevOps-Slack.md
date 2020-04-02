Azure DevOps と Slack の連携
===

## 手順

この中に Azure Pipelines Slack app へのリンクがあるからそこからチャンネルにインストール。

- https://docs.microsoft.com/en-us/azure/devops/pipelines/integrations/slack?view=azure-devops

```plaintext
# private channel だったら invite 必要。
/invite @azpipelines

# /github なノリで購読する。
/azpipelines subscribe https://dev.azure.com/..../_build?definitionId=xxx
/azpipelines subscribe https://dev.azure.com/..../_release?definitionId=xxx

# サブスクライブしているものを確認したいとき、削除したいとき。
/azpipelines subscriptions
```

## Configuration failed. Please make sure that the organization '{organization name}' exists and that you have sufficient permissions.

ここで解説されてるけど

- https://docs.microsoft.com/en-us/azure/devops/pipelines/integrations/slack?view=azure-devops#configuration-failed-please-make-sure-that-the-organization-organization-name-exists-and-that-you-have-sufficient-permissions

以下手順で。

- https://aka.ms/VsSignout から DevOps サインアウト。
- https://aex.dev.azure.com/me から対象のところへサインイン。
- Slack で `/azpipelines signout` -> `/azpipelines signin`
