"""
CSCI-603 PreTee Lab
Author: Sean Strout @ RIT CS
Author: Indrajeet Vidhate
Author: Shubham Patil

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import assignment_node  # assignment_node.AssignmentNode
import literal_node  # literal_node.LiteralNode
import math_node  # math_node.MathNode
import print_node  # print_node.PrintNode
import runtime_error  # runtime_error.RuntimeError
import syntax_error  # syntax_error.SyntaxError
import sys  # argv
import variable_node  # variable_node.VariableNode


class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees = []
        self.lineNum = 0
        self.syntaxError = False

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).

        :return: A root node for Parse tree formed for Current Expression Tree
        """

        operators = ['*', '//', '+', '-', '=']

        tree = []
        if len(tokens) > 1:
            tree = self.__parse(tokens[1:])

            if tokens[0].isidentifier():
                tree.append(variable_node.VariableNode(tokens[0], self.symTbl))
                return tree

            elif tokens[0].isdigit():
                tree.append(literal_node.LiteralNode(int(tokens[0])))
                return tree

            elif tokens[0] in operators:
                if len(tree) >= 2:
                    if tokens[0] == '=':
                        left = tree.pop()
                        if not isinstance(left, variable_node.VariableNode):
                            raise syntax_error.SyntaxError('Bad assignment expression')
                        right = tree.pop()
                        tree.append(assignment_node.AssignmentNode(left, right, self.symTbl, '='))
                        return tree

                    else:
                        left = tree.pop()
                        right = tree.pop()
                        tree.append(math_node.MathNode(left, right, tokens[0]))
                        return tree
                else:
                    raise syntax_error.SyntaxError('Incomplete Token List')
            else:

                raise syntax_error.SyntaxError("Bad Assignment Operator")

        elif len(tokens) == 1:
            if tokens[0].isdigit():

                tree.append(literal_node.LiteralNode(int(tokens[0])))
                return tree

            elif tokens[0].isidentifier():
                tree.append(variable_node.VariableNode(tokens[0], self.symTbl))
                return tree

            else:
                raise syntax_error.SyntaxError("Invalid Token " + tokens[0])

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        try:
            with open("srcFile.txt") as f:
                for line in f:

                    token_list = line.strip().split()

                    if not token_list:
                        self.lineNum += 1;


                    elif token_list[0] == '#':
                        self.lineNum += 1

                    elif token_list[0] == '=':
                        self.lineNum += 1
                        current_parse_tree = self.__parse(token_list)
                        node = current_parse_tree.pop()
                        try:
                            node.evaluate()
                        except runtime_error.RuntimeError as e:
                            print('*** Runtime error:', e)
                            sys.exit(1)
                        self.parseTrees.append(node)

                    elif token_list[0] == '@':

                        if len(token_list) > 1:
                            self.lineNum += 1
                            p = print_node.PrintNode(self.__parse(token_list[1:]).pop())
                            self.parseTrees.append(p)

                        elif len(token_list) == 1:
                            self.lineNum += 1
                            p = print_node.PrintNode(None)
                            self.parseTrees.append(p)

                        elif token_list[1] not in self.symTbl:
                            raise runtime_error.RuntimeError('Unrecognized variable  : ' + token_list[1])
                            sys.exit(1)

                    else:
                        self.lineNum += 1
                        raise syntax_error.SyntaxError("Invalid Token")
        except syntax_error.SyntaxError as e:
            self.syntaxError = True
            print("Error at line Number", str(self.lineNum))
            print(e)

    def emit(self):
        """
        Prints an infiex string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for item in self.parseTrees:
            print(item.emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """

        if not self.syntaxError:
            try:
                for item in self.parseTrees:
                    if isinstance(item, assignment_node.AssignmentNode) and item.token == '=':
                        print(item.variable.id + item.token + str(item.expression.evaluate()))
                    elif isinstance(item, print_node.PrintNode):
                        item.evaluate()
            except runtime_error.RuntimeError as e:
                raise e
        else:
            print(" Can not be Evaluated, syntax_error is Set !!")


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)


if __name__ == '__main__':
    main()
