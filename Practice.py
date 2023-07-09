'''import re
a="Malaaavikaa"
print(re.sub('a{2}',"*",a,1))'''

'''class Test:
    __sum=0
    def disp(self):
        self.__sum+=1
        print(self.__sum)
print(Test.__sum)'''
'''class Parent:
    def Test(self):
        print("Alpha Test")
class Child(Parent):
    pass
ob1=Parent()
ob2=Child()
ob1.Test()
ob2.Test()'''

class A():
    def __init__(self,a={}):
        if not ('1' in a):
            a['1']=1
        else:
            a['1']+=1
        print(a['1'])
for i in range(2):
    a=A()

'''class NumTest:
    def __init__(self):
        self.val=1
    def Test(self):
        if self.val==1:
            print('Harry')
            self.val=2
        else:
            print('met')
class Assign(NumTest):
    def __init__(self):
        NumTest.__init__(self)
        self.data='Sally!'
    def Disp(self):
        print(self.data)
oN=NumTest()
oN.Test()

oP=Assign()
oP.Test()'''

'''xyz=('apple','applets','app','ap')
abc="Semesters"
sub='e'
print(abc.find(sub,len(min(xyz)),len(max(xyz))))'''

'''lis=[1,3,5,7,9,11,13,17,19,23,29]
op=range(4,len(lis),2)
print(op)'''

'''names1=['Amit','Ben','Charlie','Damon']
names2=names1
names3=names1[:]
names2[0]='Stefan'
names3[1]='John'
sum=0
for ls in (names1,names2,names3):
    if ls[0]=='Stefan':
        sum+=1
    if ls[1]=='John':
        sum+=10
print(sum)'''

