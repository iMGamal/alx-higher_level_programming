#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for the presence of a cycle in a singly linked list
 * @list: pointer to the head of a list
 * Return: Always 0 (Success)
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	harr = list;

	while (tortoise != NULL && hare->next && hare->next->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
