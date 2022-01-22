"""
Allison Valdez
Time complexity: O(n) where n is the number of nodes contained in the linked
list. Since we have a sorted linked list we only have to traverse it one
time to solve the problem.
Space complexity: O(1) since we do not use any external space, it only relies on
constant space.
"""
import null as null
from Mod1.linked_list import LinkedList


def remove_duplicates(linked_list):
    # declares the head node as the parameter given
    current_node = linked_list

    # first while loop that checks that the current node is not the tail
    while current_node is not None:
        next_node = current_node.next

        # second while loop to check that next_node is not a tail but same value
        while next_node is not None and next_node.value == current_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node
4
    return linked_list

print(remove_duplicates({
  "head": "1",
  "nodes": [
    {"id": "1", "next": null, "value": 1}
  ]
}))