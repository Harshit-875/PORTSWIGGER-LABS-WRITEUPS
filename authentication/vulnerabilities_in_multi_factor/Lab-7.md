# 2FA Simple Bypass

## Objective

Bypass the two-factor authentication mechanism and access Carlos's account page.

---

## Credentials

```text
Attacker Account:
wiener:peter

Victim Account:
carlos:montoya
```

---

## Tools Used

* Burp Suite Community Edition
* Browser Developer Tools

---

## Step 1 - Login to Attacker Account

Login using the provided attacker credentials:

```text
Username: wiener
Password: peter
```

The application prompts for a 2FA verification code.

---

## Step 2 - Access Email Client

Click the Email client button and retrieve the verification code sent to the attacker account.

Complete the 2FA process and access the account page.

---

## Step 3 - Identify Account URL

After successful login, note the account page URL:

```text
/my-account
```

This page should normally only be accessible after completing 2FA verification.

---

## Step 4 - Logout

Logout from the attacker account.

---

## Step 5 - Login as Victim

Login using the victim credentials:

```text
Username: carlos
Password: montoya
```

The application again prompts for a 2FA verification code.

---

## Step 6 - Bypass 2FA

Without entering any verification code, manually change the URL in the browser to:

```text
/my-account
```

Press Enter.

---

## Step 7 - Access Victim Account

The application grants access to Carlos's account page without validating the second authentication step.

Lab solved successfully.

---

## Vulnerability

The application creates an authenticated session before completing the 2FA verification process.

Although the user is prompted for a verification code, the server does not properly enforce the second authentication step before allowing access to protected resources.

This allows attackers to directly access authenticated endpoints such as:

```text
/my-account
/admin
/dashboard
```

without completing 2FA.

---

## Root Cause

The application fails to verify whether:

* The user has successfully completed 2FA
* The current session is marked as fully authenticated

The server only checks whether the user passed the username and password stage.

---

## Prevention

* Mark sessions as "2FA pending" until verification is complete.
* Restrict access to authenticated endpoints before successful 2FA validation.
* Perform server-side authorization checks on every protected request.
* Invalidate incomplete authentication sessions properly.

---

## Key Learning

Two-factor authentication is only secure when access control checks properly enforce completion of the second authentication step.

If authenticated pages are accessible before OTP verification, attackers can bypass 2FA entirely.

---

## Tags

`#PortSwigger` `#Authentication` `#2FA` `#Bypass` `#WebSecurity` `#BurpSuite`
