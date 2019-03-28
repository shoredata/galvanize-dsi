import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia', host='/tmp')
c = conn.cursor()

today = '2013-08-14' #'2014-08-22' #was '201-08-17'

# This is not strictly necessary but demonstrates how you can convert a date
# to another format
ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

new_table = "logins_" + today.replace('-','_')

c.execute('''DROP TABLE IF EXISTS ''' + new_table + '''; ''')

c.execute(
    '''CREATE TABLE ''' + new_table + ''' AS
    SELECT logins.userid, registrations.tmstmp AS reg_date,
    MAX(logins.tmstmp) AS last_login, COUNT(*) AS logins_7d,
    SUM(CASE WHEN logins.type='mobile' THEN 1 ELSE 0 END) AS logins_7d_mobile,
    SUM(CASE WHEN logins.type='web' THEN 1 ELSE 0 END) AS logins_7d_web,
    CASE WHEN max(optout.userid) IS NULL THEN 'OPT_IN' ELSE 'OPT_OUT' END AS opt_out

    FROM logins
    JOIN registrations ON logins.userid = registrations.userid
    LEFT JOIN optout ON logins.userid = optout.userid
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days'
    GROUP BY logins.userid, reg_date;''', {'ts': ts}
)

conn.commit()
conn.close()


#                          Table "public.logins"
#  Column |            Type             | Collation | Nullable | Default
# --------+-----------------------------+-----------+----------+---------
#  userid | integer                     |           |          |
#  tmstmp | timestamp without time zone |           |          |
#  type   | character varying           |           |          |


#                Table "public.optout"
#  Column |  Type   | Collation | Nullable | Default
# --------+---------+-----------+----------+---------
#  userid | integer |           |          |

#                      Table "public.registrations"
#  Column |            Type             | Collation | Nullable | Default
# --------+-----------------------------+-----------+----------+---------
#  userid | integer                     |           |          |
#  tmstmp | timestamp without time zone |           |          |
#  type   | character varying           |           |          |


# socialmedia=# select * from logins;
#  userid |       tmstmp        |  type
# --------+---------------------+--------
#     579 | 2013-11-20 03:20:06 | mobile
#     823 | 2013-11-20 03:20:49 | web
#     953 | 2013-11-20 03:28:49 | web
#     612 | 2013-11-20 03:36:55 | web
#     269 | 2013-11-20 03:43:13 | web
#     799 | 2013-11-20 03:56:55 | web
#     890 | 2013-11-20 04:02:33 | mobile
#     330 | 2013-11-20 04:54:59 | mobile

# socialmedia=# select * from optout;
#  userid
# --------
#      10
#      16
#      55


# socialmedia=# select * from registrations;
#  userid |       tmstmp        |  type
# --------+---------------------+--------
#     185 | 2013-08-14 17:22:13 | web
#     950 | 2013-08-15 01:33:52 | web
#     835 | 2013-08-15 13:38:04 | mobile
#      23 | 2013-08-15 17:28:19 | mobile
#     467 | 2013-08-15 20:17:31 | web
#     714 | 2013-08-16 14:38:12 | mobile
#     977 | 2013-08-16 15:19:19 | web
