__author__ = 'IAV'
__author__ = 'SBP'

"""
CSCI-603 Computational Problem Solving
Author: Indrajeet Vidhate
Author: Shubham Patil
Lab 6
"""


class DNA:
    """
    Node class for the DNA(gene)'s. Every individual DNA
    is a node in the DNAList.
    """
    __slots__ = ['value', 'next_node']

    def __init__(self, value, next_node=None):
        """
        Constructor to initialize the value of the
        DNA and next node.
        :param value: value of the DNA node.
        :param next_node: link to the next DNA(gene) node.
        :pre: None
        :post: a single node with given value is created
        and also link to next_node is created.
        """
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class DNAList:
    """
    List of DNA(gene)'s constructed using DNA node class.
    """
    __slots__ = ['head', 'gene', 'tail']

    def __init__(self, gene=''):
        """
        Constructor to initialize the DNAList
        :param gene: String of genes(DNA) to be
               initialized.
        :pre: A gene tring is given as parameter.
        :post: A DNAList consisting of gene string
        is created using DNA node class. Every character
        in the string is a single DNA node in the DNAList.
        """
        self.head = None
        self.tail = None
        self.gene = gene
        for i in range(len(gene)):
            if self.head == None:
                self.head = DNA(gene[i])
                self.tail = self.head
            else:
                self.tail.next_node = DNA(gene[i])
                self.tail = self.tail.next_node

    def append(self, item):
        """
        Appends the character(DNA) to existing DNAList.
        :param item: character to be appended
        :pre: A single character is given as a parameter.
        :post: Character is appended to DNAList if DNAList
        was not empty, otherwise new DNAList with single
        character is created.
        :return: none
        """
        if self.head == None:
            self.head = DNA(item)
            self.tail = self.head
        else:
            self.tail.next_node = DNA(item)
            self.tail = self.tail.next_node

    def join(self, other):
        """
        Joins the given DNAList to the back of
        our DNAList.
        :param other: DNAList to be joined
        :pre: 'other' is non-empty DNAList different
        from current list.
        :post: DNAList is modified with
        'other' joined at the end of our
        DNAList.
        :return: None
        """
        if self.head == None:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next_node = other.head
            self.tail = other.tail

    def count(self):
        """
        Helper function to count number of DNA nodes
        in our DNAList.
        :return: Number of DNA nodes.
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next_node
        return count

    def splice(self, ind, other):
        """
        Inserts(splices) the given DNAList 'other' after ind'th
        DNA node in existing list.
        :param ind: Index after which 'other' DNAList is to be
        spliced.
        :param other: DNAList to be spliced
        :pre: 'other' DNAList is not empty and 'other' is different
        from 'self'.
        :return:
        """
        current = self.head
        if ind > self.count():
            print("Index exceeds list size")
        else:
            for i in range(ind):
                current = current.next_node
            if current == None:
                self.head = other.head
                self.tail = other.tail
            elif current.next_node == None:
                current.next_node = other.head
                self.tail = other.tail
            else:
                other.tail.next_node = current.next_node
                current.next_node = other.head

    def copy(self):
        """
        Makes copy of current DNAList.
        :return: Returns the new DNAList with exactly same
        DNA nodes as that 'self'(current DNAList).
        """
        copy_list = ''
        current = self.head
        while current != None:
            copy_list += current.value
            current = current.next_node
        return DNAList(copy_list)

    def snip(self, i1, i2):
        """
        Deletes the nodes from index i1 until index
        (i2-1) from current DNAList.
        :param i1: Index from which nodes are deleted.
        :param i2: Index before which nodes are deleted.
        :return: None
        """
        cursor_before_i1 = self.head
        if i1 < 0 or i2 > self.count() + 1 or i1 > i2:
            raise Exception("Invalid Indices!")
        if i1 == 0 and i2 == self.count():
            self = DNAList()
        for i in range(i1 - 1):
            cursor_before_i1 = cursor_before_i1.next_node

        cursor_at_i2 = cursor_before_i1
        for i in range(i2 - (i1 - 1)):
            cursor_at_i2 = cursor_at_i2.next_node
        cursor_before_i1.next_node = cursor_at_i2

    def find(self, current, repstr, repstr1, counter=0):
        """
        Helper function to find given subsequence 'repstr' in
        the current DNAList.
        :param current: head of the current list
        :param repstr: subsequence to be found
        :param repstr1: subsequence to be found
        :param counter: counter to find index of subsequence
        repstr.
        :return: False if subsequence repstr is not found in the
        DNAList, otherwise final index repstr subsequence.
        """
        found = False
        if current != None:
            if current.value == repstr[0]:
                found = True
                if len(repstr) == 1:
                    return counter
                else:
                    found = self.find(current.next_node, repstr[1:], repstr1, counter + 1)
            else:
                found = self.find(current.next_node, repstr1, repstr1, counter + 1)
        return found

    def replace(self, repstr, other):
        """
        Finds the subsequence 'repstr' and replaces it
        with DNAList 'other', if subsequnce is not present
        it prints the message.
        :param repstr: subsequence to be found
        :param other: DNAList to replace subsequence
        :return: None
        """
        ind = self.find(self.head, repstr, repstr)
        if not ind:
            print("No such subsequence as", repstr)
        else:
            base_index = ind - len(repstr)
            end_index = ind + 1
            prev = self.head
            for i in range(base_index):
                prev = prev.next_node
            after = prev
            for i in range(end_index - 1):
                after = after.next_node

            prev.next_node = other.head
            other.tail.next_node = after

    def __str__(self):
        """
        Returns the DNA nodes in current list in Python
        list format to print function.
        :return:
        """
        result = '['
        pointer = self.head
        while pointer != None:
            if pointer.next_node == None:
                result += pointer.value
            else:
                result += pointer.value + ','
            pointer = pointer.next_node
        result += ']'
        return result
