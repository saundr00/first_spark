"""DS"""
INPUT = "MCMXXXIV"

total = 0

for c in INPUT:
    match c:
        case "I":
            total += 1
        case "V":
            total += 5
        case "X":
            total += 10
        case "L":
            total += 50
        case "C":
            total += 100
        case "D":
            total += 500
        case "M":
            total += 1000

    if (c == "V" or c == "D") and prev_c == "I":
        total -= 2
    elif (c == "L" or c == "C") and prev_c == "X":
        total -= 20
    elif (c == "D" or c == "M") and prev_c == "C":
        total -= 200

    prev_c = c

print(total)
