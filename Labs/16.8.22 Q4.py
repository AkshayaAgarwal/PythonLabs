#1.
def birthdate(dic_1,name):
    for key, value in dic_1.items():
        if (key == name):
            print(value)
            break
        elif (key == 'Hardik Pandya'):
            print("Player not found")
dic_1 = {
    'Virat Kohli': '5  November  1988',
    'Umesh Yadav': '25  October 1987',
    'Manish Pandey': '10  September  1989',
    'Rohit Sharma': '30 April  1987',
    'Ravindra Jadeja': '6  December  1988',
    'Hardik Pandya': '11  October  1993'
}
name = input("Enter the name of the player : ")
birthdate(dic_1,name)
#2.


s=("""I bought a new laptop for $3.5k. The medel was recommended by my friend, Dr. Smith. I like its functionalities, but found that the same model is sold for only $2.8k at amazon .com... Lessonslearned? It’s worth checking online prices before shopping!""")
d = { x: ele for x, ele in enumerate(s.split(". "))}
print(d)


#3
def encodeQr(s):
    ns=""
    for i in range(0,len(s)):
        l1=['0','0','0','0','0','0','0','0']
        l1[i]='1'
        pre=''.join(l1)
        asc=ord(s[i])
        b1=bin(asc)
        ns= ns+pre+b1[2:]
    x=lambda ns: ns+"000" if(len(ns)>50) else(ns+"00" if(len(ns)>70) else ns)
    print(x(ns))
s = input("Enter the string ")
encodeQr(s)

#3-b
import python_module_16 as p
s = input("Enter the string ")
p.encodeQr(s)
