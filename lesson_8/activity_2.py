text = input("enter a string to reverse : ")
reverse= ""
for i in text:
    reverse = i + reverse
print("the reverse of entered text is : ",reverse)