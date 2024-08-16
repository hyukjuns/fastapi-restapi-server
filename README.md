# python-sample-webapp
python-sample-webapp

## Use For
- Pod의 Hostname, IP Address 확인
- Pod가 존재하는 Node 정보 확인

## App Info
- Python 3.9.1

    - Port: 8080

- Flask 3.x
- Gunicorn (예정)

## Setup
```markdown
1. Python 버전 세팅
pyenv local 3.9.1
2. 가상환경 세팅
python -m venv .venv
3. 가상환경 활성화
source .venv/bin/activate
4. 라이브러리 설치
pip install -r requirements.txt
```

## Check Container Image Arch
```bash
docker inspect IMAGE | grep -i arch
```

## Pod에 K8s API 권한 부여

```markdown
# Namespace: api
# 1. SA, Role, Rolebinding 생성
k create sa SA_NAME -n NAMESAPCE
k create role ROLE_NAME -n NAMESAPCE --verb=list,get --resource=pod
k create rolebinding ROLE_BINDING_NAME -n NAMESAPCE --role=ROLE_NAME --serviceaccount=NAMESAPCE:SA_NAME 

# 2. 권한 테스트
k auth can-i list pod -n api --as system:serviceaccount:api:api-sa

# 3. Pod 가 SA 사용하도록 연결
...
spec:
  serviceAccountName: SA_NAME
  containers:
    ...
```