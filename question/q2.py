import json

from base_client import connect
from pymysql.cursors import DictCursor

from lib.refactorJson import DateEncoder

sql = """
    select Student.SId,Sname,ss from Student,(
        select SId, AVG(score) as ss from SC  
        GROUP BY SId 
        HAVING AVG(score)> 60
        ) as r
    where Student.sid = r.sid;
"""


if __name__ == '__main__':

    with connect.cursor(DictCursor) as cursor:
        print("------------------")
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        print(json.dumps(fetchall, indent=4, cls=DateEncoder, ensure_ascii=False))
