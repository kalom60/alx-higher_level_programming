#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """Represents a node in a singly linked list

    Attributes:
        __data (int): data stored inside the node
        __next_node (Node): next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): data stored inside the node
            next_node (Node): next node in the linked list

        Returns:
            None
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of __data

        Returns:
            data stored inside the node
        """

        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data

        Args:
            value (int): data stored insite the node

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of __next_node

        Returns:
           the next node in the linked list
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node

        Args:
            value (Node): next node in the linked list

        Returns:
            None
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a class name SinglyLinkedList"""


class SinglyLinkedList:
    """Represents a single linked list

    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """Initializes the linked list

        Returns:
            None
        """

        self.__head = None

    def __str__(self):
        """String representation of SinglyLinkedList instance

        Returns:
            Formatted string representing the linked list
        """

        rtn = ""
        pt = self.__head

        while pt is not None:
            rtn += str(pt.data)
            if pt.next_node is not None:
                rtn += "\n"
            pt = pt.next_node

        return rtn

    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position

        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """

        pt = self.__head

        while pt is not None:
            if pt.data > value:
                break
            pt_prev = pt
            pt = pt.next_node

        new_node = Node(value, pt)
        if pt == self.__head:
            self.__head = new_node
        else:
            pt_prev.next_node = new_node
