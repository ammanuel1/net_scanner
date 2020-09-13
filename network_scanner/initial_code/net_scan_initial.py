import subprocess
from subprocess import Popen, PIPE

ip = input("Enter IP Address (in XXX.XXX.XXX.X format): ")

ip_split = ip.split('.')

x = '.'

ip2 = ip_split[0] + x + ip_split[1] + x + ip_split[2] + x 

for i in range(0,256):
    address = ip2 + str(i)
    result = Popen(['ping','-c','1',address], stdout=PIPE)
    output = result.communicate()[0]
    value = result.returncode
    if value == 0:
        print('ping to', address, 'WORKED')
    else: 
        print('ping to ', address, 'FAILED')
