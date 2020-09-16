import json

from base_client import connect
from pymysql.cursors import DictCursor

from lib.refactorJson import DateEncoder

sql = """
    select * from 
        (select SId from SC group by SId) as t1
    left join
        (select * from Student) as t2
    on t1.SId = t2.SId

"""
sql1 = """
    select DISTINCT Student.*
    from Student,SC
    where Student.SId=SC.SId
"""
if __name__ == '__main__':
    with connect.cursor(DictCursor) as cursor:
        print("------------------")
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
        print("------------------")
        cursor.execute(sql1)
        fetchall = cursor.fetchall()
        print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
