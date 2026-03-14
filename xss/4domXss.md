# Lab: DOM XSS in document.write sink using source location.search inside a select element

## Platform
PortSwigger Web Security Academy

## Difficulty
Practitioner

---

## Root Cause
This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which we can control using the website URL. The data is enclosed within a select element.
---

## Exploitation Steps
1. On the product pages, notice that the dangerous JavaScript extracts a storeId parameter from the location.search source. It then uses document.write to create a new option in the select element for the stock checker functionality.
2. You will see that in the javascript -> var store = (new URLSearchParams(window.location.search)).get('storeId');
It means that from the search source it try to get the value of storeid and that value get stored in new variable store which get further used directly in the function
3. Add a storeId query parameter to the URL and enter a random alphanumeric string as its value. Request this modified URL like this -product?productId=2&storeId=%27</option><script>alert(1)</script
4. Now you will see an alert pops up on the web page
5. In the browser,also notice that your random string which is %27 i.e ' is now listed as one of the options in the drop-down list.


---