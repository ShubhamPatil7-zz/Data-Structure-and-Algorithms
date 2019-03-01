__author__ = 'IAV'
__author__ = 'SBP'

"""
CSCI-603 Computational Problem Solving
Author: Indrajeet Vidhate
Author: Shubham Patil
Lab 6
"""

from dnalist import DNAList


class GeneTester:
    """
    Tester Class to try all functions defined in
    DNAList. We are passing list ABC as starting
    DNAList and performing all operations on the
    same list in sequential manner.
    """

    def test_append(self, list):
        """
        Test function for 'append'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting Append:")
        print("List before operation")
        print(list)
        print("Appending D to ABC")
        list.append('D')
        print(list)

    def test_join(self, list):
        """
        Test function for 'join'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting join:")
        print("List before operation")
        print(list)
        print("Joining EF and then GH to ABCD")
        list.join(DNAList('EF'))
        list.join(DNAList('GH'))
        print(list)

    def test_splice(self, list):
        """
        Test function for 'splice'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting Splice:")
        print("List before operation")
        print(list)
        print("Splicing XY after ABC")
        list.splice(2, DNAList('XY'))
        print(list)

    def test_snip(self, list):
        """
        Test function for 'snip'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting Snip:")
        print("List before operation")
        print(list)
        print("Snipping XY")
        list.snip(3, 5)
        print(list)

    def test_replace(self, list):
        """
        Test function for 'replace'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting Replace:")
        print("List before operation")
        print(list)
        print("Replacing CD with MN")
        list.replace('CD', DNAList('MN'))
        print(list)

    def test_copy(self, list):
        """
        Test function for 'copy'.
        :param list: DNAlist to be modified
        :return:
        """
        print("\nTesting Copy:")
        print("List before operation")
        print(list)
        print("Copied List")
        print(list.copy())


def main(self):
    """
    Main function
    :param self:
    :return:
    """
    genelist = DNAList('ABC')
    tester = GeneTester()
    tester.test_append(genelist)
    tester.test_join(genelist)
    tester.test_splice(genelist)
    tester.test_snip(genelist)
    tester.test_replace(genelist)
    tester.test_copy(genelist)


if __name__ == '__main__':
    main(str)
