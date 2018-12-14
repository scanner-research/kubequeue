#!/bin/bash

IMAGE_NAME=kubequeue-wc
TAG=gcr.io/$(gcloud config get-value project)/${IMAGE_NAME}
docker build -t ${TAG} .
gcloud docker -- push ${TAG}
