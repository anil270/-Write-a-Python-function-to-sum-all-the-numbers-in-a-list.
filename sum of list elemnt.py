#!/usr/bin/env python
# coding: utf-8

# #  Write a Python function to sum all the numbers in a list.

# In[28]:


def add(b):
    sum = 0
    for i in  b:
        sum = sum + i
    print("sum of numbers of list :",sum)

list = []
n = int(input("Enter the number of element :"))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
    y = list
print("list",y)
add(y)

