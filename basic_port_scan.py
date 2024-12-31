import os

line = " +++++++++++++++++++++++++++++ "
print(line)
print("            Welcome to Port Scanner               ")
print(line)
print()

# Prompt user for input
dns = input("Enter the website to be scanned: ")

# Perform port scan
os.system(f"sudo nmap -sS -p 20,21,22,443,80,8080 {dns}")
print(line)
print("         OS scan starts now          ")
print(line)

# Perform OS scan
os.system(f"sudo nmap -O {dns}")
