#list
myList = [1,2,3,4,'再来一次']
print(myList)
print(type(myList))
#通过索引调取元素
print(type(myList[0]))

#切片
mySlice = myList[1:3]
print(mySlice)
print(myList[:])
print(myList[:4])
print(myList[0:8])

#反转,该方法不常用
revList = myList[::-1]
print(revList)

#append追加,会将整体作为追加项
myList.append([11,22,33])
print(myList)

#extend追加,会将每个元素作为追加项
myList.extend([1,11,22,33])
print(myList)

#count 计算重复出现的次数，即计算个数
myCount = myList.count(1)
print(myCount)

#if，remove用法
print('没用remove删除前的列表：',myList)
if 1 in myList:
    myList.remove(1)
    print('好吧，删掉了一个之后：',myList)
else:
    print('没了，再删要报错了')

# sort
newList = [1,0,33,21,56,-3,9]
print('看个未排序',newList)
newList.sort()
print('默认排序：',newList)
newList.
