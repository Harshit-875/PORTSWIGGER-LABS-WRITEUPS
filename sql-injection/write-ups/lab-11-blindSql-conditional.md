# Lab: SQL Injection in WHERE Clause – Hidden Data Retrieval

## Platform
PortSwigger Web Security Academy

## Difficulty
Practitioner

## Lab Objective
Exploit a SQL injection vulnerability in the login function 
and to login as a administrator

---

## Vulnerability Type
SQL Injection  

---

## Vulnerable Functionality
Product category filter

The application uses the following SQL query:

SELECT * FROM users WHERE username = 'xxxxxx' AND password='xxxxxx'

---

## Root Cause
The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.
---

## Exploitation Steps
1. Click on any product category
2. And then send that request to Repeater in Burp-Suite
3. Concatenate your Sql query in Tracking id (trackingid:xyz' AND+LENGTH((SELECT+password+FROM+users+WHERE+username%3d'administrator'))%3d{i}--)
4. Change the value of i starting from 1 if Welcome back message appears in response then that i will be correct and you have now got the length of administrator password
5. Next for finding the password you have to change the sql query and have to use substring method to bruteforce the password (+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username%3d'administrator'),{i},1)='{char}'--) , Here put the value of i that you found in step 4 and change the value of char
6. You can refer to the automation script for this lab in automation folder i.e lab11.py
7. Now logged in as administrator by entering the username and password.
8. This method is if you use Burp Suite otherwise you can use browser dev tool also but it will take longer time.

---

## Why This Works
Application uses a sql query for tracking id analytics and using the and operator , substring method we can bruteforce the password.

---

## Impact
- Exposure of the data as an administrator
- Unauthorized access to data
---

## Mitigation
- Use prepared statements (parameterized queries)
- Validate Tracking id format
- Apply least-privilege access to database users
- Use application level logic for validation first

---

## Tools Used
- Burp Suite
- Browser Developer Tools

---

## Key Learning
This lab demonstrates how improper handling of tracking id in SQL queries
can lead to data exposure and logic bypass vulnerabilities.
