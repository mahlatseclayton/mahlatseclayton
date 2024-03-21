lis=list()
while True:
    nam=input()
    if nam != '###' :
            lis.append(nam)
    else:
        break
lik=lis[-1::-1]
for i in range(len(lik)):
    print(lik[i])