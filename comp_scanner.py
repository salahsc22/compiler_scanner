import re


KEYWORDS = [
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long",
    "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
    "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary",
    "_Noreturn", "_Static_assert", "_Thread_local"
]

OPERATORS = [
    r'\+\+', r'--', r'==', r'!=', r'>=', r'<=', r'->', r'\+=', r'-=', r'\*=', r'/=',
    r'%=', r'&=', r'\|=', r'\^=', r'<<=', r'>>=', r'\+', r'-', r'\*', r'/', r'%', r'!',
    r'~', r'&', r'\|', r'\^', r'<<', r'>>', r'=', r'<', r'>', r'\?'
]

PUNCTUATION = [
    r'\(', r'\)', r'\{', r'\}', r'\[', r'\]', r';', r',', r':', r'\.', r'\.\.\.'
]


token_patterns = {
    "KEYWORD": r'\b(' + '|'.join(KEYWORDS) + r')\b',
    "IDENTIFIER": r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
    "INTEGER": r'\b\d+\b',
    "FLOAT": r'\b\d+\.\d+([eE][-+]?\d+)?\b',
    "CHAR": r"'.?'",
    "STRING": r'"[^"\n]*"',
    "OPERATOR": '|'.join(OPERATORS),
    "PUNCTUATION": '|'.join(PUNCTUATION),
    "WHITESPACE": r'\s+',
    "UNKNOWN": r'.'
}


token_regex = re.compile('|'.join(f'(?P<{key}>{pattern})' for key, pattern in token_patterns.items()))

def scan_tokens(code):
    tokens = []
    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        
        if token_type != "WHITESPACE":
            tokens.append((token_type, token_value))
    
    return tokens

# Get C code input from the terminal --------------------------------------------------------------------------------------------------------------------------------
#                                           end input with a single line containing 'SCAN'
                                     


#-----------DONT forget to do this after entering your  c code in terminal-----------------------------------------------------------------------------------------------------------------------------------------------------------
print("Enter the C code to scan (end input with a single line containing 'SCAN'):")
code_lines = []
while True:
    line = input()
    if line.strip() == "SCAN":
        break
    code_lines.append(line)


c_code = "\n".join(code_lines)


print("\nTokens found in the C code:")
tokens = scan_tokens(c_code)
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")
