SSH Key Note
===

## Key を作る

```bash
# これを実行すると .ssh/id_rsa と id_rsa.pub ができるよ。
ssh-keygen -t rsa -b 4096 -C "yuu@example.com"

# これで key の強度とかがわかるよ。ちゃんと 4096 になってるかな?
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

## ssh

```bash
# 鍵を使わずログインしようとする。
ssh -o PubkeyAuthentication=no USER@xxx.xxx.xxx.xxx

# 鍵を指定してログインする。
ssh -i /Users/user/.ssh/id_rsa USER@xxx.xxx.xxx.xxx
```

## GitHub に登録する

- GitHub > User Settings > SSH and GPG keys > New SSH key > id_rsa.pub

```bash
# こうすると……
ssh -T git@github.com

# こう表示される
# RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
# このサイト
#       https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints
# にあるのと同じであることを確認したら yes って打つ。
```
