#include "lists.h"

/**
 * check_cycle - check if list is cycle
 *
 * @list: type listint_t
 *
 * Return: 1 true, 0 false
 */

int check_cycle(listint_t *list)
{
  listint_t *list1 = list, *list2 = list;

  while (list1 != NULL && list2 != NULL && (*list2).next != NULL)
    {
      list1 = (*list1).next;
      list2 = (*(*list2).next).next;

      if (list1 == list2)
	return(1);
    }
  return(0);
}
