#!/bin/sh
log=/srv/doit.log
echo start doit at `/bin/date -Iseconds` >> $log
source /srv/*/doit.env
CMD="python /srv/can-i-order-iphone-x-yet/cli.py $zip $phone"
$CMD >> /srv/doit.log 2>&1
echo end doit at `/bin/date -Iseconds` >> /srv/doit.log
