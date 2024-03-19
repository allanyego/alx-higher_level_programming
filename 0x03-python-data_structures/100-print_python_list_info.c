#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: A Python Common Object Structure - PyObject
 */
void print_python_list_info(PyObject *p)
{
  Py_ssize_t size, alloc;
  PyObject *item;

  size = PyList_Size(p); /* Get the size of the list */
  /* Get the allocated space for the list */
  alloc = ((PyListObject *)p)->allocated;

  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", alloc);

  /* Iterate through each item in the list */
  printf("[*] Element %ld: ", size);
  for (Py_ssize_t i = 0; i < size; i++)
  {
    item = PyList_GetItem(p, i); /* Get the item at index i */

    /* Print the type name of the item */
    printf("%s\n", Py_TYPE(item)->tp_name);
  }
}
