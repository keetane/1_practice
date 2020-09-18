#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.__file__


# In[2]:


python_list = [1, 2, 3]
python_list


# In[5]:


np_list = np.array([1, 2, 3])
np_list


# In[6]:


python_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
python_list


# In[7]:


np_list = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
np_list


# In[8]:


array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[9]:


array1 + array2


# In[10]:


array1 * array2


# In[11]:


array1 - array2


# In[12]:


array1 / array2


# In[13]:


array3 = np.array([1, 2, 3])
array4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[14]:


array3 + array4


# In[15]:


array3 * array4


# In[16]:


array3 - array4


# In[17]:


array3 / array4


# In[18]:


array5 = np.array([1, 2, 3, 4])
array6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[19]:


arra5 + array6


# ### IndexingとSlicing

# In[20]:


ndarray = np.array(([1, 2], [3, 4], [5, 6]))
print(ndarray)


# In[21]:


print(ndarray[1][0])
print(ndarray[1, 0])


# In[22]:


array = np.array([1, 2, 3, 4, 5, 6, 7])
print(array[1:6])
print(array[1:6:2])


# ### [N:M:L]とするとL-1飛びでslicingできます．

# In[23]:


ndarray = np.array([1, 2, 3])
print(ndarray)


# In[24]:


np.arange(0, 5, 2)


# ### np.arange(start, stop(, step))
# ### startからstopまでをstepおきに作成

# In[25]:


np.arange(5)


# In[26]:


np.arange(0, 5)


# In[27]:


np.arange(-5, 5)


# In[28]:


np.arange(1, 2, 20)


# In[29]:


np.arange(100, 200, 20)


# In[30]:


np.linspace(1, 2, 20)


# ### np.linspace(start, stop, num=50)
# ### np.arange()がstepだったのに対し，np.linspace()は要素の数(num)を指定します．startからstopまでの値をnum等分した値がarrayで返されます．stepを指定したい時はnp.arange()で，stepはなんでもいいが特定の数だけほしいという場合はnp.linspace()を使いましょう．stopの値を含むことに注意しましょう．

# In[31]:


ndarray = np.arange(0, 5)
ndarray_copy = ndarray.copy()
print("original array's id is {}".format(id(ndarray)))
print("copied array's id is {}".format(id(ndarray_copy)))

#changing original array
ndarray[:] = 100
print('original array:\n', ndarray)
print('copied array:\n', ndarray_copy)


# In[32]:


def myfunc(n):
    print(id(n))

a = 'test'
print(id(a))
myfunc(a)


# In[33]:


def add_world(hello):
    hello += ' world'
    return hello


# In[34]:


h_str = 'hello'
h_list = ['h', 'e', 'l', 'l', 'o']
h_array = [ndarray]
output_str = add_world(h_str)
output_list = add_world(h_list)
output_array = add_world(h_array)

print('output_str: {}'.format(output_str))
print('outpur_list: {}'.format(output_list))
print('outpur_array: {}'.format(output_array))


print('h_str: {}'.format(h_str))
print('h_list: {}'.format(h_list))


# In[35]:


def change_hundred(array):
    
    array[0] = 100
    return array

def change_hundred_copy(array):
    
    array_copy = array.copy()
    array_copy[0] = 100
    return array_copy

array_1 = np.arange(0, 4)
array_2 = np.arange(0, 4)

output_array = change_hundred(array_1)
output_array_copy = change_hundred_copy(array_2)

print('original array_1:\n', array_1)
print('original array_2:\n', array_2)


# In[36]:


shape = (2, 3, 5)
zeros = np.zeros(shape)
print(zeros)


# In[37]:


shape = (2, 3, 5)
ones_array_1 = np.ones(shape)
ones_array_2 = np.ones(0)
ones_array_3 = np.ones(4)
ones_array_4 = np.ones(4, str)
ones_array_5 = np.ones(4, list)


print(ones_array_1)
print(ones_array_2)
print(ones_array_3)
print(ones_array_4)
print(ones_array_5)


# In[38]:


np.eye(3)


# In[39]:


np.eye(3, 5)


# In[40]:


random_float = np.random.rand()
random_1d = np.random.rand(3)
random_2d = np.random.rand(3, 4)

print('random_float: {}\n'.format(random_float))
print('random_1d: {}\n'.format(random_1d))
print('random_2d: {}\n'.format(random_2d))


# In[41]:


random_float = np.random.randn()
random_1d = np.random.randn(3)
random_2d = np.random.randn(3, 4)

print('random_float: {}\n'.format(random_float))
print('random_1d: {}\n'.format(random_1d))
print('random_2d: {}\n'.format(random_2d))


# In[42]:


np.random.randint(10, 50, size=(2, 4, 3))


# In[43]:


np.random.randint(10, 50)


# In[44]:


np.random.randint(10, 50, size=(5, 2))


# In[45]:


np.random.randint(10, 50, size=(5, 2, 3, 4))


# ### array sizeは()内左から大きい次元要素を構成する。

# In[48]:


array = np.arange(0, 10)
print('array:\n{}'.format(array))
new_shape = (2,5)
reshaped_array = array.reshape(new_shape)
print('reshaped array:\n{} '.format(reshaped_array))
print("reshaped array's is:\n{} ".format(reshaped_array.shape)
print('original array is NOT changed:\n{} '.format(array))


# ### 要素の統計量を求める

# In[49]:


normal_dist_mat = np.random.randn(5, 5)
print(normal_dist_mat)


# In[50]:


print('max is:\naaa')
print(normal_dist_mat.max())
print(np.max(normal_dist_mat))


# In[51]:


#argmax
print('argmax is')
print(normal_dist_mat.argmax())


# In[52]:


normal_dist_mat.flatten()[9]


# In[53]:


print(normal_dist_mat)
print(normal_dist_mat.argmax())
print(normal_dist_mat.flatten()[normal_dist_mat.argmax()])
print(normal_dist_mat.flatten()[2])


# In[54]:


print('min is')
print(normal_dist_mat.min())
print('argmin is')
print(normal_dist_mat.argmin())


# In[55]:


print('mean is')
print(normal_dist_mat.mean())


# In[56]:


print('median is')
print(np.median(normal_dist_mat))


# In[57]:


print('standard deviation is')
print(normal_dist_mat.std())


# In[58]:


print(normal_dist_mat)
print('axis=0> {}'.format(normal_dist_mat.max(axis=0)))
print('axis=0< {}'.format(normal_dist_mat.min(axis=0)))
print('axis=1> {}'.format(normal_dist_mat.max(axis=1)))
print('axis=1< {}'.format(normal_dist_mat.min(axis=1)))
normal_dist_mat.min(axis=1)


# ### また，特定の行，列での統計量を求めたい場合は引数axisを指定します．axis=0を指定すると各列の統計量，axis=1を指定すると各行の統計量を返します．このaxisの使い方は重要です．覚えておきましょう．
# ### >上記の例では例えば、axis=0>だと各列の最大値が帰ってきている

# In[59]:


def axis0():
    return normal_dist_mat.max(axis=0)


# In[60]:


axis0()


# In[61]:


ndarray = np.linspace(-3, 3, 10)
expndarray = np.exp(ndarray)
print(ndarray)
print(expndarray)


# In[65]:


ndarray = np.linspace(-3, 3, 10)
logndarray = np.log(ndarray)
print(ndarray)
print(logndarray)


# In[66]:


print(logndarray[0])
print('nan == None?:{}'.format(logndarray[0] is None))


# In[67]:


np.isnan(logndarray[0])


# In[68]:


print(np.e)
print(np.log(np.e))


# In[69]:


ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('array is:\n{}'.format(ndarray))
print("ndarray's shape is:\n{}".format(ndarray.shape))


# In[70]:


expanded_ndarray = np.expand_dims(ndarray, axis=0)
expanded_ndarray.shape


# In[71]:


squeezed_expanded_ndarray = np.squeeze(expanded_ndarray)
squeezed_expanded_ndarray.shape


# In[72]:


flatten_array = ndarray.flatten()
print('flatten_array:\n{}'.format(flatten_array))
print('ndarray:\n{}'.format(ndarray))


# In[73]:


ndarray = np.array([
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400],
])
np.save('saved_numpy', ndarray)


# In[74]:


loaded_numpy = np.load('saved_numpy.npy')
loaded_numpy


# In[ ]:




