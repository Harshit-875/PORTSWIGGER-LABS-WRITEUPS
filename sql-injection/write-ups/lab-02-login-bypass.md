# Lab: SQL Injection in WHERE Clause – Hidden Data Retrieval

## Platform
PortSwigger Web Security Academy

## Difficulty
Apprentice

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
User-supplied input from the login form is directly concatenated into the SQL query 
without proper validation
---

## Exploitation Steps
1. Click on My Account
2. Injected a crafted SQL condition (administrator'OR 1=1)
3. Enter a random password
4. You will be now logged in as an administrator

---

## Why This Works
The injected SQL modifies the WHERE clause logic, causing the database
to logged in the user as an administrator.

---

## Impact
- Exposure of the data as an administrator
- Unauthorized access to data
- 
---

## Mitigation
- Use prepared statements (parameterized queries)
- Validate and sanitize user input
- Apply least-privilege access to database users

---

## Tools Used
- Burp Suite
- Browser Developer Tools

---

## Key Learning
This lab demonstrates how improper handling of user input in SQL queries
can lead to data exposure and logic bypass vulnerabilities.
