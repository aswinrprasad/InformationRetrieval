def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res

s1=raw_input("Enter string 1 : ")
s2=raw_input("Enter string 2 : ")
print "The edit distance between "+s1+" and "+s2+" is :",LD(s1, s2)