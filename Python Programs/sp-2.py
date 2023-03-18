def currencycalc(inr,curr):
    if(curr=='euro'):
        Res=inr*0.01417
        print(Res)
    elif(curr=='British Pound'):
        Res=inr*0.0100
        print(Res)
    elif(curr=='Australian Dollar'):
        Res=inr*0.02140
        print(Res)
    elif(curr=='Canadian Dollar'):
        Res=inr*0.02027
        print(Res)
    else:
        print(-1)
n=int(input("Enter the amount you want in INR:"))
curr=input("Enter the currency you have:")
currencycalc(n,curr)

