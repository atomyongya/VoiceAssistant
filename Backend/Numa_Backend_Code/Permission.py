import pexpect
import sys
def Permissions():

    # here you issue the command with "sudo"
    child = pexpect.spawn('sudo /usr/bin/lsof')
    # it will prompt something like: "[sudo] password for < generic_user >:"
    # you "expect" to receive a string containing keyword "password"
    child.expect('password')
    # if it's found, send the password
    child.sendline('wezx1234@')
    # read the output
    print(child.read())
    # the end
    print("Enter you password: ")
    input()