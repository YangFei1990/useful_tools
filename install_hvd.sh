#!/bin/bash
hosts=`cat $1`


for host in $hosts; do
#    scp tensorflow-1.12.0-cp27-cp27mu-linux_x86_64.whl ubuntu@$host:~

#   ssh $host 'bash --login -c "screen -L -d -m bash -c \"pip2 install tensorflow-1.12.0-cp27-cp27mu-linux_x86_64.whl\""'
    ssh $host 'bash --login -c "screen -L -d -m bash -c \"pip2 uninstall horovod -y; HOROVOD_NCCL_HOME=/usr/local/nccl HOROVOD_GPU_ALLREDUCE=NCCL pip2 install horovod==0.15.2 --no-cache-dir\""'
done
