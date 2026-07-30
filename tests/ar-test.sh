#!/usr/bin/env roundup

describe "roundup(1) testing of ar"

before() {
    printf 'int reproducible_ar_test;\n' > .ar.c
    cc -c .ar.c -o .ar.o
}

after() {
    rm -f .ar.c .ar.o .ar1.a .ar2.a
}

# Two archives of the same object, created with different mtimes on it, have
# to come out byte for byte equal, and the member header has to be zeroed.
# binutils ar already clamps the mtime to SOURCE_DATE_EPOCH on its own, so the
# uid/gid check is the part that actually tests this wrapper rather than ar.
mkboth() {
    touch -d @1000000000 .ar.o
    SOURCE_DATE_EPOCH=1234567 ../bin/ar "$@" .ar1.a .ar.o
    touch -d @2000000000 .ar.o
    SOURCE_DATE_EPOCH=1234567 ../bin/ar "$@" .ar2.a .ar.o
    cmp .ar1.a .ar2.a
    ar tv .ar1.a | grep -q ' 0/0 '
}

it_normalizes_dash_r() {
    mkboth -r
}

# cc-rs
it_normalizes_cq() {
    mkboth cq
}

# libtool
it_normalizes_cru() {
    mkboth cru
}

# cmake
it_normalizes_qc() {
    mkboth qc
}

it_normalizes_crs() {
    mkboth crs
}

it_zeroes_uid_and_mtime() {
    SOURCE_DATE_EPOCH=1234567 ../bin/ar cq .ar1.a .ar.o
    ../bin/ar tv .ar1.a | grep -q ' 0/0 '
    ../bin/ar tv .ar1.a | grep -q '1970'
}

it_leaves_long_options_alone() {
    SOURCE_DATE_EPOCH=1234567 ../bin/ar --version | grep -q 'GNU ar\|BSD ar\|llvm-ar'
}

it_passes_through_read_only_ops() {
    SOURCE_DATE_EPOCH=1234567 ../bin/ar cq .ar1.a .ar.o
    SOURCE_DATE_EPOCH=1234567 ../bin/ar t .ar1.a | grep -q '.ar.o'
}

it_does_nothing_without_source_date_epoch() {
    touch -d @1000000000 .ar.o
    ../bin/ar cq .ar1.a .ar.o
    touch -d @2000000000 .ar.o
    ../bin/ar cq .ar2.a .ar.o
    ! cmp -s .ar1.a .ar2.a
}
