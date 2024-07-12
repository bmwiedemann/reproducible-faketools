#!/usr/bin/env roundup

describe "roundup(1) testing of jar"

it_normalizes_mtime_on_create() {
   test -e /usr/bin/jar || return 0
   mkdir -p tmp
   echo foo > tmp/foo
   SOURCE_DATE_EPOCH=1 ../bin/jar --create --file tmp/test.jar tmp/foo
   hash=$(md5sum tmp/test.jar | cut -d" " -f1)
   rm -rf tmp
   [[ "$hash" = 5c9de655dea174b60f195771ce3094fa ]] || [[ "$hash" = 7eebf70ccec32147cd291da1b3acb041 ]]
}
