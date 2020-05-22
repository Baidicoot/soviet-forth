import eval
import std
import requests
import json

ip = "http://localhost:80"

def getScope():
    r = requests.get(ip)
    if (r.status_code == 200):
        eval.ldScope(r.text)

def define(id, defn):
    eval.appendScope(id, defn)
    requests.post(ip, {"name":id, "defn":defn})

def run(input):
    ins = input.split()
    state = eval.State(ins)
    while True:
        getScope()
        try:
            output = []
            state.step(eval.scope, eval.ops, output)
            if (len(output) != 0):
                print(output[0])
        except Exception as err:
            if (err.args[0] == "define"):
                define(err.args[1], err.args[2])
            elif (err.args[0] != "program ends"):
                print(err.args[0])
                break
            else:
                break

while True:
    try:
        data = input("sov>")
        if (data == "exit"):
            break
    except KeyboardInterrupt:
        print("\ntype `exit` to exit")
        continue
    try:
        run(data)
    except KeyboardInterrupt:
        print("\nhalted")