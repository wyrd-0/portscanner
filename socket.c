#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>


int main(int argc, char *argv[])
{
	int s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);

	if (s == -1) 
	{
		printf("Error in socket creation");
	}

	return 0;
}
