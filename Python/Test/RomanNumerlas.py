#Input = int(input())


def NumtoRoman(Input):

    M, D, C, L, X, V, I = 0, 0, 0, 0, 0, 0, 0

    while Input > 0:
        while Input >= 1000:
            Input -= 1000
            M += 1
        while Input >= 500:
            Input -= 500
            D += 1
        while Input >= 100:
            Input -= 100
            C += 1
        while Input >= 50:
            Input -= 50
            L += 1
        while Input >= 10:
            Input -= 10
            X += 1
        while Input >= 5:
            Input -= 5
            V += 1
        while Input >= 1:
            Input -= 1
            I += 1

    RawOutput = []
    for letter in ("M"*M + "D"*D + "C"*C + "L"*L + "X"*X + "V"*V + "I"*I):
        RawOutput.append(letter)
    # print(RawOutput)
    return RawOutput


def Simplifier(RawOutput):
    Input = RawOutput
    for x in range(len(Input)):
        if x < len(Input)-1:
            if Input[x] == Input[x+1]:
                if x <= len(Input) - 4:
                    if Input[x] == Input[x+2] and Input[x] == Input[x+3]:
                        
                        match Input[x]:
                            case "D":
                                Input[x+1] = "M"
                            case "C":
                                Input[x+1] = "D"
                            case "X":
                                Input[x+1] = "C"
                            case "V":
                                Input[x+1] = "X"
                            case "I":
                                Input[x+1] = "V"
                        
                        Input.pop(x+3) and Input.pop(x+2)
                        #print(x)
                        #print(RawOutput)
                        #print(Input)
                     
    Output = Input
    return Output

def listToString(Input):
 
    # initialize an empty string
    Output = ""
 
    # traverse in the string
    for x in Input:
        Output += x
 
    # return string
    return Output

def ToRoman(Input):
    return(listToString(Simplifier(NumtoRoman(Input))))

Bigger = 0
Smaller = 0

for x in range(1,3999):
    if len(ToRoman(x)) > len(str(x)):
        Bigger += 1
    if len(ToRoman(x)) < len(str(x)):
        Smaller += 1

print("Bigger =", Bigger)
print("Smaller =", Smaller)