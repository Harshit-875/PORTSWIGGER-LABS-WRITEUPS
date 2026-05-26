# Username Enumeration via Response Timing

## Objective
Enumerate a valid username using response timing, brute-force the password, and access the victim account.

---

## Tools Used
- Burp Suite Community Edition
- Burp Intruder
- Burp Repeater

---

## Step 1 - Identify Rate Limiting

Send invalid login attempts and observe that after multiple failures the application responds with:

```text
Please try again in 30 minutes
```

This indicates IP-based brute-force protection.

---

## Step 2 - Bypass Rate Limiting

Add the following header to spoof the IP address:

```http
X-Forwarded-For: 1
```

Change the value on every request to bypass the rate limit.

Example:

```http
X-Forwarded-For: 1
X-Forwarded-For: 2
X-Forwarded-For: 3
```

---

## Step 3 - Identify Timing Difference

Send login requests using:
- Invalid usernames
- Valid usernames

Use a very long password:

```text
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Notice:
- Invalid usernames respond quickly.
- Valid usernames take slightly longer.

This happens because the server performs password verification only for valid usernames.

---

## Step 4 - Username Enumeration

Send the request to Intruder.

Select:
- Attack Type → `Pitchfork`

Add payload positions:

```http
X-Forwarded-For: §1§
username=§user§
password=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

---

## Step 5 - Configure Payloads

### Payload 1
- Type → Numbers
- Range → 1 to 100

Used to spoof IP addresses.

### Payload 2
- Candidate usernames list

Start the attack.

---

## Step 6 - Analyze Response Timing

Enable these columns:
- Response received
- Response completed

One username consistently shows a longer response time.

This indicates a valid username.

---

## Step 7 - Brute Force Password

Create another Intruder attack.

Use:

```http
X-Forwarded-For: §1§
username=valid-user
password=§pass§
```

### Payload 1
- Numbers (1–100)

### Payload 2
- Candidate passwords list

Start the attack.

---

## Step 8 - Identify Correct Password

Most responses return:

```http
200 OK
```

One response returns:

```http
302 Found
```

This indicates successful authentication.

---

## Step 9 - Login

Use the discovered credentials to log in and access the account page.

Lab solved successfully.

---

## Vulnerability

The application leaks information through response timing differences.

Even when:
- error messages are identical
- status codes are identical

valid usernames can still be identified through backend processing delays.

---

## Prevention

- Use constant-time authentication logic.
- Implement proper rate limiting.
- Avoid trusting `X-Forwarded-For` headers directly.
- Use MFA and monitoring.

---

## Key Learning

Timing differences can create side-channel information leaks that allow username enumeration.

---

## Tags

`#PortSwigger` `#BurpSuite` `#Authentication` `#TimingAttack` `#UsernameEnumeration` `#BruteForce`