TOKEN_SUBTYPE_OPERATORS = {
    "=": "SET"
}

TOKEN_SUBTYPE_KEYWORDS = {
    "int": "KEYWORD_INT"
}

TOKEN_TYPE_SEMICOLON = "SCOL"
TOKEN_TYPE_INT = "INT"

TOKEB_TYPE_VAR = "VAR"

data = "int x = 10;"

t = list(data)

lexed_data = {}
string_mode = False
token_int = 1

def classify(token):
    if token in TOKEN_SUBTYPE_KEYWORDS:
        return TOKEN_SUBTYPE_KEYWORDS[token]
    elif token in TOKEN_SUBTYPE_OPERATORS:
        return TOKEN_SUBTYPE_OPERATORS[token]
    elif isinstance(token, int) or (isinstance(token, str) and token.lstrip('+-').isdigit()):
        return TOKEN_TYPE_INT
    else:
        return TOKEB_TYPE_VAR

for x in range(len(t)):
    if t[x] == " ":
        token_int += 1
    elif t[x] == ";":
        token_int = 0;
    else:
        lexed_data.setdefault(token_int, "")
        lexed_data[token_int] += t[x]

for y in range(len(lexed_data)):
    current_token = lexed_data[y + 1]
    lexed_data[y + 1] = {current_token : classify(current_token)}

print(lexed_data)
