#include <string.h>

void *memcpy(void *dest, const void *src, size_t n) {
    return memmove(dest, src, n);
}

char *strncpy(char *dest, const char *src, size_t n) {
    int srcn = strlen(src) + 1;
    if(n > srcn) {
        memset(dest+srcn, 0, n-srcn);
        n = srcn;
    }
    return memmove(dest, src, n);
}

char *strcpy(char *dest, const char *src) {
    int n = strlen(src) + 1;
    return memmove(dest, src, n);
}
