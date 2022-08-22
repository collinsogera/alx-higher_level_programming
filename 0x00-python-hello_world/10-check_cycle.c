#include "lists.h"

/**
*check_cycle - Checks if cycle is singly linked
*list - linked list
*
*Return: 0 if cycle, 1 if no cycle
*/

int check_cycle(listint_t *list)
{
	listinit_t *x, *y;
	
	x = list;
	y = list;

	while (x && y)
	{
		if (y->next == NULL)
			return (0);
		x = x->next;
		y = y->next->next;
		if (x == y)
			return (1);
	}

	return (0);
}
