#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - parent process
 * @void : void
 * Return: Always 0.
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
 * main - zombies process
 * @void : nothing
 * Return: Always 0.
 */
int main(void)
{

	pid_t pid;
	int i = 0;

	for (; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);

		else
			exit(0);
	}

	infinite_while();

	return (0);

}
