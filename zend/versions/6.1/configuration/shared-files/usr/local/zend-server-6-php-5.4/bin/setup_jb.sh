#!/bin/bash
if [ -f $ZCE_PREFIX/bin/shell_functions.rc ];then
    . $ZCE_PREFIX/bin/shell_functions.rc
else
    echo "$ZCE_PREFIX/bin/shell_functions.rc doesn't exist!"
    exit 1;
fi
if [ -z "$JAVA_PATH" ];then
    echo "Welcome to Java bridge setup!"
    JAVA=`which java 2>/dev/null`
    if [ ! -z $JAVA ];then
        JAVA_DEF="[$JAVA]"
    fi
    while [ ! -x "$JAVA_PATH" -o ! -f "$JAVA_PATH" ];do
        echo "Please specify path the Java executable ${JAVA_DEF}:"
        echo "NOTE: please use Java by Sun or IBM version 1.5 and above."
        read -e JAVA_PATH
        if [ -z $JAVA_PATH ]; then
            JAVA_PATH=$JAVA
        fi
    done
fi
perl -pe "s@zend_wd.process.java_daemon=([a-zA-Z0-9/._-]+)\s(.*)\$@zend_wd.process.java_daemon=$JAVA_PATH \2@" -i ${ZCE_PREFIX}/etc/watchdog-jb.ini
# since we don't want this export duplicated, we first remove any leftovers and then insert the export statement
sed -i 's/JB_EN=.*//g' /etc/zce.rc
ln -sf ${ZCE_PREFIX}/bin/java_bridge.sh ${ZCE_PREFIX}/etc/rc.d/S07jb
ln -sf ${ZCE_PREFIX}/bin/java_bridge.sh ${ZCE_PREFIX}/etc/rc.d/K02jb
${ZCE_PREFIX}/bin/java_bridge.sh start
perl -pe  's/;zend_extension_manager.dir.jbridge/zend_extension_manager.dir.jbridge/g' -i $ZCE_PREFIX/etc/conf.d/jbridge.ini 
chgrp zend $ZCE_PREFIX/etc/conf.d/jbridge.ini $ZCE_PREFIX/etc/watchdog-jb.ini
chmod 664 $ZCE_PREFIX/etc/conf.d/jbridge.ini $ZCE_PREFIX/etc/watchdog-jb.ini
${ZCE_PREFIX}/bin/apachectl restart
