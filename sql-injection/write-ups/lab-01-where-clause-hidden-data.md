# Lab: SQL Injection in WHERE Clause – Hidden Data Retrieval

## Platform
PortSwigger Web Security Academy

## Difficulty
Apprentice

## Lab Objective
Exploit a SQL injection vulnerability in the product category filter
to retrieve unreleased (hidden) products.

---

## Vulnerability Type
SQL Injection  
OWASP A03:2021 – Injection

---

## Vulnerable Functionality
Product category filter

The application uses the following SQL query:

SELECT * FROM products WHERE category = 'Gifts' AND released = 1

---

## Root Cause
User-supplied input from the category parameter is directly concatenated
into the SQL query without proper validation or parameterization.

---

## Exploitation Steps
1. Select any product category
2. Intercept the request using Burp Suite
3. Identify the category parameter
4. Inject a crafted SQL condition ('+OR+1=1) to bypass the released = 1 check 
5. Observe that unreleased products are displayed

---

## Why This Works
The injected SQL modifies the WHERE clause logic, causing the database
to return products regardless of their released status.

---

## Impact
- Exposure of unreleased or hidden products
- Unauthorized access to internal data
- Business logic bypass

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
