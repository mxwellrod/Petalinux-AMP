/*
* A simple OCM write and read Demo for zynq7000 with linux
*/

#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/mman.h>
#include <unistd.h>

#define OCM_SIZE (256 * 1024) // OCM full size on bytes
#define OCM_LOC 0xFFFC0000 // OCM high ram distro base addr

int main(int argc, char **argv) {
    int err = 0;
    uint32_t *ocm, *buf, i;
    int memf;

    printf("OCM: 256 KB @ 0x%x\n", OCM_LOC);

    // Opens /dev/mem device(imagen de la memoria fisica)
    memf = open("/dev/mem", O_RDWR | O_SYNC); // read and write and cache disabled
    if (memf < 0) {
        err = errno;
        fprintf(stderr, "Error al abrir /dev/mem: %d\n", err); // envia el print a standar error(flujo de salida tipico junto stdint stdout)
        goto err_;
    }

    // OCM mapping to userspace
    ocm = mmap(NULL, OCM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, memf, OCM_LOC);
    if (ocm == MAP_FAILED) {
        err = errno;
        fprintf(stderr, "Error en mmap: %d\n", err);
        goto err_close;
    }

    printf("Escribiendo en OCM\n");
    for (buf = ocm, i = 0; i < OCM_SIZE / 4; ++i, ++buf) // secciones de 4 Bytes(32 bits)
        *buf = i;

    printf("Leyendo OCM\n"); 
    for (buf = ocm, i = 0; i < OCM_SIZE / 4; ++i, ++buf) { // Verificación
        printf("ocm[%x] = %x\n", i, *buf);
        if (*buf != i)
            fprintf(stderr, "ERROR en ocm[%x] = %x\n", i, *buf);
    }

    // Liberar recursos
    munmap(ocm, OCM_SIZE);
err_close:
    if (memf > 0) close(memf);
err_:
    return err;
}