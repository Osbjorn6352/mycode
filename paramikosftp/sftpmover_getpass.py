#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords

def movethemfiles(sftp_object, target_dir):
    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy/" + x):
            sftp_object.put("/home/student/filestocopy/" + x, os.path.join(target_dir, x))

def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass

    target_dir = input("Which directory on the host machine would you like to move files to?\n> ")
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    try:
        sftp.stat(target_dir)
    except FileNotFoundError:
        print(f"Target directory '{target_dir}' does not exist on the remote host.")
        return

    ## copy our firstpasswd.py script to bender
    movethemfiles(sftp,target_dir) # move file to target location home directory
    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()

