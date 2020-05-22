import eval

class UnitType(eval.Type):
    def __init__(self):
        self.type = "unit"

def assertType(obj, string):
    if (obj.type != string):
        raise Exception("typeerror")