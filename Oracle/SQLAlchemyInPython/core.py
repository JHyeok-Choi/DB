# !pip install sqlalchemy oracledb

from sqlalchemy import create_engine, inspect

# 1. 접속 정보 설정
username = "C##test"
password = "test"
host = "localhost"
port = 1521
service_name = "XE"
table = "test_table"

# 2. 연결 문자열 생성 (Thin 모드)
# 형식: oracle+oracledb://user:password@host:port/?service_name=service
db_url = f"oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}"

# 3. 엔진 생성 및 연결
engine = create_engine(db_url)

# 4. 연결 확인 (예: 간단한 쿼리 실행)
try:
    inspector = inspect(engine)
    columns = inspector.get_columns(table)

    print("=" * 20) # 4-1. INSERT 문
    print(f"INSERT INTO {table} (")
    for no, column in enumerate(columns):
        if no == 0:
            print(f"\t{column['name']}")
        else:
            print(f",\t{column['name']}")
    print(") VALUES (")
    for no, column in enumerate(columns):
        if no == 0:
            print(f"\t:{column['name']}")
        else:
            print(f",\t:{column['name']}")
    print(")")
    for no, column in enumerate(columns):
        if no == 0:
            print("[{" + f"\'{column['name']}\': \'\'", end="")
        else:
            print(f", \'{column['name']}\': \'\'", end="")
    print("}]")
    print("=" * 20) # 4-2. SELECT 문
    for no, column in enumerate(columns):
        if no == 0:
            print(f"SELECT  {column['name']}")
        else:
            print(f",\t{column['name']}")
    print(f"FROM\t{table}")
    print("=" * 20) # 4-3. UPDATE 문
    for no, column in enumerate(columns):
        if no == 0:
            print(f"UPDATE {table}\nSET\t{column['name']} = \'\'")
        else:
            print(f",\t{column['name']} = \'\'")
    print("WHERE\ttest = \'\'")
    print("=" * 20) # 4-4. DELETE 문
    print(f"DELETE FROM {table}")
    print("WHERE\ttest = \'\'")
    print("=" * 20)
except Exception as e:
    print(f"Error: {e}")
finally:
    engine.dispose()



""" 예시)

====================
INSERT INTO test_table (
        no
,       name
) VALUES (
        :no
,       :name
)
[{'no': '', 'name': ''}]
====================
SELECT  no
,       name
FROM    test_table
====================
UPDATE test_table
SET     no = ''
,       name = ''
WHERE   test = ''
====================
DELETE FROM test_table
WHERE   test = ''
====================

"""
