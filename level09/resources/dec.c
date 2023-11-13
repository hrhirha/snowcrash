#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

int main()
{
	int fd, len;
	char s[1024];
	if ((fd = open("token", O_RDONLY)) < 0)
	{
		printf("Could not open token\n");
		return 1;
	}
	len = read(fd, s, 1024);
	s[len] = '\0';
	for (unsigned int i = 0; i < len; i++)
	{
		printf("%c", s[i]-i);
	}
	printf("\n");
	return 0;
}
