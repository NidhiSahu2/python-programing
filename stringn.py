list_1=list(range(1,51))
print(' '.join(map(str,[list_1])))
a=int (input("enter a number :"))
count=0
for element in list_1:
             if element%a==0 and element!=a:
              count=count+1
             print(count)
#how to add two tuple#
def no_dup(a):
    no_dup_list=[]
    for num in a:
        if num not in no_dup_list:
            no_dup_list.append(num)
            return (no_dup_list)
a=[1,2,3,4,5,6,7,5,6,7,8,45,8]
print('the new list no duplicatevalues ' ,no_dup(a))
