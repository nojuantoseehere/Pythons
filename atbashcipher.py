
atbashCipher={
    "a":"z",
    "b":"y",
    "c":"x",
    "d":"w",
    "e":"v",
    "f":"u",
    "g":"t",
    "h":"s",
    "i":"r",
    "j":"q",
    "k":"p",
    "l":"o",
    "m":"n",
    "n":"m",
    "o":"l",
    "p":"k",
    "q":"j",
    "r":"i",
    "s":"h",
    "t":"g",
    "u":"f",
    "v":"e",
    "w":"d",
    "x":"c",
    "y":"b",
    "z":"a"
}
normalTxt=input("Enter your Word: ")
count = 0

for i in normalTxt:
    if i in atbashCipher:
        ciphered = atbashCipher[i]
        print(ciphered, end="")
        
        count += 1

        if count % 5 == 0:
            print(" ", end="")
    else:
        print(i, end="")