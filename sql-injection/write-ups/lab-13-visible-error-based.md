# Lab: SQL Injection in visible-error-based 

## Platform
PortSwigger Web Security Academy

## Difficulty
Practitioner

## Lab Objective
Exploit a Blind SQL injection vulnerability in the login function 
and to login as a administrator

---

## Vulnerability Type
SQL Injection  

---

## Vulnerable Functionality
Tracking id cookie

The application uses the following SQL query:

SELECT * FROM tracking WHERE id = 'xxxxxx'

---

## Root Cause
The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.
---

## Exploitation Steps
1. Click on any product category
2. And then send that request to Repeater in Burp-Suite
3. Concatenate your Sql query in Tracking id (trackingid:xyz' AND CAST(Select password from users where username='administrator') AS int) --
4. But here the problem is you will not get a complete error means some part of your query will get cut out because it has some character restriction.
5. So now you will modify your query (using limit) into something like this : (trackingid:' AND CAST(Select password from users LIMIT 1) AS int) --
6. What Limit will do is it will give you the first entry in that table and if you are lucky enough you will get your administrator password , that you can check by changing the query and replace password to username 
7. Now you will get your password, you can also use offset with limit to get the specific entry from table.
8. Now logged in as administrator
---

## Why This Works
Application uses a sql query for tracking id analytics and we can give input and see what error message it is showing , fortunately for us it is showing verbose error and in that error shows the query running behind it

---

## Impact
- Exposure of the data as an administrator
- Unauthorized access to data
---

## Mitigation
- Use prepared statements (parameterized queries)
- Disable verbose database error messages
- Never use cookies values directly in SQL queries
- Apply least privilege access
- Validate and sanitize all user-controlled input, including cookies.

---

## Tools Used
- Burp Suite (Repeater)
- Browser Developer Tools

---

## Key Learning
- Verbose SQL error messages can leak sensitive data directly.
- Blind SQL injection can become visible error-based SQL injection due to misconfiguration.
- Cookies (like TrackingId) are also user-controlled input and must be treated as untrusted.
- Functions like CAST() can be abused to force data disclosure via errors.
- Proper error handling and prepared statements are critical to prevent SQL injection.
