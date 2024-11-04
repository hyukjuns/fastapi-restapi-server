# FastAPI Sample API Server

### CI/CD
- CI: Github Actions
    1. Commit & Merge
    2. Test
    3. Build & Push Docker Image
    4. Delivery to Container Registry
    5. Modify Deployment Manifest (Image Tag)
- CD: ArgoCD
    1. Detect Deployment Manifest (Image Tag)
    2. Deploy to Cluster (Rolling Update, Blue/Green, Canary)

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

### Build
```
# AMD64
docker build --platform linux/amd64 --no-cache -t hyukjun/fastapi-sample-webapp:v0.0.1 .
```

### Reference
- [yq](https://mikefarah.gitbook.io/yq)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Source Code](https://github.com/fastapi/fastapi)
- [virtual-environments](https://fastapi.tiangolo.com/virtual-environments/#install-packages-directly)
- [FastAPI in Production](https://dev.to/dpills/fastapi-production-setup-guide-1hhh#setup)
- [Gunicorn을 Uvicorn의 프로세스 매니저로 더이상 사용하지 않아도 되는 이유](https://fastapi.tiangolo.com/deployment/docker/#single-container)
    - Uvicorn에 서브 프로세스 들을 생성하고 관리할 수 있는 기능이 추가되었음 (다운된 프로세스 재시작 등)
- [Uvicorn Setting](https://www.uvicorn.org/settings/)
- [One process per Container](https://fastapi.tiangolo.com/deployment/docker/#one-process-per-container)
    - Containerized 해서 k8s에 배포할 거면 Worker 프로세스를 여러개 만들 필요 없음, 컨테이너당 1개의 프로세스면 충분, replication은 pod로 하면 됨
- [Github Action-Python Build](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)
- [best-practices-for-rest-api-design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [\[Python\] Class의 연산자, 특수 메서드, 상속, 그리고 pydantic](https://devocean.sk.com/blog/techBoardDetail.do?ID=164774)
- [Uvicorn Logging](https://gist.github.com/liviaerxin/d320e33cbcddcc5df76dd92948e5be3b)