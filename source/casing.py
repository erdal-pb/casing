import inspect
import sys

def get_cases():
    fcts = dir(__import__(inspect.getmodulename(__file__)))
    return filter(lambda fct:fct.endswith("case"), fcts)

def detect(var):
    var_list = analyze(var)
    type = "unknow"
    for fct in get_cases():
        type = fct[:-len("case")]
        if transform(var, type) == var:
            break
    return type

def analyze(var):
    var_list = []
    buffer = ""
    for i, charact in enumerate(var):
        if charact in ["-", "_", " "]:
            var_list.append(buffer)
            buffer = ""
        elif charact in "abcdefghijklmnopqrstuvwxyz".upper():
            if i > 0 and var[i - 1].isupper():
                buffer += charact.lower()
            else:
                var_list.append(buffer)
                buffer = charact.lower()
        elif charact in "abcdefghijklmnopqrstuvwxyz":
            buffer += charact
    var_list.append(buffer)
    return list(filter(len, var_list))
    
def snake_case(var):  # some_variable
    return "_".join(var)
    
def snake_uppercase(var):  # SOME_VARIABLE
    return "_".join(var).upper()
    
def dash_case(var):  # some-variable
    return "-".join(var)
    
def dash_uppercase(var):  # SOME-VARIABLE
    return "-".join(var).upper()
    
def pascal_case(var):  # SomeVariable
    result = ""
    for element in var:
        element = list(element)
        element[0] = element[0].upper()
        result += "".join(element)
    return result
    
def camel_case(var):  # someVariable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        if i > 0:
            element[0] = element[0].upper()
        result += "".join(element)
    return result
    
def normal_case(var):  # some variable
    return " ".join(var)
    
def pretty_case(var):  # Some Variable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        element[0] = element[0].upper()
        result += "".join(element) + " "
    return result[:-1]
    
def sentence_case(var):  # Some variable
    result = ""
    for i, element in enumerate(var):
        element = list(element)
        if i == 0:
            element[0] = element[0].upper()
        result += "".join(element) + " "
    return result[:-1]
    
def normal_uppercase(var):  # SOME VARIABLE
    return " ".join(var).upper()
    
def attached_case(var):  # samevariable
    return "".join(var)
    
def attached_uppercase(var):  # SOMEVARIABLE
    return "".join(var).upper()

def reversed_case(var):  # some Variable
    result = list(pretty_case(var))
    result[0] = result[0].lower()
    return "".join(result)
    
def transform(var, type="snake"):
    function = "{0}case".format(type)
    print("function: " + str(function))
    for fct in dir(__import__(inspect.getmodulename(__file__))):
        if function == fct:
            return globals()[fct](analyze(var))
    else:
        raise Exception("Function '{0}' don't exists".format(function))

if __name__ == "__main__":
    for var in [
        "Some-Variable",
        "Some-_Variable",
        "SomeVariable",
        "SomeVariable"
    ]:
        print(transform(var, "sentence_"))