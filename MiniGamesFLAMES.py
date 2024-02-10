n1=input("Enter the first name: ")
n2=input("Enter the Second name: ")
s=['f','l','a','m','e','s']
my_l={
    'f':"Friends",
    "l":"Loves",
    "a":"Affection",
    "m":"Marries",
    "e":"Enemys",
    "s":"Siblings"
}
def Unqcount(n1,n2):
    n1, n2 = list(n1.lower()), list(n2.lower())
    for i in n1:
        for j in n2:
            if i == j:
                n1.remove(i)
                n2.remove(j)
                break
    sum = len(n1) + len(n2)
    return sum

def findflames(s,n):
    while len(s)>1:
        j=-1
        for i in range(n):
            j=j+1
            if j>len(s)-1:
                j=0

        m=s[:j]
        s.pop(j)
        m=s[j:]+m
        s=m

    return s

#driver code
res=findflames(s,Unqcount(n1,n2))
print(n1+ " And "+ n2+" Are "+my_l[res[0]])


