CFLAGS:=-O2 -Wall -fPIC -shared

build: rbftmalloc.so rbftmemcpy.so
rbftmalloc.so: malloc.c
	${CC} ${CFLAGS} -o $@ $< -ldl

rbftmemcpy.so: memcpy.c
	${CC} ${CFLAGS} -o $@ $<
