# Add a custom HTTP header with Puppet

exec { 'Nginx Header':
command => 'sudo apt-get -y install haproxy;
echo "ENABLED=1" >> /etc/default/haproxy;
printf %s "listen holberton
    bind *:80
    mode http
    balance roundrobin
    server 1433-web-01 35.237.32.190:80 check
    server 1433-web-02 35.231.170.38:80 check
" >> /etc/haproxy/haproxy.cfg;
sudo service haproxy restart;
',
provider   => 'shell',
}