# coding: utf-8
import sys
import pymysql
import uuid
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
mysqlclient_iplist = sys.argv[1].split(",")
cdb_ip = sys.argv[2]
cdb_port = sys.argv[3]
cdb_username = sys.argv[4]
cdb_password = sys.argv[5]
cdb_dbname = sys.argv[6]
cdb_grantlist = sys.argv[7]
mysql_client_version = sys.argv[8]


class mysqlgrant(Base):
    __tablename__ = 'mysqlgrant'
    id = Column(String(40), primary_key=True)
    mysqlclient_ip = Column(String(20))
    cdb_ip = Column(String(20))
    cdb_port = Column(String(20))
    cdb_username = Column(String(20))
    cdb_password = Column(String(20))
    cdb_dbname = Column(String(20))
    cdb_grantlist = Column(String(20))
    mysql_client_version = Column(String(20))


def set_mysql_grant(
        cdb_username,
        cdb_password,
        cdb_dbname,
        cdb_grantlist,
        mysqlclient_ip,
        mysql_client_version):
    conn = pymysql.connect("localhost", "root", "")
    cursor = conn.cursor()    # 用来获得python执行mysql命令的方法，也就是我们所说的操作游标
    password_type = ("Password", "old_Password")[
        mysql_client_version == "4"]    # 判断密码是长密码还是短密码
    cursor.execute(
        "select {0}('{1}')".format(
            password_type,
            cdb_password    # 利用mysql本身方法计算密文
        )
    )
    cdb_password_cipher = cursor.fetchone()[0]  # 结果通常是列表或元组, 包含结果中的不同列的值
    sql = "grant {0} on {1}.* to {2}@{3} identified by PASSWORD '{4}';".format(
        cdb_grantlist, cdb_dbname, cdb_username, i, cdb_password_cipher)
    cursor.execute(sql)
    conn.commit()


engine = create_engine('mysql+pymysql://root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

for i in mysqlclient_iplist:
    QUERY = session.query(mysqlgrant).filter(
        mysqlgrant.mysqlclient_ip == i,
        mysqlgrant.cdb_ip == cdb_ip,
        mysqlgrant.cdb_port == cdb_port,
        mysqlgrant.cdb_username == cdb_username,
        mysqlgrant.cdb_dbname == cdb_dbname)
    if QUERY.count() > 0:
        if QUERY[0].cdb_password != cdb_password:  # 有记录并且密码不同
            print("数据库中已经有{0}的记录，并且密码和输入的不同".format(i))
        else:  # 有记录并且密码相同（叠加权限）
            cdb_grantlist_exist = QUERY[0].cdb_grantlist.split(",")
            cdb_grantlist_list = cdb_grantlist.split(",")
            cdb_grantlist_new = set(
                cdb_grantlist_exist +
                cdb_grantlist_list)   # 原有权限和新加的权限取并集
            cdb_grantlist_added = cdb_grantlist_new - \
                set(cdb_grantlist_exist)  # 新增的权限
            if cdb_grantlist_added == set():
                print("数据库中已经有{0}的记录，权限大于或等于输入的权限".format(i))
            else:
                print(
                    "数据库中已经有{0}的权限，新增加了{1}这些权限".format(i, cdb_grantlist_added))
                QUERY[0].cdb_grantlist = ','.join(list(cdb_grantlist_new))
                session.commit()
    else:
        id = str(uuid.uuid1())
        new_user = mysqlgrant(
            id=id,
            mysqlclient_ip=i,
            cdb_ip=cdb_ip,
            cdb_port=cdb_port,
            cdb_username=cdb_username,
            cdb_password=cdb_password,
            cdb_dbname=cdb_dbname,
            cdb_grantlist=cdb_grantlist,
            mysql_client_version=mysql_client_version)
        session.add(new_user)
        session.commit()
        set_mysql_grant(
            cdb_username,
            cdb_password,
            cdb_dbname,
            cdb_grantlist,
            i,
            mysql_client_version,
        )
session.close()
