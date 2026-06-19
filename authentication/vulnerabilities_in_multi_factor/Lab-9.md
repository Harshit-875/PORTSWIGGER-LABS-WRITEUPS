# 2FA Bypass Using a Brute-Force Attack

## Objective

Exploit weak two-factor authentication protection by brute-forcing the 4-digit MFA code and accessing Carlos's account.

---

## Credentials

```text
Victim Account:
carlos:montoya
```

---

## Difficulty

```text
EXPERT
```

---

## Tools Used

* Burp Suite Community Edition
* Burp Intruder
* Burp Session Handling Rules
* Burp Macros

---

# Step 1 - Investigate Authentication Flow

Login using the victim credentials:

```text
Username: carlos
Password: montoya
```

After login, the application prompts for a 4-digit security code.

Enter an incorrect code twice and observe that the application logs the user out automatically.

This indicates:

* The session is invalidated after failed MFA attempts.
* A fresh login is required before continuing brute-force attempts.

---

# Step 2 - Configure Session Handling Rule

Open Burp settings:

```text
Settings → Sessions
```

Under:

```text
Session Handling Rules
```

Click:

```text
Add
```

---

# Step 3 - Configure Rule Scope

Go to:

```text
Scope Tab
```

Under:

```text
URL Scope
```

Select:

```text
Include all URLs
```

---

# Step 4 - Add Macro Action

Return to:

```text
Details Tab
```

Under:

```text
Rule Actions
```

Click:

```text
Add → Run a macro
```

---

# Step 5 - Record Authentication Macro

Click:

```text
Add
```

to open the Macro Recorder.

Select the following requests:

```text
GET /login
POST /login
GET /login2
```

Click:

```text
OK
```

---

# Step 6 - Test Macro

The Macro Editor opens.

Click:

```text
Test macro
```

Verify that the final response contains:

```text
Enter the 4-digit security code
```

This confirms:

* Login succeeded
* Session is valid
* MFA page loaded correctly

Click OK until you return to the main Burp window.

---

# Step 7 - Send MFA Request to Intruder

Locate the request:

```http
POST /login2
```

Send it to Intruder.

---

# Step 8 - Configure Payload Position

In Intruder:

```text
Intruder → Positions
```

Clear all payload markers.

Add payload markers only to:

```http
mfa-code=§0000§
```

---

# Step 9 - Configure Payload Type

Go to:

```text
Payloads
```

Select:

```text
Payload Type → Numbers
```

Configure:

```text
From: 0000
To: 9999
Step: 1
Min integer digits: 4
Max fraction digits: 0
```

This generates all possible 4-digit MFA codes.

---

# Step 10 - Configure Resource Pool

Open:

```text
Resource Pool
```

Create a new resource pool with:

```text
Maximum concurrent requests = 1
```

This is important because:

* MFA sessions are stateful
* Multiple concurrent requests can invalidate sessions
* Sequential requests improve reliability

Assign the Intruder attack to this resource pool.

---

# Step 11 - Start Brute Force Attack

Start the Intruder attack.

Burp now automatically performs:

```text
1. Login
2. Load MFA page
3. Submit OTP guess
4. Repeat
```

for every payload.

---

# Step 12 - Identify Successful Response

Most responses return:

```text
200 OK
```

Eventually, one request returns:

```text
302 Found
```

This indicates successful authentication.

---

# Step 13 - Access Account

Right-click the successful request and select:

```text
Show response in browser
```

Copy the generated URL and open it in the browser.

Navigate to:

```text
/my-account
```

Carlos's account page loads successfully.

Lab solved.

---

# Vulnerability

The application attempts to prevent brute-force attacks by logging the user out after multiple failed MFA attempts.

However, this protection is ineffective because attackers can automate the login process using Burp macros and continue brute-forcing indefinitely.

---

# Root Cause

The application:

* Does not implement effective rate limiting
* Allows unlimited login attempts
* Relies only on session invalidation for protection

Attackers can automate:

* Session renewal
* Re-authentication
* OTP guessing

making the defense ineffective.

---

# Prevention

* Implement IP-based rate limiting
* Add progressive delays after failed MFA attempts
* Use CAPTCHA after repeated failures
* Detect automated login behavior
* Lock accounts temporarily after excessive failures
* Use device fingerprinting and anomaly detection

---

# Key Learning

Logging users out after failed OTP attempts is not sufficient brute-force protection if attackers can automate re-authentication.

Authentication workflows must be protected against automation attacks, not just individual requests.

---

# Tags

`#PortSwigger` `#Authentication` `#2FA` `#BruteForce` `#BurpSuite` `#Macros` `#SessionHandling`
