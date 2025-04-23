# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for x in tokens:
            if x.lstrip('-').isdigit():
                stack.append(int(x))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if x == "+":
                    stack.append(num1 + num2)
                elif x == "-":
                    stack.append(num1 - num2)
                elif x == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num1) / float(num2)))

        return stack[0]