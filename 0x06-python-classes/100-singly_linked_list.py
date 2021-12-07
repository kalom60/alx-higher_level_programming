#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        rtn = ""
        pt = self.__head

        while pt is not None:
            rtn += str(pt.data)
            if pt.next_node is not None:
                rtn += "\n"
            pt = pt.next_node

        return rtn

    def sorted_insert(self, value):
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
