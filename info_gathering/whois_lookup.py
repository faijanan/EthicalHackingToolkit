import whois

domain = input("Enter domain: ")
info = whois.whois(domain)
print(info)
