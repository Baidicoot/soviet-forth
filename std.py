import eval

@eval.builtin("print")
def log(state, output):
    string = state.stack.pop()
    output.append(string)

@eval.builtin(";")
def defn(state, output):
    definition = []
    word = state.stack.pop()
    while (word != "|"):
        definition.append(word)
        word = state.stack.pop()
    word = state.stack.pop()
    raise Exception("define", word, definition)

@eval.builtin(":")
def sep(state, output):
    state.stack.append("|")