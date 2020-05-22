import json

scope = {}
ops = {}

def builtin(fn):
    global ops
    if (callable(fn)):
        ops[fn.__name__] = fn
        return fn
    elif (type(fn) is str):
        def internal(func):
            ops[fn] = func
        return internal

def appendScope(name, data):
    global scope
    scope[name] = data

def dumpScope():
    global scope
    return json.dumps(scope)

def ldScope(string):
    global scope
    scope = json.loads(string)

class Ins:
    def __init__(self, ins):
        self.ins = ins
        self.parent = None
    
    def nextIns(self):
        if (self.ins != []):
            return self.ins.pop(0)
        else:
            if self.parent is None:
                raise Exception('program ends')
            else:
                self.ins = self.parent.ins
                self.parent = self.parent.parent
    
    def call(self, ins):
        self.parent = self
        self.ins = ins

class State:
    def __init__(self, ins):
        self.stack = []
        self.ins = Ins(ins)
    
    def step(self, scope, ops, output):
        ins = self.ins.nextIns()
        if ins in ops:
            ops[ins](self, output)
        if ins in scope:
            self.ins.call(scope[ins])
        if ins[0] == '\'':
            self.stack.append(ins[1:])