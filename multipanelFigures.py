#!/usr/bin/env python
# coding: utf-8

# # Making Multipanel Plots With Matplotlib

# First, we import numpy and matplotlib as usual

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# Then we define an array of angles, and their sines and cosines using numpy. This time we will use linspace

# In[2]:


x = np.linspace(0, 2 * np.pi, 100)
print(x[-1], 2 * np.pi)

y = np.sin(x)
z = np.cos(x)
w = np.sin(4*x)
v = np.cos(4*x)


# Now, let's make a two panel plot side-by-side

# In[3]:


#Call subplots to generate a multipanel figure. This means 1 row, 2 columns of figures
f, axarr = plt.subplots(1, 2)

#Treat axarr as an array, from left to right

#First panel
axarr[0].plot(x, y)
axarr[0].set_xlabel("x")
axarr[0].set_ylabel("sin(x)")
axarr[0].set_title(r"$\sin(x)$") #Math mode

#Second panel
axarr[1].plot(x, z)
axarr[1].set_xlabel("x")
axarr[1].set_ylabel("cos(x)")
axarr[1].set_title(r"$\cos(x)$")#Math mode


# In[6]:


#Call subplots to generate a multipanel figure. This means 1 row, 2 columns of figures
f, axarr = plt.subplots(1, 2)

#Treat axarr as an array, from left to right

#First panel
axarr[0].plot(x, y)
axarr[0].set_xlabel("x")
axarr[0].set_ylabel("sin(x)")
axarr[0].set_title(r"$\sin(x)$") #Math mode

#Second panel
axarr[1].plot(x, z, color = "red")
axarr[1].set_xlabel("x")
axarr[1].set_ylabel("cos(x)")
axarr[1].set_title(r"$\cos(x)$")#Math mode

#Adjust he sublots
f.subplots_adjust(wspace = 0.4)


# In[7]:


#Call subplots to generate a multipanel figure. This means 1 row, 2 columns of figures
f, axarr = plt.subplots(1, 2)

#Treat axarr as an array, from left to right

#First panel
axarr[0].plot(x, y)
axarr[0].set_xlabel("x")
axarr[0].set_ylabel("sin(x)")
axarr[0].set_title(r"$\sin(x)$") #Math mode

#Second panel
axarr[1].plot(x, z, color = "red")
axarr[1].set_xlabel("x")
axarr[1].set_ylabel("cos(x)")
axarr[1].set_title(r"$\cos(x)$")#Math mode

#Adjust he sublots
f.subplots_adjust(wspace = 0.4)

#Fix the axis ratios
axarr[0].set_aspect("equal") #Make the ratio of the tick units equal
axarr[1].set_aspect(np.pi)   #Make a square by setting the aspect to pi


# In[ ]:


#Adjust the size of the figure
# fig = plt.figure(figsize = (6, 6))

# plt.plot(x, y, label = r"$y = \sin(x)$")
# plt.plot(x, z, label = r"$y = \cos(x)$")
# plt.plot(x, w, label = r"$y = \sin(4x)$")
# plt.plot(x, v, label = r"$y = \sin(4x)$")

# plt.xlabel()
# plt.ylabel()
# plt.xlim()
# plt.ylim()

