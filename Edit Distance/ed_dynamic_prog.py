"""We can use memoization to reduce the number of calls to the function LD() 
and in turn reduce the time complexity of the code. The optimized code will
look like :"""

count=0
def LD(s, t , m , n, memo):
    global count
    count+=1
    if m == 0:
        return n
    if n == 0 :
        return m  
    if memo[m - 1][n - 1] != None :
        return memo[m - 1][n - 1]
    if s[m - 1] == t[n - 1]:
        memo[m - 1][n - 1] = LD(s, t,m-1,n-1,memo)
        return memo[m - 1][n - 1]

    memo[m-1][n-1] = 1+min([LD(s, t , m , n-1 ,memo),
                            LD(s, t , m-1 , n, memo), 
                            LD(s, t , m-1, n-1 ,memo)])
    return memo[m-1][n-1]

s1=raw_input("Enter string 1 : ")
s2=raw_input("Enter string 2 : ")
mem = [[None for i in range(1000)] for x in range(len(s1))]
print "The edit distance between "+s1+" and "+s2+" is :",LD(s1, s2 , len(s1), len(s2), mem)
print "The recursive function LD() was called "+str(count)+" times to find out the edit distance!"