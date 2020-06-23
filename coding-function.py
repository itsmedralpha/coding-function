#assinging elements
data_list=[34,56,87,23,78,90,55,18,56]
bel_50=[]
abo_50=[]
for i in range (len(data_list)):
    if data_list[i]>50:
        bel_50.append(data_list[i])
    else:
        abo_50.append(data_list[i])
print(bel_50)
print(abo_50)
print("\n")
#accessing element from tuple
food_tuple=("pizza","biriyani","meals","burger")
for i in range (len(food_tuple)):
    print(food_tuple[i])
print("\n")
#deleting different dictionary elements
name_dict={'hari':20,'kiran':19,'kishore':18}
print(name_dict)
del name_dict['kiran']
print(name_dict)

