# Username Enumeration via Subtly Different Responses

## Objective
Enumerate a valid username, brute-force the password, and access the victim account.

---

## Tools Used
- Burp Suite Community Edition
- Burp Intruder

---

## Step 1 - Capture Login Request

Intercept the login request and send it to Intruder.

```http
POST /login
```

---

## Step 2 - Enumerate Username

Set payload position on the username parameter:

```http
username=§test§&password=test
```

Load the candidate username wordlist.

---

## Step 3 - Configure Grep Extract

Go to:

```text
Intruder → Settings → Grep - Extract
```

Extract the error message:

```text
Invalid username or password.
```

Start the attack.

---

## Step 4 - Identify Valid Username

After the attack finishes, check the extracted response column.

Most responses contain:

```text
Invalid username or password.
```

One response contains:

```text
Invalid username or password 
```

Notice the subtle difference:
- Missing period (`.`)
- Extra trailing space

This indicates a valid username.

---

## Step 5 - Brute Force Password

Use the identified username and set payload position on password:

```http
username=valid-user&password=§test§
```

Load the candidate password wordlist and start the attack.

---

## Step 6 - Identify Correct Password

Most responses return:
- `200 OK`

One response returns:
- `302 Found`

This indicates successful authentication.

Save the password.

---

## Step 7 - Login

Login using the discovered credentials and access the account page.

Lab solved successfully.

---

## Vulnerability

The application leaks information through subtle differences in error responses.

Even tiny differences such as:
- Extra spaces
- Missing punctuation
- Different response lengths

can allow attackers to enumerate valid usernames.

---

## Prevention

- Use completely identical error messages.
- Normalize all authentication responses.
- Implement rate limiting and MFA.
- Monitor brute-force attempts.

---

## Key Learning

Small inconsistencies in server responses can lead to username enumeration vulnerabilities.

---

## Tags

`#PortSwigger` `#BurpSuite` `#Authentication` `#UsernameEnumeration` `#BruteForce`