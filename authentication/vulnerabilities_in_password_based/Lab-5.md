# Username Enumeration via Account Lock - Writeup

## Lab Information

* **Lab Name:** Username Enumeration via Account Lock
* **Difficulty:** Practitioner
* **Platform:** PortSwigger Web Security Academy
* **Category:** Authentication Vulnerabilities

---

# Objective

The goal of this lab is to:

1. Enumerate a valid username using the account lock mechanism.
2. Brute-force the password for the valid user.
3. Log into the account successfully to solve the lab.

---

# Vulnerability Explanation

The application implements an account lock mechanism after multiple failed login attempts.

However, the behavior differs for:

* Invalid usernames
* Valid usernames

If a valid username is used repeatedly with incorrect passwords, the application eventually responds with:

```text
You have made too many incorrect login attempts
```

This allows attackers to identify valid usernames.

---

# Tools Used

* Burp Suite Community/Professional
* Burp Intruder

---

# Step 1 - Intercept Login Request

1. Open the lab.
2. Attempt login using random credentials.
3. Intercept the request in Burp Suite.

Example request:

```http
POST /login HTTP/2
Host: example.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

username=test&password=test
```

4. Send the request to **Intruder**.

---

# Step 2 - Configure Cluster Bomb Attack

## Attack Type

Select:

```text
Cluster Bomb
```

## Payload Positions

Configure payload positions like this:

```text
username=§invalid-user§&password=test§§
```

### Explanation

* First payload → usernames list
* Second payload → null payload repeated 5 times

This repeats each username 5 times to trigger account locking.

---

# Step 3 - Configure Payloads

## Payload Set 1

Add the candidate usernames list provided by the lab.

Example:

```text
carlos
wiener
administrator
peter
martin
```

## Payload Set 2

Choose:

```text
Payload Type: Null Payloads
```

Set:

```text
Generate: 5 payloads
```

---

# Step 4 - Start Attack and Identify Valid Username

Start the Intruder attack.

Observe:

* Response length
* Error messages

Most usernames return:

```text
Invalid username or password
```

But one username returns:

```text
You have made too many incorrect login attempts
```

This indicates a **valid username**.

Example:

```text
Valid Username: carlos
```

---

# Step 5 - Password Brute Force

Send another login request to Intruder.

## Attack Type

```text
Sniper
```

## Payload Position

Set payload only on the password parameter:

```text
username=carlos&password=§test§
```

---

# Step 6 - Configure Password List

Load the candidate password list provided by the lab.

Example:

```text
123456
password
qwerty
letmein
football
```

---

# Step 7 - Add Grep Extract Rule

Go to:

```text
Intruder → Settings → Grep Extract
```

Extract the error message text.

Possible responses:

* Invalid username or password
* Account locked
* No error message

---

# Step 8 - Identify Correct Password

Start the attack.

Observe the response where:

* No error message appears
* Response length differs

This indicates the correct password.

Example:

```text
Password: football
```

---

# Step 9 - Wait for Lock Reset

The account becomes temporarily locked after multiple attempts.

Wait approximately:

```text
1 minute
```

for the lock to reset.

---

# Step 10 - Login Successfully

Use the discovered credentials:

```text
Username: carlos
Password: football
```

Login successfully and access the account page to solve the lab.

---

# Root Cause

The application reveals different responses for:

* Invalid usernames
* Valid usernames with too many failed attempts

This leaks information about account existence.

---

# Impact

An attacker can:

* Enumerate valid usernames
* Perform targeted password attacks
* Increase success rate of credential stuffing attacks

---

# Mitigation

## Recommended Fixes

1. Use generic error messages for all login failures.

Example:

```text
Invalid username or password
```

2. Apply account lock policies consistently.
3. Implement rate limiting.
4. Add CAPTCHA after multiple attempts.
5. Use MFA (Multi-Factor Authentication).

---

# Key Learning

This lab demonstrates how subtle differences in authentication responses can lead to username enumeration vulnerabilities.

Even security mechanisms like account locking can become dangerous if implemented incorrectly.

---
