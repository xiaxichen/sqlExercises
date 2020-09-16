import json

from base_client import connect
from pymysql.cursors import DictCursor

from lib.refactorJson import DateEncoder

sql = """
select * from Student RIGHT JOIN (
    select t1.SId, class1, class2 from
          (select SId, score as class1 from SC where SC.CId = '01')as t1, 
          (select SId, score as class2 from SC where SC.CId = '02')as t2
    where t1.SId = t2.SId AND t1.class1 > t2.class2
) as r 
on Student.SId = r.SId;
"""
sql1 = """
select t1.sid,t2.sid from 
    (select SC.SId from SC where SC.CId="01") as t1,
    (select SC.SId from SC where SC.CId="02") as t2 
where t1.sid = t2.sid;
"""
sql2 = """
select * from 
    (select * from SC where SC.SId = '01') as t1
left join
    (select * from SC where SC.SId = '02') as t2
on t1.SId = t2.SId;
"""
sql3 = """
select * from SC
    where SC.SId not in (
        select SId from SC
        where SC.CId = '01'
    )
and SC.CId = '02';
"""
with connect.cursor(DictCursor) as cursor:
    print("------------------")
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
    print("------------------")
    cursor.execute(sql1)
    fetchall = cursor.fetchall()
    print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
    print("------------------")
    cursor.execute(sql2)
    fetchall = cursor.fetchall()
    print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
    print("------------------")
    cursor.execute(sql3)
    fetchall = cursor.fetchall()
    print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
    print("------------------")