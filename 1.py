import vk
import sqlite3
import time
import json
session = vk.Session()
vk_api = vk.API(session)


def createDB():
    DB = sqlite3.connect('test.db')
    DB.execute('''CREATE TABLE TASK
                (NAME         TEXT    NOT NULL,
                SNAME           TEXT     NOT NULL,
                TIME           INT    NOT NULL,
                ID          TEXT    NOT NULL);''')

    DB.close()


a = True

users = []

for i in range(1000):
    users.append(i)

while a == True:

    users[0] = (vk_api.users.get(user_id=294317477, fields= 'online'))
    users[1] = (vk_api.users.get(user_id=167772346, fields='online'))
    users[2] = (vk_api.users.get(user_id=271453756, fields='online'))
    users[3] = (vk_api.users.get(user_id=332102905, fields='online'))
    users[4] = (vk_api.users.get(user_id=132804792, fields='online'))
    users[5] = (vk_api.users.get(user_id=221676396, fields='online'))
    users[6] = (vk_api.users.get(user_id=183608248, fields='online'))
    users[7] = (vk_api.users.get(user_id=253371424, fields='online'))
    users[8] = (vk_api.users.get(user_id=155275281, fields='online'))
    users[9] = (vk_api.users.get(user_id=243793532, fields='online'))
    users[10] = (vk_api.users.get(user_id=227615183, fields='online'))
    users[11] = (vk_api.users.get(user_id=202550436, fields='online'))
    users[12] = (vk_api.users.get(user_id=220996298, fields='online'))
    users[13] = (vk_api.users.get(user_id=185987139, fields='online'))
    users[14] = (vk_api.users.get(user_id=228498504, fields='online'))
    users[15] = (vk_api.users.get(user_id=322957152, fields='online'))
    users[16] = (vk_api.users.get(user_id=225827271, fields='online'))
    users[17] = (vk_api.users.get(user_id=214217051, fields='online'))
    users[18] = (vk_api.users.get(user_id=347023208, fields='online'))

    for i in range(19):
        users[i] = users[i][0]

    #for i in range(19):
    #    print(users[i]["last_name"])



    #print(c["online"])

    for i in range(19):
        print(users[i])

    time.sleep(1)