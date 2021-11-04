n=int(input("entrer le nombre que vous voulez"))
compter = 0
while(n>0):
    compter+=1
    n=n//10
    print("le nombre de degte dans le nombre donnée sont:{compter}")