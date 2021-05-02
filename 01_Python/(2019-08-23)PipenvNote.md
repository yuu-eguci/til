Pipenv Note 
===

## Commands

```bash
# Get pipenv
pip install pipenv
python -m pip install pipenv

# Mac 
brew install pipenv
```

```bash
# Create virtual env.

# If you don't have neither Pipfile nor Pipfile.lock
# You have to have the python version in your PC.
pipenv install --python 3.8

# If you have Pipfile
pipenv install
# Install packages for dev as well
pipenv install --dev

# Install packages not using Pipfile but using Pipfile.lock
pipenv sync
pipenv sync --dev 
```

```bash
# Install pip modules.
pipenv install MODULE1 MODULE2 ...
pipenv install --dev MODULE1 MODULE2 ...
```

```bash
# Start virtual env.
pipenv shell

# Start virtual env without using shell
pipenv run python ***.py
```

```bash
# Display actual path of virtual env.
pipenv --venv

# Remove virtual env.
pipenv --rm
```

```bash
# requirements.txt
pipenv lock -r > requirements.txt

# Locking Failed! って言われたとき。
pipenv lock --clear
```

```bash
# Install from requirements.txt
pipenv install -r ./requirements.txt
```

## dotenv は必要ないカモ?

> プロジェクトに .env ファイルを用意しておくと、 pipenv run や pipenv shell を実行するときに自動で読み込んでくれます  
> https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a

こんな情報があった。次から使ってみたい。

## venv

を、使いたい場合はこれがラクそう。

https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3
