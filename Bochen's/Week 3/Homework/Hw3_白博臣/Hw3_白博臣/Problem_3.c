#include <stdio.h>

int main()
{
	int a = 0x11223344;
	char *p =  (char *) &a;
	if(*p == 0x44)
		printf("小端序！\n");
	if(*p == 0x11)
		printf("大端序！\n");
	return 0;
}

