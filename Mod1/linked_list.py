"""
Code created by Allison Valdez.
The purpose of this file is to instantiate the linked list data structure as
well as create all subsequent nodes and attributes necessary for the
structure to work.
"""


class LinkedList:
    def __init__(self, value):
        """
        When we design a class we have to make sure that the it is
        initialized with the proper attributes it needs to run properly. The
        next node is already set to a default value of none.

        :param value: the value contained in the node
        """
        self.value = value
        self.next = None

