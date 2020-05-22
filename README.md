# Soviet-Forth

## Builtins
Currently, very few builtins are defined, but you can easily define more in `std.py`.
- `:` - separate a function body from its name
- `;` - define a function (i.e. `'name : 'body`)
- `print` - print a symbol

## Running
To run, download `std.py`, `eval.py` and `client.py`. Run `python client.py`. Requires `requests`, and probably something else i've forgotten.

Make sure to change the ip in `client.py` to the server you want to connect to's ip. By default it is the main server at: `aidan-network.duckdns.org:80`. You can visit `http://aidan-network.duckdns.org/` to view the current scope.