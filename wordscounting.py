#eg:1
word = input("enter a word:")  # Hello World
d1 = {}
#------------------------------step 1
for i in word:
    if i ==" ":
        i = "space"
        d1[i] = 1
    
    if i in d1:
        d1[i] += 1
        
    else:
        d1[i] = 1
print(d1)

















































































































































