#include <stdio.h>

char * echo(char * what)
{
   return what;
}

int add_int(int a, int b)
{
    int sum = a+b;
    return sum;
}

int add_int(int a, int b)
{
    int sum = a+b;
    return sum;
}


int main(void)
{
    printf("hello\n");
    printf("%d\n", add_int(2, 3));
    printf("%s\n", echo("Foo"));
    return 0;
}

