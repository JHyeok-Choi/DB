# Oracle

## 계정생성

CREATE USER c##test IDENTIFIED BY test;

or

#### Oracle 12C
ALTER SESSION SET "_ORACLE_SCRIPT"=true;
CREATE USER test IDENTIFED BY test;


## 권한부여

GRANT DBA TO c##test WITH ADMIN OPTION;
- 주의) 계정 이름에 c## 붙음.
