# Username Enumeration via Different Responses

## Objective
Enumerate a valid username, brute-force the password, and access the victim account.

---

## Tools Used
- Burp Suite Community Edition
- Burp Intruder

---

## Step 1 - Capture Login Request

Intercept the login request in Burp Suite and send it to Intruder.

```http
POST /login
```

---

## Step 2 - Enumerate Username

Set payload position on the username parameter:

```http
username=§test§&password=test
```

Use the candidate username wordlist and start the attack.

### Observation
- Most responses → `Invalid username`
- One response → `Incorrect password`

The different response indicates a valid username.

---

## Step 3 - Brute Force Password

Fix the valid username and set payload on password:

```http
username=valid-user&password=§test§
```

Use the candidate password wordlist and start the attack.

### Observation
Most responses return:
- `200 OK`

One response returns:
- `302 Found`

This indicates successful login.

---

## Step 4 - Login

Use the discovered credentials to log in and access the account page.

Lab solved successfully.

---

## Vulnerability

The application reveals different error messages for:
- Invalid username
- Incorrect password

This allows attackers to enumerate valid usernames before brute-forcing passwords.

---

## Prevention

- Use generic error messages.
- Implement rate limiting.
- Enable account lockout.
- Use Multi-Factor Authentication (MFA).

---

## Key Learning

Different authentication responses can leak sensitive information and help attackers identify valid usernames.

---

## Tags

`#PortSwigger` `#BurpSuite` `#Authentication` `#BruteForce` `#UsernameEnumeration`