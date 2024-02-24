#include "list.h"

/**
 * check_cycle - check for cycles
 * @list: head of linked list
 * Return: 0 for no circles, 1 for circles
 */

int check_cycle(listint_t *list)
{
        listint_t *current_one = list->next;
	listint_t *current_two = list->next->next;

	if (list == NULL)
		return (0);

	while (current_one != current_two)
	{
		if (current_one == NULL || current_two == NULL)
			return (0);
		current_one = current_one->next;
		current_two = current_two->next->next;
	}
        return (1);
}	
