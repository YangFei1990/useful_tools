import math

ips = []
with open('hs','r') as fr:

    for _ in range(32):
        ips.append(fr.readline().strip())


with open('ranks','w') as fw:
    for i in range(256):

        host = int(math.floor(i/8))
        socket = int(math.floor(i/4))%2
        
        firstcore = (i%4)*8
        lastcore = ((i%4)+1)*8-1

        fw.write('rank %d=%s slot=%d:*\n'%(i, ips[host], socket))
