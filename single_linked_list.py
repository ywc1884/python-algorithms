import numbers


class SingleLinkedListNode:
    nextNode = None
    num = 0

    def __init__(self, number):
        self.num = number


class SingleLinkedList:
    headNode = SingleLinkedListNode(0)

    def __init__(self, numbers):
        if len(numbers) != 0:
            for n in numbers:
                node = SingleLinkedListNode(n)
                node.nextNode = self.headNode.nextNode
                self.headNode.nextNode = node

    def find_node(self, number):
        if self.headNode.nextNode is None:
            return None

        q = self.headNode.nextNode
        while q is not None:
            if q.num == number:
                return q
            q = q.nextNode
        return None

    def insert_node(self, number):
        if not isinstance(number, numbers.Number):
            print("only numbers could be inserted")
            return
        node = SingleLinkedListNode(number)
        node.nextNode = self.headNode.nextNode
        self.headNode.nextNode = node

    def delete_node(self, number):
        q = self.headNode.nextNode
        while q is not None and q.nextNode is not None:
            if q.nextNode.num == number:
                q.nextNode = q.nextNode.nextNode
            q = q.nextNode

    def traverse_list(self):
        if self.headNode.nextNode is not None:
            num_list = []
            q = self.headNode.nextNode
            while q is not None:
                num_list.append(q.num)
                q = q.nextNode
            if num_list:
                result = '-'.join([str(num) for num in num_list])
                print("linked list nodes: {}".format(result))
            else:
                print("linked list is empty")
