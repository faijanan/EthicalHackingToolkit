import requests

domain = input("Enter domain: ")
subdomains = ["www", "mail", "ftp", "dev", "test"]

for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        requests.get(url)
        print(f"[+] Found: {url}")
    except:
        pass
