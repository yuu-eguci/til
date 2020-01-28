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
pipenv install --python 3.7

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
