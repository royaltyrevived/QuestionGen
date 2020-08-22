import sqlite3


conn = sqlite3.connect('db1.db')
c = conn.cursor()

def errorcorr(user_time,constraint_time):
    if constraint_time != user_time:
        if constraint_time>user_time:
            c.execute("UPDATE complexity FROM db WHERE constraint_time=? ",(constraint_time,))
        if constraint_time<user_time:
            c.execute("UPDATE complexity FROM db WHERE constraint_time=? ", (constraint_time,))

    else:
        print("none")
    return None


#FROM webpage user_time should be returned

def user_time_update(init_time,count,id):
    if count>1:
        init_time + = (init_time)/count
        c.execute("UPDATE user_time FROM db WHERE id=?",(id))

    return None

def app:
    #question ko id as it appeared on the webpage and count return
    user_time_update(init_time,count,id)
    if count>100:
        errorcorr(user_time,constraint_time)
