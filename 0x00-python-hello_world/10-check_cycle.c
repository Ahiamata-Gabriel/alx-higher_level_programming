#include "lists.h"
/**
 *check_cycle - checks if there is a cycle in a linked list.
 *@list: head of the linked least
 *Return: 1 if there is a loop, 0-no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_pointer, *slow_pointer;

	if (list == NULL)
		return (0);

	fast_pointer = list;
	slow_pointer = list;
	while (fast_pointer && fast_pointer->next)
	{
		list = list->next;
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;
		if (fast_pointer == slow_pointer)
			return (1);
	}
	return (0);
}
