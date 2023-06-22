#!/usr/bin/env python
# coding: utf-8

# In[18]:


myList=["Alan","Binoy","John"]


# In[19]:


print(myList[0])


# In[20]:


myList.append(234)


# In[21]:


myList


# In[26]:


myList.append([1,2,3,4])
myList


# In[28]:


myList[1:4]


# In[29]:


myList.insert(1,"Mark")


# In[30]:


myList


# In[31]:


my_new_list=[1,243,563,54]
myList.extend(my_new_list)


# In[32]:


myList


# In[33]:


len(myList)


# In[34]:


type(myList)


# In[36]:


pip install numpy


# In[37]:


myList.remove(myList[2])


# In[40]:


myList.pop(5)


# In[39]:


myList


# In[44]:


del myList


# In[47]:


import keyword


# In[48]:


keyword.kwlist


# In[63]:


list1=["apple","orange","mango","pine","jelly"]


# In[64]:


for x in list1:
    print (x)


# In[65]:


for x in range(0,10):
    print(list1[x])


# In[55]:


i=0
while(i<=9):
    print(list1[i])
    i=i+1


# In[66]:


list1


# In[67]:


[print(x) for x in list1]


# In[71]:


newList=[x for x in list1 if "a" in x]


# In[72]:


newList


# In[79]:


newList.sort()
newList


# In[80]:


newList.sort(reverse=True)
newList


# In[83]:


def hello():
    print("Hello Function")


# In[84]:


hello()


# In[97]:


def function(*name):
    print(name[1]+" hai")
    


# In[98]:


function("abhay","ajay")


# In[101]:


def fun(name,age):
    print(name+" is "+age+" year old.")
fun(age="24",name="Ashiq")


# In[105]:


def lis(list_name):
    for x in list_name:
        print(x+" is fruit")


# In[106]:


fruits=["cherry","mango","apple"]
lis(fruits)


# In[4]:


def myfunction(items):
    for x in items:
        print(x,"is an alphabet")
        
items=["a","b","c"]
myfunction(items)


# In[6]:


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)


# In[23]:


List1=[1,2,3,4]
List2=[]
List2=List1.copy()
List2.append(5)


# In[24]:


List1


# In[25]:


List2


# In[35]:


List3=List1+List2
print(List3)


# In[34]:


print(List3.count(1));


# In[ ]:




