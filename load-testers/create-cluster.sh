#!/bin/bash

gcloud container --project ${PROJECT_ID} clusters create "loadtesting" --zone "us-east1-b" --username "admin" --cluster-version "1.14.6-gke.13" --machine-type "custom-8-8192" --image-type "COS" --disk-size "10" --scopes "https://www.googleapis.com/auth/compute","https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --preemptible --num-nodes "1" --network "default" --no-enable-cloud-logging --enable-cloud-monitoring --subnetwork "default" --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autorepair

sleep 5
gcloud container clusters get-credentials loadtesting --zone us-east1-b --project ${PROJECT_ID}
