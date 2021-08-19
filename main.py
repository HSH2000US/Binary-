# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.binary = str (input ("Enter a binary number "))
binary = binary [::-1]
listBin = list(binary.split())
while len(listBin) % 4 != 0:
    listBin.append('0')

def listToString(bin):
    str1 = ""
    for i in bin:
        str1 += i
    return str1
binary = listToString(listBin)

def convertBin(binary):
    val = 0
    for i in range (0, len(binary)):
        if binary[i] == "1":
            val += 2 ** i
    return val
print(convertBin(binary))





