#!/bin/sh

#symlinks_to_sandbox=(
#"etc"
#"tmp"
#"var"
#"gui/lighttpd/etc"
#"gui/lighttpd/logs"
#"gui/lighttpd/tmp"
#"gui/config"
#)

zend_install_dir="/usr/local/zend-server-6-php-5.4"
zend_sandbox="/sandbox/zend-server-6-php-5.4"
restore=$1

#This function symlinks the above paths to /sandbox PAM namespace
function create_zend_to_sandbox_links {
  mkdir -p $zend_sandbox
  for path in ${symlinks_to_sandbox[*]}; do
    zpath=$zend_install_dir/$path
    if [ ! -e $zpath ]; then
      echo "Path does not exist $zpath"
      if [ ! -h $zpath ]; then
        continue
      fi
    fi
    zdir=`dirname $zpath`
    zfile=`basename $zpath`
    if [ "$restore" == "restore" ]; then
      #echo "Undoing Linking $zdir/$zfile to $zend_sandbox/$path"
      rm -f $zdir/$zfile
      #echo "Removing $zend_sandbox"
      rm -rf $zend_sandbox
    else
      if [ ! -L $zpath ]; then
        #echo "Backing up $zpath to ${zpath}_openshift_original_$(date +%s)"
        cp -r $zpath ${zpath}_openshift_original_$(date +%s)
        #echo "Copying $zpath to $zend_sandbox/${path}"
        mkdir -p $zend_sandbox/${path}
        cp -r $zpath/* $zend_sandbox/${path}/.
        #echo "Removing $zpath"
        rm -rf $zpath
        #echo "Linking $zdir/$zfile to $zend_sandbox/$path"
        ln -s $zend_sandbox/$path $zdir/$zfile
      fi
    fi
  done
}


uid=`id -u`
if [ $uid -eq 0 ] ; then
 echo "Running as root..."
#Don't create sandbox since it is not user for the Zend Server version 6 cartridge
# create_zend_to_sandbox_links
fi

