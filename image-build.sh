#!/bin/bash

TAG=gcr.io/$(gcloud config get-value project)/kubequeue
docker build -t ${TAG} .
gcloud docker -- push ${TAG}
