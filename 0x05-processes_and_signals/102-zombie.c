#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * create_zombie_process - Create a zombie process.
 *
 * Return: None.
 */
void create_zombie_process(void)
{
	pid_t pid;

	pid = fork();
	if (pid > 0)
	{
		printf("Zombie process created, PID: %d\n", pid);
		sleep(1);
	}
	else if (pid == 0)
		exit(0);
	else
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	char count = 0;

	while (count < 5)
	{
		create_zombie_process();
		count++;
	}

	while (1)
	{
		sleep(1);
	}

	return (EXIT_SUCCESS);
}
