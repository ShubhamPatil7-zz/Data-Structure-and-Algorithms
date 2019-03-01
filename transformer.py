__author__ = 'IAV'
__author__ = 'SBP'

"""
CSCI-603 Computational Problem Solving
Author: Indrajeet Vidhate
Author: Shubham Patil

This function encrypts and decrypts the input message and 
transformation file according to users input.
"""


def Si(message, i):
    """
    This functions shifts a letter at i'th index by 1 forward.
    :param message: word to be encrypted
    :param i: index i in 'message'
    :return: encrypted message with forward shift
    """
    message_list = list(message)
    message_list[i] = chr(ord('A') + (((ord(message[i])) % ord('A')) + 1) % 26)
    message = "".join(message_list)
    return message


def Sik(message, i, k):
    """
    This functions shifts a letter at i'th index by 'k'.
    :param message: wo
    :param message: word to be encrypted
    :param i: index i in 'message'
    :param k: number of shifts
    :return: encrypted message with shift depending on sign of k.
    """
    message_list = list(message)
    message_list[i] = chr(65 + (((ord(message[i]) % ord('A')) + k) % 26))
    message = "".join(message_list)
    return message


def DSik(message, i, k):
    """
    This functions shifts a letter at i'th index by 'k'.
    :param message: wo
    :param message: word to be encrypted
    :param i: index i in 'message'
    :param k: number of shifts
    :return: decrypted message with shift depending on sign of inverted k.
    """
    message_list = list(message)
    message_list[i] = chr(ord('A') + ((26 + ((ord(message_list[i]) % ord('A')) - k)) % 26))
    message = "".join(message_list)
    return message


def R(message):
    """
    Rotates the last character forward by 1.
    :param message: word to be encrypted
    :return: encrypted message
    """
    message = message[-1] + message[0:len(message) - 1]
    return message


def Ri(message, exponent):
    """
    Rotates the group of characters of length exponent forward
    or backward depending on sign and magnitude.
    :param message: word to be encrypted/decrypted
    :param exponent: length of character group to be shifted
    :return: encrypted message with shifts
    """
    if exponent > 0:
        message = message[len(message) - exponent:len(message)] + message[0:len(message) - exponent]
        return message
    elif exponent < 0:
        exponent *= -1
        message = message[exponent:] + message[0:exponent]
        return message


def Di(message, i):
    """
    Duplicates letter at index i
    :param message: word to be encrypted
    :param i: index i in 'message'
    :return: encrypted message
    """
    message_list = list(message)
    message_list[i] = message[i] * 2
    message = "".join(message_list)
    return message


def Dik(message, i, k):
    """
    multiplies letter at index i by k times
    :param message: word to be encrypted
    :param i: index i in 'message'
    :param k: duplication factor
    :return: encrypted message
    """
    message_list = list(message)
    message_list[i] = message[i] * k
    message = "".join(message_list)
    return message


def Tij(message, i, j):
    """
    swaps the i'th letter with j'th letter
    :param message: word to be encrypted/decrypted
    :param i: index i in 'message'
    :param j: index j in 'message'
    :return: encrypted/decrypted message
    """
    message_list = list(message)
    message_list[i], message_list[j] = message_list[j], message_list[i]
    message = "".join(message_list)
    return message


def Tgij(message, g, i, j):
    """
    divides the word g partitions and swaps
    i'th partition with j'th partition
    :param message: word to be encrypted
    :param g: number of partitions
    :param i: i'th partition after g divisions
    :param j: j'th partition after g divisions
    :return:
    """
    message_list = list(message)
    length = len(message)
    if len(message) % 2 != 0:
        length = len(message) + 1
    upper = int(length / g)
    step = upper
    initial = 0
    divided_list = [0] * g
    for k in range(g):
        if k == g - 1:
            divided_list[k] = "".join((message_list[initial:len(message)]))
            break
        divided_list[k] = "".join((message_list[initial:upper]))
        initial = upper
        upper += step

    divided_list[i], divided_list[j] = divided_list[j], divided_list[i]
    return message


def BS(message, i, extension):
    """
    Shifts the all occurrences of letter at i'th index
    by 'extension' times forward.
    :param message: word to be encrypted
    :param i: index in message
    :param extension: number of shifts
    :return: encrypted message
    """
    initial = 0
    a = 0
    message_list = list(message)
    c = message_list[i]
    while (not initial >= len(message) - 1) and (not a == -1):
        a = message.find(c, initial, len(message))

        if not a == -1:
            message_list[a] = chr(65 + (((ord(message[a])) % ord('A')) + extension) % 26)
        initial = a + 1
    message = "".join(message_list)
    return message


def DBS(message, i, extension):
    """
    Shifts the all occurrences of letter at i'th index
    by 'extension' times backward.
    :param message: word to be encrypted
    :param i: index in message
    :param extension: number of shifts
    :return: decrypted message
    """
    message_list = list(message)
    a = 0
    initial = 0
    c = message_list[i]

    while (not initial >= len(message) - 1) and (not a == -1):
        a = message.find(c, initial, len(message) + 1)
        if not a == -1:
            message_list[a] = chr(ord('A') + ((26 + ((ord(message[a]) % ord('A')) - extension)) % 26))
        initial = a + 1
    decrypted = "".join(message_list)
    return decrypted


def encrypt():
    """
    Reads the input files from user and encrypts them.
    :return:
    """
    message_file = input("Enter message file name with "
                         "format(eg. message.txt)\n")
    transformation_file = input("Enter transformation file name "
                                "with format(eg transformations.txt)\n")
    with open(message_file) as m, open(transformation_file) as t:
        for msg, trns in zip(m, t):
            message = msg.strip()
            transformation = trns.strip()
            print("Original message is : ", message)
            transformation_list = transformation.split(';')

            for i in range(len(transformation_list)):
                single = transformation_list[i].split(',')
                if single[0].startswith('S'):
                    if len(single) == 1:
                        message = Si(message, int(single[0][1:]))
                    elif len(single) == 2:
                        message = Sik(message, int(single[0][1:]), int(single[1][0:]))

                if single[0].startswith('R'):
                    if len(str(single[0])) > 1:
                        message = Ri(message, int(single[0][1:]))
                    else:
                        message = R(message)

                if single[0].startswith('D'):
                    if len(single) == 1:
                        message = Di(message, int(single[0][1:]))
                    else:
                        message = Dik(message, int(single[0][1:]), int(single[1][0:]))

                if single[0].startswith('T'):
                    if str(single[0]).__contains__('('):
                        g = int(single[0][(single[0].index('(')) + 1: single[0].index(')')])
                        i = int(single[0][(single[0].index(')') + 1):])
                        j = int(single[1][0:])
                        message = Tgij(message, g, i, j)
                    else:
                        message = Tij(message, int(single[0][1:]), int(single[1][0:]))

                if single[0].startswith('B'):
                    message = BS(message, int(single[0][2:]), int(single[1][0:]))
            print("Encrypted message is :", message)


def decrypt():
    """
    Reads the input files from user and decrypts them by
    reversing transformations for encryption.
    :return:
    """
    message_file = input("Enter message file name with "
                         "format(eg. message.txt)\n")
    transformation_file = input("Enter transformation file name "
                                "with format(eg transformations.txt)\n")
    with open(message_file) as m, open(transformation_file) as t:
        for msg, trns in zip(m, t):
            message = msg.strip()
            transformation = trns.strip()
            print("Original message is : ", message)
            transformation_list = transformation.split(';')
            transformation_list.reverse()

            for i in range(len(transformation_list)):
                single = transformation_list[i].split(',')
                if single[0].startswith('S'):
                    if len(single) == 1:
                        message = DSik(message, int(single[0][1:]), 1)
                    elif len(single) == 2:
                        message = DSik(message, int(single[0][1:]), int(single[1][0:]))

                if single[0].startswith('R'):
                    if len(str(single[0])) >= 2:
                        message = Ri(message, -1 * int(single[0][1:]))
                    else:
                        message = Ri(message, -1)

                if single[0].startswith('D'):
                    print("Sorry decryption not possible for operation D")
                    break

                if single[0].startswith('T'):
                    if str(single[0]).__contains__('('):
                        g = int(single[0][(single[0].index('(')) + 1: single[0].index(')')])
                        i = int(single[0][(single[0].index(')') + 1):])
                        j = int(single[1][0:])
                        message = Tgij(message, g, j, i)
                    else:
                        message = Tij(message, int(single[1][0:]), int(single[0][1:]))
                if single[0].startswith('B'):
                    message = DBS(message, int(single[0][2:]), int(single[1][0:]))
            print("Decrypted message is :", message)


def main():
    """
    Main function, asks the user for encryption or decryption
    :return:
    """
    answer = input("You want to Encrypt or Decrypt?\tE/D\n")
    if answer == 'E' or answer == 'e':
        encrypt()
    elif answer == 'D' or answer == 'd':
        decrypt()
    else:
        print("Please enter E or D")


if __name__ == '__main__':
    main()