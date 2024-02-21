#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>


int main(void)
{
    printf("HI\n");
    int pid = fork();
    printf("after fork [%i]\n", pid);
    return (0);
}