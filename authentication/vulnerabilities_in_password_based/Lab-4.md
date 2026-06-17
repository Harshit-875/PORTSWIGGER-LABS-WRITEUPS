# Broken Brute-Force Protection, IP Block Bypass

## Objective

Bypass the application's brute-force protection mechanism and brute-force Carlos's password by alternating successful logins with failed attempts.

---

## Tools Used

- Burp Suite Community Edition
- Burp Intruder

---

## Step 1 - Observe Brute-Force Protection

Navigate to the login page and attempt multiple invalid login attempts.

After several failed attempts, the application temporarily blocks further login attempts.

Example response:

```text
Invalid username or password
```

After multiple failed attempts:

```text
You have made too many incorrect login attempts. Please try again later.
```

This indicates the presence of brute-force protection based on failed login counters.

---

## Step 2 - Understand the Flaw

Testing reveals:

- Failed login attempts increase the lockout counter.
- Successful logins reset the failed login counter.

This means the protection can be bypassed by periodically performing a valid login while brute-forcing another account.

Valid credentials provided by the lab:

```text
Username: wiener
Password: peter
```

---

## Step 3 - Capture Login Request

Enter invalid credentials such as:

```text
test:test
```

Capture the `POST /login` request using Burp Proxy.

Send the request to Burp Intruder.

---

## Step 4 - Configure Intruder Attack

Select:

```text
Attack Type → Pitchfork
```

Clear unnecessary payload positions and keep only:
- username
- password

Example request:

```http
POST /login HTTP/1.1
Host: target.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

username=§user§&password=§pass§
```

---

## Step 5 - Configure Resource Pool

Open:

```text
Resource Pool
```

Create a custom resource pool with:

```text
Maximum concurrent requests = 1
```

Important:
- Select the custom resource pool before starting the attack.
- Requests must be sent sequentially.

This ensures login attempts occur in the correct order.

---

## Step 6 - Create Username Payload List

Use the following repeating pattern:

```text
wiener
carlos
carlos
```

Repeat this pattern throughout the payload list.

Reason:
- `wiener:peter` performs a successful login.
- Successful logins reset the brute-force counter.
- This prevents Carlos's account from becoming locked.

Example:

```text
wiener
carlos
carlos
wiener
carlos
carlos
wiener
carlos
carlos
```

---

## Step 7 - Create Password Payload List

Align the password payloads with the username payloads.

Example:

```text
peter
123456
password
peter
12345678
qwerty
```

Alignment:

| Username | Password |
|---|---|
| wiener | peter |
| carlos | 123456 |
| carlos | password |
| wiener | peter |
| carlos | 12345678 |
| carlos | qwerty |

Continue this pattern throughout the entire password list.

---

## Step 8 - Start Attack

Start the Intruder attack.

Requests are now sent sequentially:

```text
wiener:peter  → successful login
carlos:guess1 → failed login
carlos:guess2 → failed login
wiener:peter  → resets counter
```

This bypasses the brute-force protection.

---

## Step 9 - Analyze Responses

After the attack completes:

1. Filter out:
   ```text
   200 OK
   ```

2. Look for:
   ```http
   302 Found
   ```

Most `302` responses correspond to:

```text
wiener : peter
```

Ignore these.

Find the single `302` response associated with:

```text
carlos
```

The corresponding password is Carlos's valid password.

---

## Step 10 - Login as Carlos

Use the discovered credentials to log in as Carlos.

Navigate to Carlos's account page.

The lab is now solved successfully.

---

# Vulnerability

The brute-force protection implementation is flawed because:
- Successful logins reset failed-attempt counters globally.
- Failed login tracking is not isolated properly.
- Authentication rate limiting can be bypassed through valid logins.

This allows attackers to continue brute-force attempts indefinitely.

---

# Impact

An attacker can:
- Bypass brute-force protection
- Enumerate passwords
- Gain unauthorized account access
- Compromise user accounts

---

# Prevention

- Track failed login attempts per account and IP separately.
- Do not reset brute-force counters globally after successful logins.
- Implement exponential backoff and CAPTCHA.
- Use MFA (Multi-Factor Authentication).
- Detect automated login patterns.
- Lock accounts securely after repeated failures.

---

# Key Learning

Brute-force protections can often be bypassed if authentication logic improperly resets failed-attempt counters.

Understanding authentication workflow behavior is critical during penetration testing.

---

# Tags

`#PortSwigger` `#BurpSuite` `#Authentication` `#BruteForce` `#BrokenAuthentication` `#Intruder`