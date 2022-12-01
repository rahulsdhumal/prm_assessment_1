lst = []
size=int(input("Enter the size of list : "))
for i in range(0,size):
    ele=input("Enter a Element : ")
    lst.append(ele)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i][-2]>lst[j][-2]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)