#include <stdio.h>
#include <stdlib.h>

/**
 * struct list - singly linked list
 * @x: integer value stored in node of the list
 * @next: pointer to the next node
 */
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
	linked *new_node;

	new_node = create(x);
	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		linked *temp;

			temp = *head;
			while (temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = new_node;
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
}

void freeN(linked *head)
{
	linked *temp;

	temp = head;
	while(temp != NULL)
	{
		temp = temp->next;
		free(temp);
	}
}

int check(linked *head)
{
	linked *tortoise, *hare;

	tortoise = head;
	hare = head;
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

int main(void)
{
	linked *head;

	head = NULL;
	add(&head, 1);
	add(&head, 2);
	add(&head, 3);

	print(head);
	return (0);
}
