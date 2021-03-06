// play with memcpy
#include <stdio.h>

int main(int argc, char *argv[])
{
  int numbers[4] = { 0 };
  char name[4] = { 'a', 'a', 'a' };

  // first, print them out raw
  printf("numbers: %d %d %d %d\n",
    numbers[0],
    numbers[1],
    numbers[2],
    numbers[3]
  );

  printf("name each: %c %c %c %c\n",
    name[0],
    name[1],
    name[2],
    name[3]
  );

  printf("name: %s\n", name);

  // set up the numbers
  numbers[0] = '3';
  numbers[1] = 'a';
  numbers[2] = 'E';
  numbers[3] = '_';

  // set up the name
  name[0] = 120;
  name[1] = 66;
  name[2] = 69;
  name[3] = 85;

  // print them out initialized
  printf("numbers: %d %d %d %d\n",
    numbers[0],
    numbers[1],
    numbers[2],
    numbers[3]
  );

  printf("name each: %c %c %c %c\n",
    name[0],
    name[1],
    name[2],
    name[3]
  );

  printf("name: %s\n", name);

  // another way to use name
  char *another = "Zed";

  printf("another: %s\n", another);

  printf("another each: %c %c %c %c\n",
    another[0],
    another[1],
    another[2],
    another[3]
  );

  return 0;
}
