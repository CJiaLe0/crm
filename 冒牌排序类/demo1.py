input1=['h','e','l','l','o',' ','w','o','r','d',' ','j','a','v','a']
list1=[]
list2=[]
list3=[]
list1.extend(input1[0:5])
list2.extend(input1[5:11])
list3.extend(input1[11:15])
list3.extend(list2)
list3.extend(list1)
print(list3)


