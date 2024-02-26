#include "lists.h"

/**
 * is_palindrome - checks if the linked list is palindrome or not
 * @head: pointer to head of list
 * Return: 0 for not being palindrome, 1 for palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *top = *head;
	listint_t *current;
	listint_t *mirror;

	if (top == NULL)
		return (1);

	current = top->next;

	while (current != NULL)
	{
		if  (top == mirror || top->next == mirror)
			return (1);

		if (top->n == current->n)
		{
			if (top == *head)
			{
				if (current->next != NULL)
					return (0);
			}
			else
			{
				if (current->next != mirror)
					return (0);
			}
			top = top->next;
			mirror = current;
			current = top->next;
		}
		else
			current = current->next;
	}
	if (top->next == mirror || top->next == NULL || top == mirror)
		return (1);

	return (0);
}
