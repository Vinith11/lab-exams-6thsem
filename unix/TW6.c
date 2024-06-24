#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

void charatatime(const char *str) {
  const char *ptr;
  int c;

  setbuf(stdout, NULL);
  for (ptr = str; (c = *ptr++) != 0;) {
    putc(c, stdout);
  }
}

int main() {
  pid_t pid;
  for (int i = 0; i < 3; ++i) {
    if ((pid = fork()) < 0) {
      perror("fork error"); 
      return 1;
    } else if (pid == 0) {
      charatatime("output from child\n");
      _exit(0);
    } else {
      charatatime("output from parent\n");
    }
  }
 
  while (wait(NULL) > 0); 

  return 0;
}

//regular