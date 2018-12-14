#!/bin/bash

ip=$(kubectl get pods -l 'app=master' -o json | \
            jq '.items[0].spec.nodeName' -r | \
            xargs -I {} kubectl get nodes/{} -o json | \
            jq '.status.addresses[] | select(.type == "ExternalIP") | .address' -r)

echo $ip
