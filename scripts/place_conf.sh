# https://aws.amazon.com/premiumsupport/knowledge-center/kibana-outside-vpc-nginx-elasticsearch/
#
# Move the Nginx config file to it's final resting place
# and set some good permissions.
mv /home/es-config/default.conf /etc/nginx/sites-available/cognito
chmod -R 744 /etc/nginx/sites-available/cognito

# Create a symlink so Nginx will use the new config file.
# https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
ln -s /etc/nginx/sites-available/cognito /etc/nginx/sites-enabled/

# Replace default nginx.conf with good nginx.conf file with a larger hash_bucket_size.
# https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
# 
# This copy while overwriting might be tricky but we'll try it this way first. 
# https://stackoverflow.com/questions/8488253/how-to-force-cp-to-overwrite-without-confirmation
cp -r /home/es-config/nginx.conf /etc/nginx/nginx.conf
chmod -R 744 /etc/nginx/nginx.conf

# Restart Nginx so it will take the new configs.
systemctl restart nginx