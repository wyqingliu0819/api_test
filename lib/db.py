import pymysql

from conf import config


def get_conn():
    conn = pymysql.connect(host = config.db_host,
                           port = config.db_port,
                           user = config.db_user,
                           passwd = config.db_passwd,
                           db = config.db_db,
                           charset=config.db_charset)
    return conn

def db_query(sql):
    config.logging.debug(sql)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    r = cur.fetchall()
    config.logging.debug(r)
    cur.close()
    conn.close()
    return r

def db_change(sql):
    config.logging.debug(sql)
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        config.logging.error(repr(e))
        print(repr(e))
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# r = db_query(str1)
# print(r)
# db_query(str3)
# r1 = db_query(str1)
# print(r1)

#查询用户是否存在
def check_user(name):
    r = db_query("select * from `user` where `name`='%s'" %name)
    if r:
        return True
    return False

def del_user(name):
    db_change("delete from `user` where `name`='%s'" %name)


if __name__ == '__main__':
    print(check_user("张三"))
