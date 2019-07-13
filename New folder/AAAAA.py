print('AAACCCCCC')

my_list=[10,20,30,10,[10,56,89,75,10,56,10],56,10,89,48]
x=1
print('adadassdfdsssssssssss')
for num in my_list:
    if num==10:
        my_list.remove(num)
    elif x==1:
        print("vishnu")
    elif type(num) == list:
        print("vikrant")
        TenCount = num.count(10)
        print(TenCount)
        for item in range(TenCount):
            num.remove(10)
print(my_list)

# C:\Users\Admin\PycharmProjects\Demo\11_04_19_ListTypes_List_Tuple_Set_Dict_Methods.py
'''
my_list=[10,20,30,10,[10,56],56,10,89,48]
my_list1=[]
for num in my_list:
    if num != 10:
        my_list1.append(num)
    elif type(num) == list:
        print("vikrant")
        for item in num:
            if item == 10:
                num.remove(item)
                print(num)
        my_list1.append(num)
        #print(TenCount)

print(my_list1)

listOfItems1=[10,10,30,[10,0,20],10,58,10,10]

for outerItem in listOfItems1:
    if type(outerItem)==list:
        innerList = outerItem
        for innerItem in innerList:
                if innerItem==10:
                    innerList.remove(innerItem)
    elif outerItem==10:
        listOfItems1.remove(outerItem)
print(listOfItems1)



'''
