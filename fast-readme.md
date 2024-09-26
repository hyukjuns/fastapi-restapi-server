### FastAPI

### 기능 구현
- print all data
- Print hostname
- print header
- Check Init, Ready, Live Status
- Print Access Log to STDOUT
- Print Error Log to STDOUT
- WSGI

### 작업세팅

```markdown
python3 -m venv .venv
source .venv/bin/activate
# which python
# python -m pip install --upgrade pip
pip install "fastapi[standard]"
# pip install -r requirements.txt
fastapi dev main.py
deactivate
```

### Docs & Learn
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Source Code](https://github.com/fastapi/fastapi)
- [virtual-environments](https://fastapi.tiangolo.com/virtual-environments/#install-packages-directly)