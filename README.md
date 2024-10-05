# FastAPI Sample API Server

### REST API Features
- return hostname
- return request header
- return player ranks

### Environment
- Python > 3.11.x
- FastAPI > 0.115.0

### Set Up
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

### Reference
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Source Code](https://github.com/fastapi/fastapi)
- [virtual-environments](https://fastapi.tiangolo.com/virtual-environments/#install-packages-directly)