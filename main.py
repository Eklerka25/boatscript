TOKEN_SUBTYPE_OPERATORS = {
    "=": "SET"
}

TOKEN_SUBTYPE_KEYWORDS = {
    "int": "KEYWORD_INT"
}

TOKEN_TYPE_SEMICOLON = "SCOL"
TOKEN_TYPE_INT = "INT"

data = "int x = 10;"

t = list(data)

lexed_data = {}
string_mode = False
token_int = 1

for x in range(len(t)):
    if t[x] == " ":
        token_int += 1
    elif t[x] == ";":
        token_int = 0;
    else:
        lexed_data.setdefault(token_int, "")
        lexed_data[token_int] += t[x]

print(lexed_data)
