import inflect

numbers = inflect.engine()

silly_file = open("index.js", "a")

def peak(letter):
    if letter == "a":
        return "A"
    elif letter == "b":
        return "B"
    elif letter == "c":
        return "C"
    elif letter == "d":
        return "D"
    elif letter == "e":
        return "E"
    elif letter == "f":
        return "F"
    elif letter == "g":
        return "G"
    elif letter == "h":
        return "H"
    elif letter == "i":
        return "I"
    elif letter == "j":
        return "J"
    elif letter == "k":
        return "K"
    elif letter == "l":
        return "L"
    elif letter == "m":
        return "M"
    elif letter == "n":
        return "N"
    elif letter == "o":
        return "O"
    elif letter == "p":
        return "P"
    elif letter == "q":
        return "Q"
    elif letter == "r":
        return "R"
    elif letter == "s":
        return "S"
    elif letter == "t":
        return "T"
    elif letter == "u":
        return "U"
    elif letter == "v":
        return "V"
    elif letter == "w":
        return "W"
    elif letter == "x":
        return "X"
    elif letter == "y":
        return "Y"
    elif letter == "z":
        return "Z"


for i in range(375001, 390001):
    number_string = numbers.number_to_words(i)
    number_string = number_string.replace(", ", " ")
    number_string = number_string.replace(" and ", " ")

    number_string_cap = list(number_string)
    for b in range(len(number_string_cap) - 1, 0, -1):
        if number_string_cap[b] == " " or number_string_cap[b] == "-":
            number_string_cap[b + 1] = peak(number_string_cap[b + 1])
    number_string_cap[0] = peak(number_string_cap[0])
    number_string_cap = "".join(number_string_cap)

    final_string = '    else if(number === ' + str(i) + '|| number === "' + str(i) + '" || number === "' + number_string + '" || number === "' + number_string_cap + '" || number === "' + number_string.upper() + '") return true;\n'

    silly_file.write(final_string)

silly_file.close()


