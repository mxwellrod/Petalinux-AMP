/*
*
* Read some OCM values. Used to check if core1 writes succesfully on OCM directory
*
*/


#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define OCM_BASE_ADDR  0xFFFC0000  // OCM base address mapped on linux
#define OCM_SIZE       0x40000    // OCM size -> 256 KB -> (0xFFFC0000 - 0xFFFFFFFF)
#define NUM_FLOATS     (OCM_SIZE / sizeof(float))  // number of floats

int main() {

    int mem_fd;
    volatile float *mem;

    // open dev/mem(image of physical memory)
    mem_fd = open("/dev/mem", O_RDWR | O_SYNC);
    if (mem_fd < 0) {
        perror("error opening dev/mem");
        return -1;
    }

    // mapping memory to userspace as floats
    mem = (float *)mmap(NULL, OCM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, OCM_BASE_ADDR); //cast allows to interpret memory as a floats array -> allow use of mem[i]
    if (mem == MAP_FAILED) {
        perror("Error mapping");
        close(mem_fd);
        return -1;
    }

    // simple check for first and last values
    printf("FIRST 10 values:\n");
    for (int i = 0; i < 10; i++) {
        printf("mem[%d] = %.2f\n", i, mem[i]);
    }

    printf("LAST 10 values\n");
    for (int j = NUM_FLOATS - 10; j < NUM_FLOATS; j++) {
        printf("mem[%d] = %.2f\n", j, mem[j]);
    }

    // Unmap and close fd
    munmap((void *)mem, OCM_SIZE);
    close(mem_fd);

    return 0;


}