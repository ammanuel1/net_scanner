import subprocess
from subprocess import Popen, DEVNULL

ip = input("Enter IP Address (in XXX.XXX.XXX.X format): ")

ip_split = ip.split('.')

x = '.'

ip2 = ip_split[0] + x + ip_split[1] + x + ip_split[2] + x 
p = {}
for i in range(0,256):
    address = ip2 + str(i)
    p[address] = Popen(['ping','-c','1',address], stdout=DEVNULL)
success = []
while p:
    for address, value in p.items():
        if value.poll() is not None:
            del p[address]
            if value.returncode == 0:
                print('%s WORKING' % address)
                success.append(address)
            elif value.returncode == 1:
                print('%s NO RESPONSE' % address)
            else:
                print('%s FAILURE' % address)
            break
print(success, "Responded")