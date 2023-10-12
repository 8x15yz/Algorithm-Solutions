cryptogram = "browoanoommnaon "
pointer, compare = 0, 1
answer = ""

while compare < len(cryptogram):
    print(cryptogram[pointer], cryptogram[compare])
    if cryptogram[pointer] == cryptogram[compare]:
        while cryptogram[pointer] == cryptogram[compare]:
            print(pointer, compare, "*")
            if compare == len(cryptogram): break
            compare += 1
        pointer, compare = compare, compare + 1
        continue
    else: 
        if compare == len(cryptogram): break
        if (cryptogram[pointer] != cryptogram[compare]):
            answer += cryptogram[pointer]
    
    
    
print(answer)
