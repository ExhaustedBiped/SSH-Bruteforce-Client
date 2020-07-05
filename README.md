# SSH-Bruteforce-Client
Extra-simple ssh credentials bruteforce client written in python.

### Running:
Execute `pip3 install paramiko colorama` in the terminal to install Paramiko (for SSH connections) and Colorama (to make it look fancy.) Then run it:

`python3 sshbruteforce.py <ip> -u <username> -P <wordlist .txt file>`

Depending on your computer's processing power, this can take a while. Here's a maxim: Higher Hertz, Hastier Hacking.

At some point I will add a 12gb file full of common passwords from weakpass to use as a (efficient) baseline.

### Disclaimer:

This software is for ethical and/or educational purposes only. DO NOT USE WITHOUT PERMISSION FROM THE ADMINISTRATOR OF THE SERVER YOU ARE ATTEMPTING TO BRUTEFORCE. I take no responsibility for any trouble you get into for using this. Just don't be stupid.
