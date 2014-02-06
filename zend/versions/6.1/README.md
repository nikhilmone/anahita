# Zend Server 6 Cartridge for Openshift

## Zend Server 6.x binaries installation

### from RPM:

    cat << EOF > /etc/yum.repos.d/zendserver-6.repo
    [Zend Server 6.x]
    name=Openshift-Zend-Server-6.x
    baseurl=http://repos.zend.com/zend-server-6.1.0-openshift/epel-6
    enabled=1
    EOF

    yum install -y zend-server-php-5.4

### from TAR GZ archive:

Download the Zend Server binaries from:

    https://docs.google.com/file/d/0BzHaQDVEbOVhbVBjeXZYZ184alU/edit?usp=sharing

Extract the zs6-binaries to / on your server (it should create /usr/local/zend-server-6-php-5.4 directory):

    tar --directory=/ -xvzf zs6-binaries.tar.gz

## Cartridge installation

### from RPM:

    yum install -y http://zend-tdawson.rhcloud.com/test/45621b875/openshift-origin-cartridge-zend-server-6-php-5.4-0.1.11-1.el6.noarch.rpm

### from GIT repository:

Clone and install ZS6 cartridge (you need to have access to the github repo):

    cd /usr/libexec/openshift/cartridges/
    git clone git@github.com:zendtech/zend-server-openshift-cartridge.git zendserver
    chown -R root:root zendserver
    cd zendserver
    oo-admin-cartridge -a install -s ./

Clear the cache

    oo-admin-broker-cache -c
    # rm -rf /var/www/openshift/broker/tmp/cache/*
    # cd /var/www/openshift/broker; scl enable ruby193 "bundle exec rake tmp:clear"

Check if ZS6 cartridge got installed successfully

    oo-admin-cartridge -l | grep zendserver
    rhc cartridge-list | grep zendserver

# Usage

## Creating a new app
To create a new app, run:

    rhc create-app z1 zendserver-6

After running this command you'll get detailed instructions on how to access the Zend Server console.

## Creating a new scaled app

    rhc create-app z2 zendserver-6 -s
