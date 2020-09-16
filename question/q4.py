import json

from base_client import connect
from pymysql.cursors import DictCursor

from lib.refactorJson import DateEncoder

sql = """
select Student.sid, Student.sname,r.coursenumber,r.scoresum from Student,
    (select SC.Sid, sum(SC.score) as scoresum, count(SC.Cid) as coursenumber from SC 
group by SC.Sid)r
where Student.Sid = r.Sid
"""

if __name__ == '__main__':
    with connect.cursor(DictCursor) as cursor:
        print("------------------")
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
