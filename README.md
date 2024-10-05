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
- [FastAPI in Production](https://dev.to/dpills/fastapi-production-setup-guide-1hhh#setup)
- [Gunicorn을 Uvicorn의 프로세스 매니저로 더이상 사용하지 않아도 되는 이유](https://fastapi.tiangolo.com/deployment/docker/#single-container)
    - Uvicorn에 서브 프로세스 들을 관리할 수 있는 기능이 추가되었음 (다운된 프로세스 재시작 등)
- [Uvicorn Setting](https://www.uvicorn.org/settings/)
- [One process per One Container](https://fastapi.tiangolo.com/deployment/docker/#one-process-per-container)
    - Containerized 해서 k8s에 배포할 거면 Worker 프로세스를 여러개 만들 필요 없음, 컨테이너당 1개의 프로세스면 충분, replication은 pod로 하면 됨