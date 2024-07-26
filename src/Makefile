build: rbftmalloc.so rbftmemcpy.so
rbftmalloc.so: malloc.c
	gcc -Wall -fPIC -shared -o $@ $< -ldl

rbftmemcpy.so: memcpy.c
	gcc -Wall -fPIC -shared -o $@ $<
