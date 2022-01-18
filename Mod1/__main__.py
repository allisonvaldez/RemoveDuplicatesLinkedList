"""
Allison Valdez
Time complexity: O(n) where n is the number of nodes contained in the linked
list. Since we have a sorted linked list we only have to traverse it one
time to solve the problem.
Space complexity: O(1) since we do not use any external space, it only relies on
constant space.
"""
from Mod1.linked_list import LinkedList

def remove_duplicates(linked_list):
    # declares the head node as the parameter given
    current_node = linked_list

    # first while loop that checks that the current node is not the tail
    while current_node is not None:
