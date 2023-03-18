n1=int(input("Enter the number of adults"))
n2=int(input("Enter the number of children"))
ta=n1*37550
tc=n2*(37550/3)
st=(ta+tc)*0.07
ft=ta+tc+st
dft=ft*0.1
ft=ft-dft
print("Total ticket cost:",ft)

