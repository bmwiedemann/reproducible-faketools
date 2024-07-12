#!/usr/bin/env roundup

describe "roundup(1) testing of date"

it_normalizes_date() {
   result=$(SOURCE_DATE_EPOCH=1234567 ../bin/date -u -Iseconds)
   [[ "$result" = "1970-01-15T06:56:07+00:00" ]]
}

it_ignores_normalized_date() {
   result=$(SOURCE_DATE_EPOCH=1234567 ../bin/date -u -d @1 -Iseconds)
   [[ "$result" = "1970-01-01T00:00:01+00:00" ]]
   touch -d @1 .tmp
   result=$(SOURCE_DATE_EPOCH=1234567 ../bin/date -u -r .tmp -Iseconds)
   [[ "$result" = "1970-01-01T00:00:01+00:00" ]]
   rm -f .tmp
}
