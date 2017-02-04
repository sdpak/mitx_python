s = 'boobhoboobooboobtobooobobbobbbobob'
x = 0
y = 3
bobCount = 0
print(len(s))
for w in range(0,len(s)-2):
    print(s[x:y])
    if s[x:y] == "bob":
        bobCount = bobCount+1
    x = x+1
    y = y+1

print("Number of times bob occurs is:",bobCount)
