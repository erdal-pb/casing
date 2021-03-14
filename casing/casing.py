import inspect
import sys

separators = "-_ "
alphabet = "abcdefghijklmnopqrstuvwxyz"

def getcases():
    return filter(lambda fct:fct.endswith("case"), dir(__import__(inspect.getmodulename(__file__))))

def detect(var):
    var_list = analyze(var)
    type = "unknow"
    for fct in getcases():
        type = fct[:-len("case")]
        if transform(var, type) == var:
            break
    return type

def analyze(var):
    var_list = []
    buffer = ""
    for i, charact in enumerate(var):
        if charact in separators:
            var_list.append(buffer)
            buffer = ""
        elif charact in alphabet.upper():
            if i > 0 and var[i - 1].isupper():
                buffer += charact.lower()
            else:
                var_list.append(buffer)
                buffer = charact.lower()
        elif charact in alphabet:
            buffer += charact
    var_list.append(buffer)
    return list(filter(len, var_list))

def transform(var, type="snake"):
    for fct in dir(__import__(inspect.getmodulename(__file__))):
        if "{0}case".format(type) == fct:
            return globals()[fct](analyze(var))
    else:
        raise Exception("Function '{0}' don't exists".format(function))
    
def snakecase(var):  # some_variable
    return "_".join(var)
    
def snakeuppercase(var):  # SOME_VARIABLE
    return "_".join(var).upper()
    
def dashcase(var):  # some-variable
    return "-".join(var)
    
def dashuppercase(var):  # SOME-VARIABLE
    return "-".join(var).upper()
    
def pascalcase(var):  # SomeVariable
    result = ""
    for element in var:
        element = list(element)
        element[0] = element[0].upper()
        result += "".join(element)
    return result
    
def camelcase(var):  # someVariable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        if i > 0:
            element[0] = element[0].upper()
        result += "".join(element)
    return result
    
def normalcase(var):  # some variable
    return " ".join(var)
    
def prettycase(var):  # Some Variable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        element[0] = element[0].upper()
        result += "".join(element) + " "
    return result[:-1]
    
def sentencecase(var):  # Some variable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        if i == 0:
            element[0] = element[0].upper()
        result += "".join(element) + " "
    return result[:-1]
    
def normaluppercase(var):  # SOME VARIABLE
    return " ".join(var).upper()
    
def attachedcase(var):  # samevariable
    return "".join(var)
    
def attacheduppercase(var):  # SOMEVARIABLE
    return "".join(var).upper()

def reversedcase(var):  # some Variable
    result = list(prettycase(var))
    result[0] = result[0].lower()
    return "".join(result)

if __name__ == "__main__":
    print(list(getcases()))