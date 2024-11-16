operators = {"^": 4, "*": 3, "/": 3, "%": 3, "+": 2, "-": 2}

def is_number(string):
    try:
        float(string)
        return True
    except:
        return False
  
def is_operator(string):
    return string in operators.keys()

def is_greater(a, b):
    # compares the precedence of the two operators
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
        if len(tokens)==0 and i in "0123456789.()^*/%+-":
            tokens.append(i)
        elif is_number(i) or i == ".":
            if is_number(tokens[-1]) or tokens[-1] == ".":
                tokens[-1] += i
            else:
                tokens.append(i)
        elif i in "()" or is_operator(i):
            tokens.append(i)
        else:
            return []
    
    # combine negative signs with numbers
    i = 0
    while i+1<len(tokens):
        if tokens[i] == "-" and is_number(tokens[i+1]):
            tokens[i] += tokens[i+1]
            tokens.pop(i+1)
        i+=1

    for thing in tokens:
        if is_number(thing):
            output.append(float(thing))
        elif is_operator(thing):
            while not (top_of(stack) == None or top_of(stack) in "()") and is_greater(top_of(stack), thing):
                output.append(stack.pop())
            stack.append(thing)
        elif thing == "(":
            stack.append(thing)
        elif thing == ")":
            while not (top_of(stack) == None or top_of(stack) == "("):
                output.append(stack.pop())
            stack.pop()
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
            opr = output.pop(0)
            if opr == "^":
                stack.append(b ** a)
            elif opr == "*":
                stack.append(b * a)
            elif opr == "/":
                try:
                    stack.append(b / a)
                except:
                    return
            elif opr == "%":
                stack.append(b % a)
            elif opr == "+":
                stack.append(b + a)
            elif opr == "-":
                stack.append(b - a)

    return stack[0] if stack else None