'''
Created on 23/02/2015

@author: Owner
'''

import sys,paramiko

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
        
    client.connect("10.10.11.100", port=22, username="root", password="abcd")
 
    stdin, stdout, stderr = client.exec_command("ls -l")
    print(stdout.read()),
    # dsadaskmdasklnkclna
 
finally:
    client.close()
