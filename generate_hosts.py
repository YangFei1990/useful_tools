import os, math, sys


# get the list of private dns names in the vpc
ret = os.popen('aws ec2 describe-instances --query \'Reservations[].Instances[].[PrivateIpAddress]\' --filters "Name=instance-state-name,Values=running" "Name=instance-type,Values=p3dn.24xlarge" "Name=availability-zone,Values=us-east-1b"').read()
ret_tokenized = ret.split('"')

dns = []

for token in ret_tokenized:
  if token.startswith('172.'):
    dns.append(token)

# generate hostfile
with open('hosts','a') as f:
  for name in dns:
    f.write(name+'\n')


