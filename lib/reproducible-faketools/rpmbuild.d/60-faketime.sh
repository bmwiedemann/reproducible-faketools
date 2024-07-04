. $(dirname $0)/../lib/reproducible-faketools/lib
step=1
faketoolnotice step=$step date=$SOURCE_DATE_EPOCH
export FAKETIME_DONT_RESET=1
wrapper+=(faketime -f "@$(date -u -d@$SOURCE_DATE_EPOCH "+%F %T") i$step")
