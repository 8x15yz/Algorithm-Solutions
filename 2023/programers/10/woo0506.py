forms = [ ["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nowm@email.com", "이제엠"] ]
result = set()

for i in range(len(forms)-1):
    for k in range(len(forms[i][1])-1):
        pntStr = forms[i][1][k]+forms[i][1][k+1]
        for j in range(i+1, len(forms)):
            for l in range(len(forms[j][1])-1):
                comStr = forms[j][1][l]+forms[j][1][l+1]
                if pntStr == comStr: 
                    result.add(forms[i][0])
                    result.add(forms[j][0])
                  
print(list(result))
                
