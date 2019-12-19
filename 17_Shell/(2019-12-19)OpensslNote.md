OpensslNote
===

## 基本形式

```bash
openssl [サブコマンド] [オプション]
```

## openssl version

openssl のバージョン情報の表示。

```bash
# openssl のバージョン確認。
openssl version

# 全情報を確認。
openssl version -a
```

### 出力例

```plaintext
$ openssl version
OpenSSL 1.1.1c  28 May 2019

$ openssl version -a
OpenSSL 1.1.1c  28 May 2019
built on: Tue May 28 18:32:49 2019 UTC
platform: mingw64
options:  bn(64,64) rc4(16x,int) des(long) idea(int) blowfish(ptr)
compiler: gcc -m64 -Wall -O3 -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM -DX25519_ASM -DPOLY1305_ASM -DUNICODE -D_UNICODE -DWIN32_LEAN_AND_MEAN -D_MT -DZLIB -DZLIB_SHARED -DNDEBUG -D__MINGW_USE_VC2005_COMPAT -DOPENSSLBIN="\"/mingw64/bin\""
OPENSSLDIR: "/mingw64/ssl"
ENGINESDIR: "/mingw64/lib/engines-1_1"
Seeding source: os-specific
```

## openssl dgst

メッセージダイジェストの計算。

```bash
# ランダムの元データを作成。
openssl dgst [-md5|-md4|-md2|-sha] > rand.dat
```

※ よくわからん。

## openssl genrsa

RSA 形式の秘密鍵の作成。

```bash
openssl genrsa
    -out filename       # 出力する秘密鍵のファイル名。 private-key.pem とか。
    -rand file          # ランダムデータの元となるファイル。
    -des|-des3|-idea    # 利用する暗号化の方式。
    nubits              # 生成する秘密鍵のビット数。ゼッタイ最後につける。
```

### 例

```bash
openssl genrsa -out private-key.pem 2048
```

## openssl req

証明書の署名要求(CSR)の作成。

```bash
openssl req
    -new                # 新規に CSR 作成。
    -in filename        # 入力する CSR のファイル名。(入力ってどういうことやねん。)
    -out filename       # 出力する CSR のファイル名。
    -key filename       # 秘密鍵の名前。パスフレーズつきのときは入力することになる。
                        # あー、ここでパスフレーズ使うんだ。
    -x509               # X.509 形式の CSR を作成。
    -days n             # 証明書の有効期限。
```

このあとディスティングイッシュネーム(サーバの情報)をきかれる。

### 例

```bash
openssl req -new -x509 -days 365 -key private-key.pem -out csr.pem
```

## openssl x509

X.509 証明書ファイルの表示。

```bash
openssl x509
    -in filename        # 入力する証明書
    -out filename       # 出力する証明書のファイル名。
    -inform DER|PEM|NET # 入力ファイルの書式。
    -outform same       # 出力ファイルの書式。
    -days n             # 証明書の有効期限。
    -text               # テキスト形式で表示。
    -noout              # 出力ファイルに出力しない。
```

## openssl rsa

```bash
openssl rsa
# 情報未発見。↑ openssl x509 のオプションと同じ感じか?
```
