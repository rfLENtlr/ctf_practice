#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>

ssize_t getrandom(void *buf, size_t buflen, unsigned int flags) {
    memset(buf, 202, buflen);
    return buflen;
}