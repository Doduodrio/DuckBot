import math

operators = {"^": 4, "*": 3, "/": 3, "%": 3, "+": 2, "-": 2}
functions = ["ceil", "floor", "abs", "factorial", "round", "sqrt", "log", "ln", "sin", "cos", "tan", "arcsin", "asin", "arccos", "acos", "arctan", "atan"]

def is_number(string):
    try:
        float(string)
        return True
    except:
        return False

def is_string(string):
    for letter in string:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True
  
def is_operator(string):
    return string in operators.keys()

def is_function(string):
    return string in functions

def is_greater(a, b):
    # compares the precedence of two operators
    return operators[a] > operators[b]

def top_of(stack):
    return stack[-1] if stack else None

def shunt_yard(expression: str):
    # Convert an expression into reverse Polish notation
    # with the shunting yard algorithm

    tokens = []
    stack = []
    output = []
    
    # strip spaces and then convert to tokens
    for i in "".join(expression.split()):
        if len(tokens)==0 and i in "abcdefghijklmnopqrstuvwxyz0123456789.()^*/%+-":
            tokens.append(i)
        elif is_number(i) or i == ".":
            if is_number(tokens[-1]) or tokens[-1] == ".":
                tokens[-1] += i
            else:
                tokens.append(i)
        elif is_string(i):
            if is_string(tokens[-1]):
                tokens[-1] += i
            else:
                tokens.append(i)
        elif i in "()" or is_operator(i):
            tokens.append(i)
        else:
            return [] # invalid character
    
    # combine negative signs with numbers
    j = 0
    while j+1<len(tokens):
        if tokens[j] == "-" and is_number(tokens[j+1]):
            tokens[j] += tokens[j+1]
            tokens.pop(j+1)
        j+=1
    
    # substitute special mathematical constants
    for i in range(len(tokens)):
        if i<len(tokens)-1:
            if tokens[i+1] == "(":
                continue
        if tokens[i] == "pi":
            tokens[i] = math.pi
        elif tokens[i] == "e":
            tokens[i] = math.e
        elif tokens[i] == "tau":
            tokens[i] = math.tau
        # purposely excluding math.inf and math.nan
    
    for token in tokens:
        if is_number(token):
            output.append(float(token))
        elif is_function(token):
            stack.append(token)
        elif is_operator(token):
            while not (top_of(stack) is None or top_of(stack) in "()") and is_greater(top_of(stack), token):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while not (top_of(stack) is None or top_of(stack) == "("):
                output.append(stack.pop())
            stack.pop()
        else:
            return
    while len(stack) > 0:
        output.append(stack.pop())
    return output

def evaluate(expression: str):
    # Evaluate an expression

    output = shunt_yard(expression)
    stack = []

    while len(output) > 0:
        if is_number(output[0]):
            stack.append(output.pop(0))
        elif is_operator(output[0]):
            a = stack.pop()
            b = stack.pop()
            op = output.pop(0)
            if op == "^":
                stack.append(b ** a)
            elif op == "*":
                stack.append(b * a)
            elif op == "/":
                try:
                    stack.append(b / a)
                except:
                    return
            elif op == "%":
                stack.append(b % a)
            elif op == "+":
                stack.append(b + a)
            elif op == "-":
                stack.append(b - a)
        elif is_function(output[0]):
            a = stack.pop()
            op = output.pop(0)
            if op == "ceil":
                stack.append(math.ceil(a))
            elif op == "floor":
                stack.append(math.floor(a))
            elif op == "abs":
                stack.append(abs(a))
            elif op == "factorial":
                stack.append(math.factorial(int(a)))
            elif op == "round":
                if a%1<0.5:
                    stack.append(math.floor(a))
                else:
                    stack.append(math.ceil(a))
            elif op == "sqrt":
                stack.append(math.sqrt(a))
            elif op == "log":
                stack.append(math.log(a, 10))
            elif op == "ln":
                stack.append(math.log(a))
            elif op == "sin":
                stack.append(math.sin(a))
            elif op == "cos":
                stack.append(math.cos(a))
            elif op == "tan":
                stack.append(math.tan(a))
            elif op in ["arcsin", "asin"]:
                stack.append(math.asin(a))
            elif op in ["arccos", "acos"]:
                stack.append(math.acos(a))
            elif op in ["arctan", "atan"]:
                stack.append(math.atan(a))
            else:
                return # mismatched parentheses error

    return stack[0] if stack else None