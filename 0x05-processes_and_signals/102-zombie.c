#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a fun to trap infinitely
 * Return: 0 if success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Return: 0 if success
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			perror("fork");
		else if (!pid)
			exit(0);
		printf("Zombie process created, PID:%d\n", pid);
	}
	infinite_while();
	return (0);
}
