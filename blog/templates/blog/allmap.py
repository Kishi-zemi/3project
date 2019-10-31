import sqlite3
import pandas.io.sql as psql
import Mark as m


def main():
    print("start")
    dbname = 'h28_30.db'

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    df1 = psql.read_sql("SELECT * FROM sample WHERE 発生年 = 2016 AND 甲_年齢 IN ('65～74歳', '75歳以上')", conn)
    print("df1 finished")
    m1 = m.MarkClass(df1,'blue','2016')
    m1.marker()

    df2 = psql.read_sql("SELECT * FROM sample WHERE 発生年 = 2017 AND 甲_年齢 IN ('65～74歳', '75歳以上')", conn)
    m2 = m.MarkClass(df2,'red','2017')
    m2.marker()

    df3 = psql.read_sql("SELECT * FROM sample WHERE 発生年 = 2018 AND 甲_年齢 IN ('65～74歳', '75歳以上')", conn)
    m3 = m.MarkClass(df3,'green','2018')
    m3.marker()

    df4 = psql.read_sql("SELECT * FROM sample WHERE 甲_年齢 IN ('65～74歳', '75歳以上')", conn)
    m4 = m.MarkClass(df4,'','all')
    m4.marker()

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
