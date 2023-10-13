cryptogram = "browoanoommnaon*"
pointer, compare = 0, 1
isSame = [0 for _ in range(len(cryptogram))]
answer = ""

while compare < len(cryptogram):
    while cryptogram[pointer] == cryptogram[compare]:
        isSame[pointer], isSame[compare] = 1, 1
        compare += 1
    if not isSame[pointer]: answer += cryptogram[pointer]
    pointer, compare = compare, compare+1

print(answer)
