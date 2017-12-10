import MySQLdb

def antisql(content):
    
    antistr=u"'|and|exec|insert|select|delete|update|count|*|%|chr|mid|master|truncate|char|declare|;|or|-|+|,".split(u"|")
    
    for i in range (len(antistr)):
        if antistr[i] in content:
            return 1
    return 0    
    


def sql_select(text):
    conn=MySQLdb.connect(host='47.93.246.204',user="mint",passwd="INSCHINAisdead1",db="dimcreator",port=3306,charset='utf8')
    cur = conn.cursor()
    cur.execute(text)
    res=cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return res


def sql_write(text):
    conn=MySQLdb.connect(host='47.93.246.204',user="mint",passwd="INSCHINAisdead1",db="dimcreator",port=3306,charset='utf8')
    cur = conn.cursor()
    cur.execute(text)
    
    cur.close()
    conn.commit()
    conn.close()





