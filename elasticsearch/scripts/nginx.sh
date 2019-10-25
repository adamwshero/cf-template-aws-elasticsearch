#!/bin/bash

# Install nginx
apt-get install nginx -y

#Start service
systemctl start nginx

#Ensure Nginx restarts on reboot
systemctl enable nginx