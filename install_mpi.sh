#!/bin/bash
hosts=`cat $1`


for host in $hosts; do
   ssh $host 'bash --login -c "screen -L -d -m bash -c \"cd /home/ubuntu/openmpi-4.0.0/; make -j $(nproc); sudo make install; sudo ldconfig\""'

done
