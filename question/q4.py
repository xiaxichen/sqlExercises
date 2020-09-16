import json

from base_client import connect
from pymysql.cursors import DictCursor

from lib.refactorJson import DateEncoder

sql = """
/*联合查询不会显示没选课的学生*/
select Student.sid, Student.sname,r.coursenumber,r.scoresum from Student,
    (select SC.Sid, sum(SC.score) as scoresum, count(SC.Cid) as coursenumber from SC 
group by SC.Sid)r
where Student.Sid = r.Sid
"""

sql1 = """
select s.SId, s.sname,r.coursenumber,r.scoresum
from (
    (select Student.SId,Student.sname 
    from Student
    )s 
    left join 
    (select 
        SC.sid, sum(SC.score) as scoresum, count(SC.CId) as coursenumber
        from SC 
        group by SC.SId
    )r 
   on s.Sid = r.Sid
);
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
