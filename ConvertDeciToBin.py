file=open("convert_deci_to_bin.txt",'w')
Num=int(input("Enter a Number: "))
file.write("Enter a Number: ")
file.write(str(Num))
file.write('\n')
abc=[]
while Num>0:
    temp=Num%2
    abc.append(temp)
    Num=int(Num/2)
abc.reverse()
file.write("The binary form: ")
for i in abc:
    file.write(str(i))
print(abc)