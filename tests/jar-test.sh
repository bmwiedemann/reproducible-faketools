#!/usr/bin/env roundup

describe "roundup(1) testing of jar"

it_normalizes_mtime_on_create() {
   test -e /usr/bin/jar || return 0
   mkdir -p tmp
   echo foo > tmp/foo
   SOURCE_DATE_EPOCH=1 ../bin/jar --create --file tmp/test.jar tmp/foo
   hash=$(zipinfo -T  tmp/test.jar | sed -n 's/ 5[0-6] / 51 /; 3,5p' | md5sum | cut -d" " -f1)
   rm -rf tmp
   [[ "$hash" = 0142cf4129848d42e3f08f35f8cd56fc ]]
}
