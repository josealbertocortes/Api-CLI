from fastapi import FastAPI
from pydantic import BaseModel

import datetime

import sqlite3
import jwt
class Usuario(BaseModel):
    username: str
    password: str 

app = FastAPI()

@app.post("/api/Seguridad/login")
def create_item(user: Usuario):
    username = user.username
    password = user.password
    query=f""" SELECT *  FROM USERS WHERE USERNAME = '{username}' """
    conn = sqlite3.connect('test')
    c = conn.cursor()
    c.execute(query)
    data  = c.fetchall()
    print(username)
    if len(data)==0:
        return {"estado":False,"descripcionRespuesta":"Usuario o contraseña incorrecta"}
    else:
        response_sql = data[0]
        response_password = response_sql[1]
        response_expired = response_sql[3]
        token = response_sql[2]
        if(response_password!=password):
            conn.commit()
            return {"estado":False,"descripcionRespuesta":"Usuario o contraseña incorrecta"}
        now = datetime.datetime.now()
        dt_obj = datetime.datetime.strptime(response_expired, '%Y-%m-%d %H:%M:%S')
        print(now,dt_obj)
        if now>dt_obj:
            encoded_jwt = jwt.encode({"username":username,"password":password}, "ASDECDGRSASDWFVTHFD", algorithm="HS256")
            query_update = f"""UPDATE USERS SET TOKEN = '{encoded_jwt}'  WHERE USERNAME= '{username}' """
            c.execute(query_update)
            conn.commit()
            return {"estado":True,"descripcionRespuesta":"","token":encoded_jwt}
        else:
            conn.commit()
            return  {"estado":True,"descripcionRespuesta":"","token":token}



# query = """CREATE TABLE  USER (USERNAME VARCHAR(255), PASSWORD VARCHAR(255), TOKEN VARCHAR(255), EXPERATIONACCESS TIMESTAMP)
# """
# query = f""" INSERT INTO USERS (USERNAME,PASSWORD,TOKEN,EXPERATIONACCESS)
# VALUES('Ecommerce','F4bt4s1!','BASD-DASDSDAS-DASDASDAS','2022-07-08 00:00:00'),
# ('Admin','123','BASD-DASDSDAS-DASDASDAS','2040-04-30 11:50:40')
# """