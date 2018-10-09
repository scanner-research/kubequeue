#!/bin/bash

CLUSTER_ID=wc-test
ZONE=us-east1-b
NUM_NODES=3
WORKER_MACHINE=n1-standard-16

gcloud container clusters -q create ${CLUSTER_ID} \
       --zone ${ZONE} \
       --num-nodes 1 \
       --machine-type n1-standard-2

gcloud container node-pools -q create workers \
       --zone ${ZONE} \
       --cluster ${CLUSTER_ID} \
       --machine-type ${WORKER_MACHINE} \
       --num-nodes ${NUM_NODES} \
       --preemptible
