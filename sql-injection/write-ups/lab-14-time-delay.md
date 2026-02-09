# Lab: Blind SQL Injection with Time Delays

## Platform
PortSwigger Web Security Academy

## Difficulty
Practitioner

## Lab Objective
Exploit a **blind SQL injection vulnerability** in the tracking cookie to trigger a **10-second time delay**, proving successful SQL injection even when no output or errors are visible.

---

## Vulnerability Type
Blind SQL Injection (Time-Based)

---

## Vulnerable Functionality
TrackingId cookie used for analytics

The application uses a SQL query similar to:

SELECT * FROM tracking WHERE id = 'TrackingId'

The query result is not reflected in the response.

---

## Root Cause
The application:
- Directly inserts the **TrackingId cookie value** into a SQL query
- Does **not display query results**
- Does **not show database errors**
- Executes SQL queries **synchronously**

Because of synchronous execution, **time delays** in the database cause delayed HTTP responses.

---

## Exploitation Steps

1. Open the lab and visit the home page of the shop.
2. Intercept the request using **Burp Suite**.
3. Locate the request containing the `TrackingId` cookie.
4. Send the request to **Repeater**.
5. Modify the `TrackingId` value to the following payload: TrackingId=x'||pg_sleep(10)--

6. Send the request.
7. Observe that the application response is delayed by **10 seconds**.

---

## Payload Explanation

- `||` → String concatenation operator in PostgreSQL
- `pg_sleep(10)` → Pauses database execution for 10 seconds
- `--` → Comments out the rest of the SQL query

This payload forces the database to sleep, delaying the HTTP response.

---

## Why This Works
- The SQL query runs synchronously.
- The injected `pg_sleep(10)` function executes inside the query.
- The application waits for the database to finish execution.
- A delayed response confirms successful SQL injection.

Even though:
- No errors are shown
- No output is reflected

The **response time** becomes the attacker’s information channel.

---

## Impact
- Confirms the presence of a blind SQL injection vulnerability
- Can be extended to:
- Extract sensitive data character by character
- Enumerate users
- Dump credentials using time-based logic

---

## Mitigation
- Use prepared statements (parameterized queries)
- Never use cookie values directly in SQL queries
- Apply strict input validation and sanitization
- Use least-privilege database accounts
- Implement proper query timeout limits

---

## Tools Used
- Burp Suite (Proxy & Repeater)
- Web Browser

---

## Key Learning
- Blind SQL injection does not require visible output.
- Time delays can be used as a TRUE/FALSE condition.
- Cookies are user-controlled input and must not be trusted.
- PostgreSQL uses `||` for string concatenation, not logical OR.
- Time-based SQL injection is extremely powerful when error handling is secure.


