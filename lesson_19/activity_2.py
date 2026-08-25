def pal(tup):
    e = len(tup)-1
    s = 0
    while s<e:
        if (tup[s]!=tup[e]):
            return False
        s = s + 1
        e = e - 1
        return True

my_tup = (1,2,3,4,1)
if pal(my_tup):
    print("The tuple is a palindrome")
else:
    print("the tuple is not a plaindrome")