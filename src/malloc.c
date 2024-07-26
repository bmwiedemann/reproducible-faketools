#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>

void *malloc(size_t size) {
    //printf("In rbft malloc %li\n", size);

    void *(*original_malloc)(size_t size);
    original_malloc = dlsym(RTLD_NEXT, "malloc");
    if(original_malloc == NULL) {
        printf("could not find original malloc");
        return NULL;
    }
    void *ret = (*original_malloc)(size);
    if(ret == NULL) {
        return ret;
    }
    memset(ret, 0, size); // ensure memory is initialized
    return ret;
}
