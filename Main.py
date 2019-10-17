class Operator:

    def __init__(self, id):
        self.id = id
        self.precedence = self.getPrecedence(id)

    @staticmethod
    def getPrecedence(id):

        if id == "+" or id == "-":
            return 0

        if id == "*" or id == "/":
            return 1

        if id == "^":
            return 2

        if id == '(' or id == ')':
            return 100


class Calculator:

    def __init__(self):
        self._operatorStack = []
        self._inFix = None
        self._postFix = []

    def process(self, arr):
        """

        Args:
            arr: input array of strings

        Returns:
            none, processes the string into a postfix expression

        """
        self._inFix = ' '.join(arr)
        for i in arr:
            if self.isNumber(i):
                self._postFix.append(i)
            else:
                op = Operator(i)

                # if new operator has smaller precedence than top, pop the top and push into postfix
                while len(self._operatorStack) > 0 and op.precedence < self._operatorStack[-1].precedence:
                    self._postFix.append(self._operatorStack.pop().id)
                self._operatorStack.append(op)

        while len(self._operatorStack) > 0:
            self._postFix.append(self._operatorStack.pop().id)

    @staticmethod
    def isNumber(a):
        try:
            float(a)
            return True
        except ValueError:
            return False

    def inFix(self):
        return self._inFix

    def postFix(self):
        return self._postFix


def main():

    calc = Calculator()
    string = "1 + 2 * 5 - 3 * 2".split(' ')
    calc.process(string)
    print(calc.inFix())
    print(calc.postFix())


if __name__ == "__main__":
    main()