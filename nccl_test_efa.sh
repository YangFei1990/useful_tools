# To use TREE change NCCL_TREE_THRESHOLD=4294967296
# To use RING change NCCL_TREE_THRESHOLD=0
# fp16: 88350184
# fp32: 176700368

#single node ring
mpirun -x FI_PROVIDER="efa" \
       -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
       -x FI_OFI_RXR_RX_COPY_OOO=1 \
       -x FI_EFA_MR_CACHE_ENABLE=1 \
       -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
       -x NCCL_TREE_THRESHOLD=0 \
       -H localhost:8 -n 8 -N 8 \
       --mca btl tcp,self \
       --mca btl_tcp_if_exclude lo,docker0 \
       --bind-to none \
       -x NCCL_DEBUG=INFO \
       nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 8gpus_ring_fp32.log

#Two nodes ring
mpirun -x FI_PROVIDER="efa" \
      -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
      -x FI_OFI_RXR_RX_COPY_OOO=1 \
      -x FI_EFA_MR_CACHE_ENABLE=1 \
      -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
      -x NCCL_TREE_THRESHOLD=0 \
      -hostfile hosts2 -n 16 -N 8 \
      --mca btl tcp,self \
      --mca btl_tcp_if_exclude lo,docker0 \
      --bind-to none \
      -x NCCL_DEBUG=INFO \
      nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 16gpus_ring_fp32.log

#Four nodes ring
mpirun -x FI_PROVIDER="efa" \
       -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
       -x FI_OFI_RXR_RX_COPY_OOO=1 \
       -x FI_EFA_MR_CACHE_ENABLE=1 \
       -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
       -x NCCL_TREE_THRESHOLD=0 \
       -hostfile hosts -n 32 -N 8 \
       --mca btl tcp,self \
       --mca btl_tcp_if_exclude lo,docker0 \
       --bind-to none \
       -x NCCL_DEBUG=INFO \
       nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 32gpus_ring_fp32.log

 #Eight nodes ring
 mpirun -x FI_PROVIDER="efa" \
        -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
        -x FI_OFI_RXR_RX_COPY_OOO=1 \
        -x FI_EFA_MR_CACHE_ENABLE=1 \
        -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
        -x NCCL_TREE_THRESHOLD=0 \
        -hostfile host8_slots -n 64 -N 8 \
        --mca btl tcp,self \
        --mca btl_tcp_if_exclude lo,docker0 \
        --bind-to none \
        -x NCCL_DEBUG=INFO \
        nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 64gpus_ring_fp32.log

###################################

#single node tree
mpirun -x FI_PROVIDER="efa" \
      -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
      -x FI_OFI_RXR_RX_COPY_OOO=1 \
      -x FI_EFA_MR_CACHE_ENABLE=1 \
      -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
      -x NCCL_TREE_THRESHOLD=4294967296 \
      -H localhost:8 -n 8 -N 8 \
      --mca btl tcp,self \
      --mca btl_tcp_if_exclude lo,docker0 \
      --bind-to none \
      -x NCCL_DEBUG=INFO \
      nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 8gpus_tree_fp32.log

#Two nodes tree
mpirun -x FI_PROVIDER="efa" \
     -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
     -x FI_OFI_RXR_RX_COPY_OOO=1 \
     -x FI_EFA_MR_CACHE_ENABLE=1 \
     -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
     -x NCCL_TREE_THRESHOLD=4294967296 \
     -hostfile hosts2 -n 16 -N 8 \
     --mca btl tcp,self \
     --mca btl_tcp_if_exclude lo,docker0 \
     --bind-to none \
     -x NCCL_DEBUG=INFO \
     nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 16gpus_tree_fp32.log

#Four nodes tree
mpirun -x FI_PROVIDER="efa" \
      -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
      -x FI_OFI_RXR_RX_COPY_OOO=1 \
      -x FI_EFA_MR_CACHE_ENABLE=1 \
      -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
      -x NCCL_TREE_THRESHOLD=4294967296 \
      -hostfile hosts4 -n 32 -N 8 \
      --mca btl tcp,self \
      --mca btl_tcp_if_exclude lo,docker0 \
      --bind-to none \
      -x NCCL_DEBUG=INFO \
      nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 32gpus_tree_fp32.log

#Eight nodes tree
mpirun -x FI_PROVIDER="efa" \
       -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
       -x FI_OFI_RXR_RX_COPY_OOO=1 \
       -x FI_EFA_MR_CACHE_ENABLE=1 \
       -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
       -x NCCL_TREE_THRESHOLD=4294967296 \
       -hostfile hosts8_slots -n 64 -N 8 \
       --mca btl tcp,self \
       --mca btl_tcp_if_exclude lo,docker0 \
       --bind-to none \
       -x NCCL_DEBUG=INFO \
       nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 64gpus_tree_fp32.log


#24 nodes tree
mpirun -x FI_PROVIDER="efa" \
      -x FI_OFI_RXR_RX_COPY_UNEXP=1 \
      -x FI_OFI_RXR_RX_COPY_OOO=1 \
      -x FI_EFA_MR_CACHE_ENABLE=1 \
      -x FI_OFI_RXR_INLINE_MR_ENABLE=1 \
      -x NCCL_TREE_THRESHOLD=4294967296 \
      -hostfile hosts24_slots -n 192 -N 8 \
      --mca btl tcp,self \
      --mca btl_tcp_if_exclude lo,docker0 \
      --bind-to none \
      -x NCCL_DEBUG=INFO \
      nccl-tests/build/all_reduce_perf -b 176700368 -e 176700368 -f 2 -g 1 -c 1 -n 100 |& tee 192gpus_tree_fp32.log
