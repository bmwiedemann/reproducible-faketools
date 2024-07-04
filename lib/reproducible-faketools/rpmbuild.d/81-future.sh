: ${years:=16}
now=$(date +%s)
: ${datediff:=$(((((365*$years+36)*24+13)*60+17)*60))}
: ${date:=$((now+datediff))}
# needs root permissions:
if [[ $UID = 0 ]] ; then
    date --set @$date
else
    faketoolnotice "faketools not running as root - cannot set system clock"
fi
