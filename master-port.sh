#!/bin/bash

port=$(kubectl get svc/master -o json | \
              jq '.spec.ports[0].nodePort' -r)

echo $port
