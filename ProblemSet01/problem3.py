s = 'eaulvsncbnlkxronrpszz'
index=0
primarySubString = []
operatingSubString = []
#print("length:",len(s))
for x in range(0,len(s)):
    operatingSubString.append(s[index])
    if len(primarySubString) < len(operatingSubString):
        primarySubString = operatingSubString
    #print("primary :", ''.join(primarySubString))
    #print("operating :", ''.join(operatingSubString))
    if index<(len(s)-1):
        if s[index+1]>=s[index]:
            #print("Index Value:",index)
            index = index+1
            #print("primary 1st :",''.join(primarySubString))
            #print("operating 1st :",''.join(operatingSubString))


        else:
            if len(primarySubString)<len(operatingSubString):
                primarySubString = []
                primarySubString = operatingSubString
                operatingSubString = []

            else:
                operatingSubString = []
            index = index + 1


print("Longest substring in alphabetical order is:",''.join(primarySubString))



