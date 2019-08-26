import os

# build known_hosts locally
with open('hosts_noslots','r') as f:
    for _ in range(4):
        ip = f.readline().strip()
        os.system('ssh-keyscan -H %s >> ~/.ssh/known_hosts'%ip)

# move known_hosts to all workers
with open('hosts_noslots','r') as f:
    for _ in range(4):
        ip = f.readline().strip()

        os.system('scp ~/.ssh/known_hosts ubuntu@%s:/home/ubuntu/.ssh'%ip)
