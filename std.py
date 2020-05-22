import eval
from stdtype import *

@eval.builtin("print")
def log(state, output):
    item = state.stack.pop()
    if (hasattr(item, 'log')):
        output.append(item.log)
    else:
        raise Exception("typeerror")

@eval.builtin(";")
def defn(state, output):
    definition = []

    item = state.stack.pop()
    assertType(item, "symbol")

    while (item.type == "symbol"):
        definition.insert(0, item.log)
        item = state.stack.pop()
    
    assertType(item, "unit")

    item = state.stack.pop()
    assertType(item, "symbol")

    raise Exception("define", item.log, definition)

@eval.builtin(":")
def sep(state, output):
    state.stack.append(UnitType())