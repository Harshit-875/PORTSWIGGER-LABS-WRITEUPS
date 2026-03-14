# Lab: Reflected XSS into HTML context with nothing encoded

## Platform
PortSwigger Web Security Academy

## Difficulty
Apprentice

---

## Root Cause
User-supplied input from the search box get directly embedded into the javascript inside
the h1 tag

---

## Exploitation Steps
1. Enter 'Hello' inside the search box
2. You will see the result like 0 search results for 'hello' 
3. Now enter <script>alert(1)</script>
4. Now you will see an alert which means your javascript get executed and alert box pops up

---