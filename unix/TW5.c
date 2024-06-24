#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    pid_t child_pid;

    // Create a child process
    child_pid = fork();

    if (child_pid == 0)
    {
        printf("Child process with PID %d exiting...\n", getpid());
        exit(0);
    }
    else if (child_pid > 0)
    {

        printf("Parent process with PID %d waiting...\n", getpid());

        sleep(5); 

        system("ps -o pid,ppid,state,tty,command");
    }
    else
    {
        // Fork failed
        perror("fork");
        exit(1);
    }

    return 0;
}

// # gcc TW5.c
// # ./a.out
