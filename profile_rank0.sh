#!/bin/bash
if [[ $OMPI_COMM_WORLD_RANK == 0 ]]; then
~/nsys/nsys profile ./myapp "$@" --mydummyargument
else
./myapp "$@"
fi
