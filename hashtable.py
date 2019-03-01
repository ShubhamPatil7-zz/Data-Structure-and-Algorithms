__author__ = 'zjb'
__author__ = 'IAV'
__author__ = 'SBP'

"""
CSCI-603 Computational Problem Solving
Author: Indrajeet Vidhate
Author: Shubham Patil
Lab 7
"""
import re
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    __slots__ = 'table', 'numkeys', 'cap', 'maxload', 'probes', 'collisions', 'hash_func', 'MAX_FREQ'

    def __init__(self, hash_func, initsz=100, maxload=0.7):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.probes = 0
        self.collisions = 0
        self.hash_func = hash_func
        self.MAX_FREQ = Entry(None, 0)

    def put(self, key):
        '''
        Adds the given (key) to the map, replacing entry with same key if present
        and calls helper function with count of the key(value).
        :param key: Key of new entry
        :return:
        '''
        if not self.contains(key):
            self.__put__(key)
        else:
            count = self.get(key)
            if count > self.MAX_FREQ[1]:
                self.MAX_FREQ = Entry(key, count + 1)
            self.__put__(key, count + 1)

    def __put__(self, key, value=1):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present
        and keeps track collisions, probes and most frequent word.
        :param key: Key of new entry
        :param value: Number of times key has been added
        '''
        index = self.hash_func(key) % self.cap
        if self.table[index] is not None and \
                        self.table[index] is not DELETED:
            self.collisions += 1
        self.probes += 1
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == len(self.table):
                index = 0
        self.probes += 1
        if self.table[index] is None:
            self.numkeys += 1
        self.probes += 1
        self.table[index] = Entry(key, value)
        if self.numkeys / self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.probes = 0
            self.collisions = 0
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.__put__(entry[0], entry[1])

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == self.cap:
                index = 0
        self.probes += 1
        return self.table[index] is not None

    # def hash_func(self,key):
    #     '''
    #     Not using Python's built in hash function here since we want to
    #     have repeatable testing...
    #     However it is terrible.
    #     Assumes keys have a len() though...
    #     :param key: Key to store
    #     :return: Hash value for that key
    #     '''
    #     # if we want to switch to Python's hash function, uncomment this:
    #     #return hash(key)
    #     return len(key)

    def get_collisions_and_probes(self):
        '''
        Returns total number of collisions and probes
        :return: number of collisions and probes
        '''
        return self.collisions, self.probes

    def get_most_frequent_word(self):
        '''
        Returns most frequent word with it's value(frequency)
        :return: Entry with Most frequent key.
        '''
        return self.MAX_FREQ


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def my_hash_1(key):
    '''
    Our own hash function which utilizes properties
    of prime numbers to return uniform values over
    long range.
    :param key: key to be hashed
    :return: hash value
    '''
    hash = 11
    p = 3
    q = 7
    r = 10 ** 9 + 7
    s = 10 ** 8 + 7
    for i in range(len(key)):
        if i % 2 == 0:
            hash += ord(key[i]) ** p % r
        else:
            hash += ord(key[i]) ** q % s
    return hash


def my_hash_2(key):
    '''
    Our own hash function which utilizes properties
    of prime numbers to return uniform values over
    long range.
    :param key: key to be hashed
    :return: hash value
    '''
    hash = 7
    primes = [2851, 641, 1597, 991, 331, 421]
    r = 10 ** 9 + 7
    s = 10 ** 8 + 7
    for i in range(len(key)):
        hash += ord(key[i]) * (17 ** i)
        hash *= primes[i * ord(key[i]) % len(primes)]

    return hash


def testMap(BOOK, HASHFUNCTION, LOADFACT):
    '''
    Test function
    :param BOOK: FileName
    :param HASHFUNCTION: Name of Hash Function
    :param LOADFACT: Max Loading Factor
    :return:
    '''
    print("File:", BOOK, "Hash Function:", str(HASHFUNCTION), "Maxload:", LOADFACT)
    map = Hashmap(HASHFUNCTION, initsz=50, maxload=LOADFACT)
    count = 0
    with open(BOOK, encoding="utf8") as dict:
        for lines in dict:
            list = re.split("\W+", lines)
            for i in range(len(list)):
                if list[i] is not '':
                    map.put(list[i])
                    count += 1
    a, b = map.get_collisions_and_probes()
    print("Number of Words in file :", count)
    print("Collisions :", a)
    print("Probes :", b)
    max_word = str(map.get_most_frequent_word())
    print("Word with maximum frequency is :\n" + max_word + "\n")


def main():
    '''
    We call the Hashmap with 3 files, 3 hash functions
    and 3 load factors, so total 27 combinations.
    :return:
    '''
    DICTIONARY = ['words', 'Novel1.txt', 'Novel2.txt']
    HASHES = [hash, my_hash_1, my_hash_2]
    MAXLOAD = [0.65, 0.70, 0.75]

    for book in DICTIONARY:
        for function in HASHES:
            for load in MAXLOAD:
                testMap(book, function, load)


if __name__ == '__main__':
    main()
