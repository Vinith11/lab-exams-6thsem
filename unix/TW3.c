// hardlink and softlink
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[])
{

  if (argc < 3 || argc > 4)
  {
    printf("Usage: %s [-s] <source_file> <destination_file>\n", argv[0]);
    return 1;
  }

  if (argc == 4 && strcmp(argv[1], "-s") != 0)
  {
    printf("Usage: %s [-s] <source_file> <destination_file>\n", argv[0]);
    return 1;
  }

  if (argc == 4)
  {
    if (symlink(argv[2], argv[3]) == -1)
    {
      perror("symlink");
      return 1;
    }
    printf("Symbolic link created successfully\n");
  }
  else
  {
    if (link(argv[1], argv[2]) == -1)
    {
      perror("link");
      return 1;
    }
    printf("Hard link created successfully\n");
  }

  return 0;
}

// # gcc TW3.c
// # ./a.out soft.txt hard.txt
// Hard link created successfully
// # ./a.out -s soft.txt softly.txt
// Symbolic link created successfully