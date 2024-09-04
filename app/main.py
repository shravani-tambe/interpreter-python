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
    
    with open(filename) as file:
        file_contents = file.read()
        
    error = False
    toks = []
    errs = []
    
    if file_contents:
        line_no = 1
        ptr = 0
        
        while ptr < len(file_contents):
            i = file_contents[ptr]
            char_name = " "
            if i == "(":
                print("LEFT_PAREN ( null")
                char_name = "LEFT_PAREN"
            elif i == ")":
                print("RIGHT_PAREN ) null")
                char_name = "RIGHT_PAREN"
            elif i == "{":
                print("LEFT_BRACE { null")
                char_name = "LEFT_BRACE"
            elif i == "}":
                print("RIGHT_BRACE } null")
                char_name = "RIGHT_BRACE"
            elif i  == "*": 
                print("STAR * null")
                char_name = "STAR"
            elif i == ".": 
                print("DOT . null")
                char_name = "DOT"
            elif i == ",": 
                print("COMMA , null")
                char_name = "COMMA"
            elif i == "+": 
                print("PLUS + null")
                char_name = "PLUS"
            elif i == "-": 
                print("MINUS - null")
                char_name = "MINUS"
            elif i == ";": 
                print("SEMICOLON ; null")
                char_name = "SEMICOLON"
            elif i == "=": 
                print("EQUAL = null")
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
            else:
                errs.append(f"[line {line_no}] Error: Unexpected character: {i}")
                error = True
                ptr += 1
                continue
            
            ptr += 1 
            toks.append(f"{char_name} {i} null")
        
        toks.append("EOF  null")
        print("\n".join(errs), file=sys.stderr)
        print("\n".join(toks))
    
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()