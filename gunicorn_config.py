import multiprocessing

# 로그 스트림 출력
accesslog = '-'
errorlog = '_'

# Worker and Thread
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4
threads = 4

# Worker 당 최대 요청 처리 개수 지정
max_requests = 5000

# Socket 타임아웃(초) 지정
timeout = 120
bind = '0.0.0.0:8000'