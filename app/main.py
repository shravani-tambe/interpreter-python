import sys

def main():
    print("Logs from your program will appear here!", file=sys.stderr)
    
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)
    
    command = sys.argv[1] 
    filename = sys.argv[2] 
    
    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    
    try:
        with open(filename) as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        exit(1)
    
    error = False
    toks = []
    errs = []
    
    if file_contents:
        line_no = 1
        ptr = 0
        
        while ptr < len(file_contents):
            i = file_contents[ptr]
            char_name = None  
            
            if i == "(":
                char_name = "LEFT_PAREN"
            elif i == ")":
                char_name = "RIGHT_PAREN"
            elif i == "{":
                char_name = "LEFT_BRACE"
            elif i == "}":
                char_name = "RIGHT_BRACE"
            elif i == "*": 
                char_name = "STAR"
            elif i == ".": 
                char_name = "DOT"
            elif i == ",": 
                char_name = "COMMA"
            elif i == "+": 
                char_name = "PLUS"
            elif i == "-": 
                char_name = "MINUS"
            elif i == ";": 
                char_name = "SEMICOLON"
            elif i == "=": 
                if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == "=":
                    char_name = "EQUAL_EQUAL"
                    i = "=="  
                    ptr += 1  
                else:
                    char_name = "EQUAL"
            elif i == "\n":
                line_no += 1
                ptr += 1  
                continue
            elif i.isspace():
                ptr += 1
                continue
            else:
                errs.append(f"[line {line_no}] Error: Unexpected character: {i}")
                error = True
                ptr += 1
                continue
            
            if char_name:  
                toks.append(f"{char_name} {i} null")
            ptr += 1 
        
        toks.append("EOF  null")  
    
    else:
        toks.append("EOF  null")
    
    print("\n".join(toks))  
    
    if errs:
        print("\n".join(errs), file=sys.stderr)
    
    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
