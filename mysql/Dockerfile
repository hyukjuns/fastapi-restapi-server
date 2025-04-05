# 베이스이미지
FROM mysql:8.2.0

# 데이터베이스 셋업
ADD scheme.sql /docker-entrypoint-initdb.d

# MySQL 포트 명시
EXPOSE 3306