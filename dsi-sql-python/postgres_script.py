import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia', host='/tmp')
c = conn.cursor()

today = '2013-08-29' #'2014-08-22' #was '201-08-17'

# This is not strictly necessary but demonstrates how you can convert a date
# to another format
ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

c.execute('''DROP TABLE logins_7d; ''')

c.execute(
    '''CREATE TABLE logins_7d AS
    SELECT userid, COUNT(*) AS cnt, timestamp %(ts)s AS date_7d
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days'
    GROUP BY userid;''', {'ts': ts}
)

conn.commit()
conn.close()
