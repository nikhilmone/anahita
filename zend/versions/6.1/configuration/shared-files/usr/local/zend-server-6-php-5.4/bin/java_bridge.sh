#!/bin/bash 
NAME="Java bridge"
JB_EN="false";

#Don't parse zce.rc in openshift - the character generates the variables
#if [ ! -x $ZCE_PREFIX/php-5.4/etc/rc.d/S07jb ];then
#    echo "Please run $ZCE_PREFIX/bin/setup_jb.sh"
#    exit 1
#fi
if [ -f $ZCE_PREFIX/bin/shell_functions.rc ];then
    . $ZCE_PREFIX/bin/shell_functions.rc
else
    echo "$ZCE_PREFIX/bin/shell_functions.rc doesn't exist!"
    exit 1;
fi
#check_root_privileges
WD_UID=$WEB_USER
WD_GID=$WEB_USER
. ${ZCE_PREFIX}/bin/shell_functions.rc
WD_INI=${ZCE_PREFIX}/etc/watchdog-jb.ini
WATCHDOG="${ZCE_PREFIX}/bin/watchdog -c $WD_INI"
BINARY=java_daemon



start()
{
    launch
}

stop()
{
    _kill
}
status()
{
    $WATCHDOG -i $BINARY
}
case "$1" in
	start)
		start
		#sleep 1
		status
		;;
	stop)
		stop
		rm -f ${ZCE_PREFIX}/tmp/java_daemon.{app,wd}
		;;
	restart)
		stop
		rm -f ${ZCE_PREFIX}/tmp/java_daemon.{app,wd}
		sleep 1
		start
		;;
	status)
                status
		;;
	*)
		usage
esac

exit $?
