# Lab: Stored XSS into HTML context with nothing encoded

## Platform
PortSwigger Web Security Academy

## Difficulty
Apprentice

---

## Root Cause
Comment is stored in a database which does not handle user input properly and not sanitise the input 
and when user post javascript code in the comment it is directly put inside the paragraph tag , then any user who will open the comment section of the website
the javascript will get executed in their browser leading to an XSS attack.

---

## Exploitation Steps
1. Post <script>alert(1)</script> in the comment section
2. Now you will see an alert which means your javascript get executed and alert box pops up

---