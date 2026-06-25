# PostgreSQL

## PostgreSQL 접속

sudo -i -u postgres psql


## 관리자 비밀번호 변경

\password postgres  
 (사용할 비밀번호를 두 번 입력)


## 사용자, DB 생성

- 사용자(User) 생성  
CREATE USER 나의계정명 WITH PASSWORD '비밀번호';

- 데이터베이스(Database) 생성  
CREATE DATABASE 나의DB명 OWNER 나의계정명;


## 종료

\q
