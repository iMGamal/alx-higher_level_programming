#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
	int x;
	struct list *next;
} linked;

linked *create(int x)
{
	linked *node;

	node = (linked *)malloc(sizeof(linked));
	if (!node)
	{
		printf("Failed allocation");
		return (NULL);
	}
	node->x = x;
	node->next = NULL;
	return (node);
}

void add(linked **head, int x)
{
	linked *new;

	new = create(x);
	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		linked *temp;

		temp = *head;
		while (temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = new;
	}
}

void print(linked *head)
{
	linked *temp;

	temp = head;
	while (temp != NULL)
	{
		printf("%d\n", temp->x);
		temp = temp->next;
	}
	printf("NULL\n");
}

int check(linked *head)
{ 

	linked *tortoise, *hare;

	tortoise = head;
	hare = head;
	while (tortoise != NULL && hare->next && hare)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
		{
			return (1);
		}
	}
	return (0);
}

void freeN(linked *head)
{
	linked *temp;

	temp = head;

	while (temp != NULL)
	{
		temp = temp->next;
		free(temp);
	}
}

int main(void)
{
	linked *head, *first, *third;

	head = NULL;
	add(&head, 1);
	add(&head, 2);
	add(&head, 3);

	first = head;
	third = head->next->next;
	third->next = first;

	printf("Is there is a cycle ? %d\n", check(head));
	return (0);
}
