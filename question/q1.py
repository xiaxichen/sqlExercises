from base_client import connect
from pymysql.cursors import DictCursor
sql = """
select * from Student RIGHT JOIN (
    select t1.SId, class1, class2 from
          (select SId, score as class1 from SC where SC.CId = '01')as t1, 
          (select SId, score as class2 from SC where SC.CId = '02')as t2
    where t1.SId = t2.SId AND t1.class1 > t2.class2
) as r 
on Student.SId = r.SId;
"""
with connect.cursor(DictCursor) as cursor:
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    print(fetchall)
