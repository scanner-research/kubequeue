#!/bin/bash

kubectl create -f master.yaml
kubectl expose deploy/master --port 6379 --type NodePort
kubectl create -f worker.yaml
