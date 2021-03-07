from single_linked_list import SingleLinkedList


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def single_linked_list_demo():
    num_list = [1, 2, 3, 4, 5, 6]
    single_linked_list = SingleLinkedList(num_list)
    single_linked_list.traverse_list()
    node = single_linked_list.find_node(5)
    if node:
        print("node number: {} found".format(node.num))
    else:
        print("node 5 not found")
    single_linked_list.insert_node(8)
    print("after inserting node 8")
    single_linked_list.traverse_list()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    single_linked_list_demo()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
