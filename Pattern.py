#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Inverted Right Triangle Star Pattern
n = 5
for i in range (0,n):
    for j in range (0,n-i):
        print("* ",end="")
    print()


# In[13]:


#Mirrored Right Triangle Star Pattern

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


# In[18]:


#right triangle star pattern
n = 5
for i in range (0,n+1):
    for i in range (0,i):
        print("* ",end="")
    print()


# In[4]:


#inverted mirror right triangle star pattern
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


# In[6]:


#pyramid star pattern
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# In[10]:


#inverted pyramid star pattern
n=5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# In[5]:


#half diamond star pattern
def pattern(n):
    for i in range(1, n+1):
        print('* ' * i)
    for j in range(n-1, 0, -1):
        print('* ' * j)
n = 5
pattern(n)


# In[8]:


#mirror half diamond star pattern
def pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))
    for j in range(n - 1):
        print(' ' * (j + 1) + '*' * (n - j - 1))
n = 5
pattern(n)


# In[10]:


#diamond star pattern
def print_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for j in range(n - 2, -1, -1):
        print(' ' * (n - j - 1) + '*' * (2 * j + 1))
n = 5
print_diamond(n)


# In[11]:


# 0,1 Number Pattern 
for i in range(1,6):
    for j in range(0,i):
        if(j % 2 == 1):
            print("0",end="")
        else:
            print("1", end="")
    print()


# In[13]:


# Number Pattern
for i in range(1,6):
    for j in range(i, i*2):
        print(j, end="")
    print()


# In[15]:


# 0,1 Number Pattern 
for i in range(1,6):
    for j in range(0,i):
        if(i % 2 == 1):
            print("1",end="")
        else:
            print("0", end="")
    print()


# In[18]:


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
n = 5
pattern(n)


# In[19]:


# diamond pattern with number 
def pattern(n):
    for i in range(1, n + 1):
        for s in range(n - i):
            print(' ', end=' ')
        for j in range(1, i + 1):
            print(j, end=' ')
        for k in range(i - 1, 0, -1):
            print(k, end=' ')
        print()

    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(' ', end=' ')
        for j in range(1, i + 1):
            print(j, end=' ')
        for k in range(i - 1, 0, -1):
            print(k, end=' ')
        print()

n = 5
pattern(n)


# In[20]:


# X Number Pattern
for i in range(1,10):
    for j in range(1,10):
        if(i == j or i+j == 10):
            print(i, end="")
        else:
            print(" ", end="")
    print()


# In[ ]:




