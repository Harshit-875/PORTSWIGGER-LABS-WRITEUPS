# Lab: DOM XSS in document.write sink using source location.search

## Platform
PortSwigger Web Security Academy

## Difficulty
Apprentice

---

## Root Cause
Source - Where the user inputs like search box , url search query etc
Sink - Where the input get executed or where your payload get executed

CAUSE - It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which we can control using the website URL.
---

## Exploitation Steps
1. Enter a random string inside the search box
2. Now inspect the element and you will see that your string get placed inside an src attribute in an image tag
3. Now enter ">script>alert(1)</script> and you will see an alert pops up

---