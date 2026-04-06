def flames(n1:str,n2:str)->int:
    d1:dict[str,int] = {}
    d2:dict[str,int] = {}
    for i in range(len(n1)):
        d1[n1[i]] = d1.get(n1[i], 0) + 1
    for j in range(len(n2)):
        d2[n2[j]] = d2.get(n2[j], 0) + 1
    f = [abs(v1-v2) for k1,v1 in d1.items() for k2,v2 in d2.items() if k1==k2]
    return sum(f) if len(f) > 0 else 0
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames(name1, name2)
flames:dict[str,str] = {"F": "Friends", "L": "Lovers", "A": "Acquaintances", "M": "Married", "E": "Enemies", "S": "Single"}
print(f"The relationship between {name1} and {name2} is: {flames.get('FLAMES'[result % 6], 'Unknown')}")
buffer = input("Press Enter to exit...")