#!/usr/bin/python3

from telnetlib import Telnet
from getpass import getpass

user_name = input('Enter the Master Username: ')
pass_word = getpass()

file_name = open('list_of_ips.txt')

for ip in file_name:
    ip = ip.strip()
    print ('Setting username and password on device: ', (ip), '...')

    telnet_connection = Telnet(ip)

    telnet_connection.read_until('Username: ')
    telnet_connection.write(user_name.encode('ascii') + b'\n')
    telnet_connection.read_until('Password: ')
    telnet_connection.write(pass_word.encode('ascii') + b'\n')

    telnet_connection.write('conf t\n')
    telnet_connection.write('username administrator password P@ssw0rd\n')
    telnet_connection.write('end\n')
    telnet_connection.write('wr\n')
    telnet_connection.write('exit\n')

    print(telnet_connection.read_all.decode('ascii'))

