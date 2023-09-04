#include <stdio.h>
#include <string.h>

void comp_str(char argone[100], char argtwo[100]);

int main(void)
{
	comp_str("deobaba", "baba");
	comp_str("deobaba", "bbaa");

	return (0);
}

void comp_str(char *argone, char *argtwo)
{
    int i = 0;

    if (strstr(argone, argtwo) != NULL)
		printf("true\n");
	else
		printf("false\n");
}

