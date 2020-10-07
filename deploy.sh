#!/bin/bash

echo "START DEPLOY"
cd /home/ubuntu/purple_task
sudo git pull
sudo pip install -r requirements/txt
echo "OK"

