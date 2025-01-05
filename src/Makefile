build: rbftmalloc.so rbftmemcpy.so
rbftmalloc.so: malloc.c
	gcc -O2 -Wall -fPIC -shared -o $@ $< -ldl

rbftmemcpy.so: memcpy.c
	gcc -O2 -Wall -fPIC -shared -o $@ $<
