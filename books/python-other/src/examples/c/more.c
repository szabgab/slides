#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int len(char * s)
{
   return strlen(s);
}

char * concat(char * a, char * b)
{
   char * res;
   int leng = strlen(a) + strlen(b);
   res = (char *)malloc(leng);
   strcpy (res, a);
   strcat (res, b);
   return res;
}


int main(void)
{
    printf("concat\n");
    printf("%d\n", len("abc"));
    printf("%d\n", len(""));
    printf("%d\n", len("xxxxxxxxxx"));
    printf("%s\n", concat("Foo1", "Bar"));
    return 0;
}

