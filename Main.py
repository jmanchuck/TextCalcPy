class Operator:

    def __init__(self, id):
        self.id = id
        self.precedence = self.getPrecedence(id)

    def __str__(self):
        return self.id

    @staticmethod
    def getPrecedence(id):

        if id == "+" or id == "-":
            return 0
        if id == "*" or id == "/":
            return 1
        if id == "^":
            return 2
        if id == "(" or id == ")":
            return 3

    # changes a plus operator to minus, minus operator to plus, otherwise does nothing
    def reverse(self):
        if self.id == "+":
            self.id = "-"
        elif self.id == "-":
            self.id = "+"

    def operate(self, first_num, second_num):

        if self.id == "+":
            return first_num + second_num
        elif self.id == "-":
            return first_num - second_num
        elif self.id == "*":
            return first_num * second_num
        elif self.id == "/":
            return first_num / second_num
        elif self.id == "^":
            return first_num ** second_num
        else:
            raise


class Calculator:

    def __init__(self):
        self._operatorStack = []
        self._inFix = None
        self._postFix = []
        self.answer = None

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

                # add open parenth to operator stack
                if op.id == "(":
                    self._operatorStack.append(op)

                # pop operators until corresponding open parenth is found
                elif op.id == ")":
                    while len(self._operatorStack) > 0 and self._operatorStack[-1].id != "(":
                        self._postFix.append(self._operatorStack.pop())
                    self._operatorStack.pop()
                else:
                    # if new operator has smaller precedence than top, pop the top and push into postfix
                    while len(self._operatorStack) > 0 and op.precedence < self._operatorStack[-1].precedence and self._operatorStack[-1].id != "(":
                        self._postFix.append(self._operatorStack.pop())
                    self._operatorStack.append(op)

        while len(self._operatorStack) > 0:
            if self._operatorStack[-1].id == "-" and not self.isNumber(self._postFix[-1]):
                self._postFix[-1].reverse()
            self._postFix.append(self._operatorStack.pop())

    @staticmethod
    def isNumber(a):
        try:
            float(a)
            return True
        except (ValueError, TypeError) as e:
            return False

    def inFix(self):
        return self._inFix

    def postFix(self):
        a = []
        for i in self._postFix:
            if self.isNumber(i):
                a.append(i)
            else:
                a.append(i.id)
        return a

    def evaluate(self):
        answer = []

        for i in self._postFix:
            print(answer)
            if self.isNumber(i):
                answer.append(int(i))
            else:
                num_second = answer.pop()
                num_first = answer.pop()
                answer.append(i.operate(num_first, num_second))

        self.answer = answer[0]
        return answer[0]


def main():

    calc = Calculator()
    string = "( 9 + 3 ) / 3 - 8 / 2 - 2 * 3".split(' ')
    calc.process(string)
    print(calc.inFix())
    print(calc.postFix())
    print(calc.inFix(), '=', calc.evaluate())


def precedenceTest():

    calc = Calculator()
    string = "5 - 2 * 4 + 3 + 10 / 2 - 5".split(' ')
    calc.process(string)
    print(calc.inFix(), '=', calc.evaluate())
    assert calc.answer == 0


def parenthTest():

    calc = Calculator()
    string = "( 5 + 2 ) / 7 - ( 10 / 2 ) + 2 ^ 2".split(' ')
    calc.process(string)
    print(calc.inFix(), '=', calc.evaluate())
    assert calc.answer == 0

if __name__ == "__main__":
    parenthTest()