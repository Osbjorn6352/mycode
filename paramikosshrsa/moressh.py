#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko
import yaml

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    with open('credz.yml', 'r') as yamlFile:
        credz = yaml.load(yamlFile, Loader=yaml.FullLoader)

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    with open("results.log", 'w') as f:
        f.write('')

    # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        ## display output
        with open('results.log', 'a') as f:
            print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"), file=f)
            print(sessout.read().decode('utf-8'), file=f)


        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()

