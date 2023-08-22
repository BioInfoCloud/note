Pandas 是一个 Python 库，提供了高效的数据操作和分析功能。它主要用于数据处理和分析，包括数据读取、数据清洗、数据转换、数据聚合和可视化等功能。Pandas 基于 NumPy 库，并提供了类似 MATLAB 的接口，使得数据处理和分析变得更加方便。

Pandas 的核心是 Series 和 DataFrame 两种数据结构。Series 是一种一维数组，可以包含各种类型的数据（如整数、浮点数、字符串等），并具有标签（index）用于标记数据。DataFrame 是一个二维表格，可以看作是由多个 Series 组成的表格，其中每一列都可以看作是一个 Series。

Pandas 提供了一系列用于数据处理和分析的函数和方法，如：

    数据读取和写入：read_csv、read_excel、read_json、to_csv、to_excel、to_json 等。
    数据清洗：dropna、fillna、drop_duplicates 等。
    数据转换：map、replace、applymap、apply 等。
    数据聚合：groupby、agg、pivot_table 等。
    数据可视化：plot、hist、bar、箱形图等。

## 1.Pandas 的数据结构

Pandas 的核心数据结构是 Series 和 DataFrame。

**Series**：是一种一维数组，包含一组数据（values,ndarray类型）以及一个标签（index）。它可以看作是 Python 中的一维 NumPy 数组的扩展，增加了标签和数据类型等额外信息。Series 可以包含各种类型的数据，如整数、浮点数、字符串等。Series: 可以看做是一个有序的字典结构。

**DataFrame**：是一个二维表格，包含多个 Series，每个 Series 可以看作是表格中的一列。DataFrame 提供了类似于表格的数据结构，可以方便地访问、处理和分析数据。

除了 Series 和 DataFrame，Pandas 还提供了其他数据结构，如 Index、MultiIndex、Panel、Panel4D、SparseSeries 和 SparseDataFrame 等。这些数据结构可以满足不同类型的数据分析和操作需求。

### 1.1  Series的创建

**(1) 由列表或NumPy数组创建**


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
s = pd.Series([11, 22, 33], index=list('ABC'))
s
```




    A    11
    B    22
    C    33
    dtype: int64




```python
# index和values
s.index, s.values
```




    (Index(['A', 'B', 'C'], dtype='object'), array([11, 22, 33], dtype=int64))



**(2) 由字典创建**


```python
s = pd.Series({'name': "肖战","age": 27,'tel':"18012541968"})
s
```




    name             肖战
    age              27
    tel     18012541968
    dtype: object



### 1.2 Series的索引和切片

#### 1.2.1 Series的索引

可以使用中括号取单个索引（此时返回的是元素类型），或者中括号里一个列表取多个索引（此时返回的仍然是一个Series类型）。分为显示索引和隐式索引：

**(1) 显式索引：**

使用index中的元素作为索引值


```python
s = pd.Series({'name': "肖战","age": 27,'tel':"18012541968"})
s['name']
```




    '肖战'



**(2) 隐式索引：**

使用整数作为索引值


```python
s = pd.Series({'name': "肖战","age": 27,'tel':"18012541968"})
s[0]
```




    '肖战'



#### 1.2.2 Series的切片


```python
s = pd.Series([11, 22, 33, 44, 55, 66, 77, 88, 99], index=list('ABCDEFGHI'), name='hello')
s
```




    A    11
    B    22
    C    33
    D    44
    E    55
    F    66
    G    77
    H    88
    I    99
    Name: hello, dtype: int64




```python
s[1 : 4]  # 前闭后开
```




    B    22
    C    33
    D    44
    Name: hello, dtype: int64




```python
s['B': 'D']  # 2边都包含
```




    B    22
    C    33
    D    44
    Name: hello, dtype: int64



#### 1.2.3 Series的基本属性和方法¶

    shape 形状
    
    size 长度
    
    index 索引
    
    values 值
    
    name 名字


```python
s = pd.Series([11, 22, 33, 44, 55, 66, 77, 88, 99], index=list('ABCDEFGHI'), name='hello')
print(s.shape)
print(s.size)
print(s.index)
print(s.values)
print(s.name)
```

    (9,)
    9
    Index(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], dtype='object')
    [11 22 33 44 55 66 77 88 99]
    hello


### 1.3 DataFrame

DataFrame是一个【表格型】的数据结构，可以看做是【由Series组成的字典】（共用同一个索引）。DataFrame由按一定顺序排列的多列数据组成。设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也有列索引。

    行索引：index
    列索引：columns
    值：values（NumPy的二维数组）

#### 1.3.1 DataFrame的创建

最常用的方法是传递一个字典来创建。DataFrame以字典的键作为每一【列】的名称，以字典的值（一个数组）作为每一列。

此外，DataFrame会自动加上每一行的索引（和Series一样）。

同Series一样，若传入的列与字典的键不匹配，则相应的值为NaN。


```python
df = pd.DataFrame({'name': ['刘亦菲', '李冰冰', '林心如'], 'age': [33, 44, 55]})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>刘亦菲</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李冰冰</td>
      <td>44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>林心如</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({'name': ['刘亦菲', '李冰冰', '林心如'], 'age': [33, 44, 55]},index=list('ABC'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>刘亦菲</td>
      <td>33</td>
    </tr>
    <tr>
      <th>B</th>
      <td>李冰冰</td>
      <td>44</td>
    </tr>
    <tr>
      <th>C</th>
      <td>林心如</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}  
index = pd.Index(['row0', 'row1', 'row2'], name='row')  
df = pd.DataFrame(data, index=index)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>row</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row0</th>
      <td>Alice</td>
      <td>25</td>
    </tr>
    <tr>
      <th>row1</th>
      <td>Bob</td>
      <td>30</td>
    </tr>
    <tr>
      <th>row2</th>
      <td>Charlie</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df.values)
print(df.index)
print(df.columns)
print(df.shape)
```

    [['Alice' 25]
     ['Bob' 30]
     ['Charlie' 35]]
    Index(['row0', 'row1', 'row2'], dtype='object', name='row')
    Index(['Name', 'Age'], dtype='object')
    (3, 2)



```python
df.head(2)  # 默认前5行
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>row</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row0</th>
      <td>Alice</td>
      <td>25</td>
    </tr>
    <tr>
      <th>row1</th>
      <td>Bob</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(2)  # 默认后5行
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>row</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row1</th>
      <td>Bob</td>
      <td>30</td>
    </tr>
    <tr>
      <th>row2</th>
      <td>Charlie</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(np.random.randint(60,100,size=(4, 5)), 
                  index=['李白', '杜甫', '白居易', '秦始皇'], 
                  columns=['Python', 'Java', 'C', 'R', 'JS'])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>66</td>
      <td>67</td>
      <td>75</td>
      <td>66</td>
      <td>95</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
      <td>85</td>
      <td>74</td>
      <td>65</td>
      <td>88</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>67</td>
      <td>62</td>
      <td>96</td>
      <td>74</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 默认是对列取索引
df2['Python']
# df2['李白']  # 不可以直接取行索引

```




    李白     66
    杜甫     63
    白居易    95
    秦始皇    67
    Name: Python, dtype: int32




```python
df2.Python  #  Series
```




    李白     66
    杜甫     63
    白居易    95
    秦始皇    67
    Name: Python, dtype: int32




```python
df2[['Python']]  # DataFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>66</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[['Python', 'Python', 'Java']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Python</th>
      <th>Java</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>66</td>
      <td>66</td>
      <td>67</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
      <td>63</td>
      <td>85</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>95</td>
      <td>69</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>67</td>
      <td>67</td>
      <td>62</td>
    </tr>
  </tbody>
</table>
</div>



#### 1.3.2 对行进行索引

使用.loc[]加index来进行行索引

使用.iloc[]加整数来进行行索引

同样返回一个Series，index为原来的columns。


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>66</td>
      <td>67</td>
      <td>75</td>
      <td>66</td>
      <td>95</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
      <td>85</td>
      <td>74</td>
      <td>65</td>
      <td>88</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>67</td>
      <td>62</td>
      <td>96</td>
      <td>74</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc['李白']
```




    Python    66
    Java      67
    C         75
    R         66
    JS        95
    Name: 李白, dtype: int32




```python
df2.iloc[0]
```




    Python    66
    Java      67
    C         75
    R         66
    JS        95
    Name: 李白, dtype: int32




```python
df2.loc[['李白', '杜甫']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>66</td>
      <td>67</td>
      <td>75</td>
      <td>66</td>
      <td>95</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
      <td>85</td>
      <td>74</td>
      <td>65</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.iloc[[2, 1, 2, 2, 2, 2, 2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>63</td>
      <td>85</td>
      <td>74</td>
      <td>65</td>
      <td>88</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>95</td>
      <td>69</td>
      <td>70</td>
      <td>64</td>
      <td>72</td>
    </tr>
  </tbody>
</table>
</div>



#### 1.3.3 DataFrame的切片

【注意】 直接用中括号时：

    索引优先对列进行操作
    切片优先对行进行操作


```python
# NumPy 索引和切片都是优先对行
df2 = pd.DataFrame(np.random.randint(60,100,size=(4, 5)), 
                  index=['李白', '杜甫', '白居易', '秦始皇'], 
                  columns=['Python', 'Java', 'C', 'R', 'JS'])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>89</td>
      <td>86</td>
      <td>98</td>
      <td>93</td>
      <td>60</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>85</td>
      <td>62</td>
      <td>91</td>
      <td>62</td>
      <td>83</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>64</td>
      <td>62</td>
      <td>69</td>
      <td>95</td>
      <td>90</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>84</td>
      <td>76</td>
      <td>89</td>
      <td>87</td>
      <td>94</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.values[:2]
```




    array([[89, 86, 98, 93, 60],
           [85, 62, 91, 62, 83]])




```python
# DataFrame: 
#   索引优先对列进行操作
#   切片优先对行进行操作

# 行切片
df2[1 : 3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>杜甫</th>
      <td>99</td>
      <td>90</td>
      <td>87</td>
      <td>73</td>
      <td>60</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>94</td>
      <td>61</td>
      <td>95</td>
      <td>87</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2['杜甫' : '白居易']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Python</th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
      <th>JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>杜甫</th>
      <td>99</td>
      <td>90</td>
      <td>87</td>
      <td>73</td>
      <td>60</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>94</td>
      <td>61</td>
      <td>95</td>
      <td>87</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 列切片
df2.iloc[:, 1:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Java</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>78</td>
      <td>79</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>90</td>
      <td>87</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>61</td>
      <td>95</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>79</td>
      <td>94</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc[:, "Java": "R"]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Java</th>
      <th>C</th>
      <th>R</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>李白</th>
      <td>78</td>
      <td>79</td>
      <td>96</td>
    </tr>
    <tr>
      <th>杜甫</th>
      <td>90</td>
      <td>87</td>
      <td>73</td>
    </tr>
    <tr>
      <th>白居易</th>
      <td>61</td>
      <td>95</td>
      <td>87</td>
    </tr>
    <tr>
      <th>秦始皇</th>
      <td>79</td>
      <td>94</td>
      <td>89</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Pandas数据合并

Pandas 中的数据合并主要包括以下几种方式：

    pd.concat() 函数实现。
    pd.merge() 函数实现。



```python
import numpy as np
import pandas as pd
```


```python
## 定义一个生成DataFrame的函数
def make_df(indexs, columns):    
    data = [[str(j)+str(i) for j in columns] for i in indexs]
    df = pd.DataFrame(data=data, index=indexs, columns=columns)
    return df
```


```python
make_df([1, 2, 3, 4], ['A','B','C'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
    </tr>
  </tbody>
</table>
</div>



### 2.1  使用pd.concat()级联
pandas使用pd.concat函数，与np.concatenate函数类似。

> pd.concat(objs, axis=0, join='inner', join_axes=None, ignore_index=False, copy=True, names=None)


参数说明：

    objs：要合并的 Pandas 对象列表。可以是 DataFrame、Series 或其他 Pandas 对象。
    axis：要合并的轴。0 表示按行合并（默认值），1 表示按列合并。
    join：指定合并方式。可以是 'inner'（默认值，只保留重叠的元素）、'outer'（保留所有元素）或 'left'、'right'（分别保留左边界和右边界的元素）。
    join_axes：指定合并时使用的轴。如果指定了该参数，则只合并指定的轴，而不是所有轴。
    ignore_index：如果为 True，则不保留原始索引，重新创建一个新的索引。
    copy：如果为 True，则将合并后的对象复制一份，否则直接在原地进行修改。
    names：如果指定了该参数，则在合并后的对象中创建两个附加的列，分别包含左侧和右侧对象的名称。

**简单级联**

    df1 = make_df([1, 2], ['A', 'B'])
    df2 = make_df([3, 4], ['A', 'B'])
    display(df1, df2)


```python
df1 = make_df([1, 2], ['geneA', 'geneB', 'geneC'])
df2 = make_df([2, 3], ['geneA', 'geneB', 'geneD'])
display(df1, df2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geneA</th>
      <th>geneB</th>
      <th>geneC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>geneA1</td>
      <td>geneB1</td>
      <td>geneC1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>geneC2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geneA</th>
      <th>geneB</th>
      <th>geneD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>geneD2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>geneA3</td>
      <td>geneB3</td>
      <td>geneD3</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.concat( (df1, df2) )  # 上下合并，默认
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geneA</th>
      <th>geneB</th>
      <th>geneC</th>
      <th>geneD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>geneA1</td>
      <td>geneB1</td>
      <td>geneC1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>geneC2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>NaN</td>
      <td>geneD2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>geneA3</td>
      <td>geneB3</td>
      <td>NaN</td>
      <td>geneD3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat((df1, df2), axis=1)  # 左右合并
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geneA</th>
      <th>geneB</th>
      <th>geneC</th>
      <th>geneA</th>
      <th>geneB</th>
      <th>geneD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>geneA1</td>
      <td>geneB1</td>
      <td>geneC1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>geneC2</td>
      <td>geneA2</td>
      <td>geneB2</td>
      <td>geneD2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>geneA3</td>
      <td>geneB3</td>
      <td>geneD3</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd  
  
# 创建两个 DataFrame  
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})  
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})  
  
# 沿着行方向合并  
result = pd.concat([df1, df2])  
display(result)
# 沿着列方向合并  
result = pd.concat([df1, df2], axis=1)  
display(result)
  
# 沿着行方向合并，忽略索引  
result = pd.concat([df1, df2], ignore_index=True)  
display(result)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>


### 2.2 使用pd.merge()合并

类似MySQL中表和表的合并

pd.merge()是pandas库中用于合并两个或更多数据框（DataFrame）的函数。它通过共享一个或多个键将数据框的行连接在一起。

merge与concat的区别在于，merge需要依据某一共同的行或列来进行合并。

使用pd.merge()合并时，会自动根据两者相同column名称的那一列，作为key来进行合并。

每一列元素的顺序不要求一致

> pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

参数说明：

    left: 左侧的数据框。
    right: 右侧的数据框。
    how: 连接类型，可以是'inner'（内连接，默认），'left'（左连接），'right'（右连接），'outer'（外连接）。
    on: 用于连接的键，可以是列名或索引名。如果how='inner'，则此参数必须提供。
    left_on: 左侧数据框中的键。
    right_on: 右侧数据框中的键。
    left_index: 是否使用左侧数据框的索引作为连接键（如果为True，则忽略left_on）。
    right_index: 是否使用右侧数据框的索引作为连接键（如果为True，则忽略right_on）。
    sort: 是否对合并后的结果进行排序（如果为True，则按照连接键进行排序）。
    suffixes: 当有重复键时，用于区分列名的后缀。
    copy: 是否创建新的数据框（如果为True，则创建新的数据框）。
    indicator: 是否创建一个指示列，指示合并的类型（如果为True，则创建一个指示列）。
    validate: 用于验证连接键的函数。

#### 2.2.1 一对一合并


```python
import pandas as pd  
  
# 创建左侧数据框  
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})  
display(df1)  
# 创建右侧数据框  
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': ['x', 'y', 'z']})  
display(df2)  
# 使用pd.merge()合并两个数据框  
merged_df = pd.merge(df1, df2, on='key')  
  
# 输出合并后的数据框  
merged_df
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B</td>
      <td>x</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C</td>
      <td>y</td>
    </tr>
    <tr>
      <th>2</th>
      <td>D</td>
      <td>z</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
      <th>value2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B</td>
      <td>2</td>
      <td>x</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C</td>
      <td>3</td>
      <td>y</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2) # 默认 内连接
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
      <th>value2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B</td>
      <td>2</td>
      <td>x</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C</td>
      <td>3</td>
      <td>y</td>
    </tr>
  </tbody>
</table>
</div>



#### 2.2.2 多对一合并


```python
df3 = pd.DataFrame({
    'id': [1, 2, 2],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df4 = pd.DataFrame({
    'id': [2, 3, 4],
    'sex': ['男', '女', '男'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df3, df4)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.merge(df3, df4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>陈明</td>
      <td>44</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
  </tbody>
</table>
</div>



#### 2.2.3 多对多的合并


```python
df5 = pd.DataFrame({
    'id': [1, 2, 2],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df6 = pd.DataFrame({
    'id': [2, 2, 4],
    'sex': ['男', '女', '男'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df5, df6)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.merge(df5, df6)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>陈明</td>
      <td>44</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>陈明</td>
      <td>44</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>



#### 2.2.4 key的规范化

使用on=显式指定哪一列为key,当2个DataFrame有多列相同时使用。


```python
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'name': ['王明', '赵明', '江明'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df1, df2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>赵明</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>江明</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.merge(df1, df2, on='id')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name_x</th>
      <th>age</th>
      <th>name_y</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>王明</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>赵明</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>李四</td>
      <td>33</td>
      <td>Saler</td>
    </tr>
  </tbody>
</table>
</div>



使用left_on和right_on指定左右两边的列作为key，当左右两边的key都不想等时使用


```python
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id2': [2, 3, 4],
    'sex': ['男', '女', '男'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df1, df2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id2</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.merge(df1, df2, left_on='id', right_on='id2')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>id2</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>3</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>



当左边的列和右边的index相同的时候,使用right_index=True


```python
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id2': [2, 3, 4],
    'sex': ['男', '女', '男'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df1, df2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id2</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
pd.merge(df1, df2, left_index=True, right_on='id2')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>id2</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
  </tbody>
</table>
</div>



#### 2.2.5 内合并与外合并




```python
# 内合并：只保留两者都有的key（默认模式）
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['李明', '王明', '陈明'],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'sex': ['男', '女', '男'],
    'job': ['Saler', 'CEO', 'Programer']
})
display(df1, df2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



```python
# how : {'left', 'right', 'outer', 'inner', 'cross'}, default 'inner'
pd.merge(df1, df2)  # 默认是内连接
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, how='inner')  # 默认是内连接
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, how='left') 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
  </tbody>
</table>
</div>



外合并 how='outer'：补NaN


```python
pd.merge(df1, df2, how='outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>李明</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>王明</td>
      <td>33.0</td>
      <td>男</td>
      <td>Saler</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>陈明</td>
      <td>44.0</td>
      <td>女</td>
      <td>CEO</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>男</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>



当列冲突时，即有多个列名称相同时，需要使用on=来指定哪一个列作为key，配合sufixes指定冲突列名。

可以使用suffixes=自己指定后缀


```python
import pandas as pd  
  
# 创建数据框 df1  
df1 = pd.DataFrame({'id':[1,2,3],
                    'name': ['Alice', 'Bob', 'Charlie'],  
                    'age': [25, 30, 35]})  
  
# 创建数据框 df2  
df2 = pd.DataFrame({'id':[2,3,4],
                    'name': ['David', 'Bob', 'Charlie'],  
                    'salary': [50000, 60000, 70000]})  
  
print("df1:")  
display(df1)
print("df2:")  
display(df2)

merged_df = pd.merge(df1, df2, on='id', suffixes=('_df1', '_df2') )  
merged_df
```

    df1:



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alice</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bob</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Charlie</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>


    df2:



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>David</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Bob</td>
      <td>60000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Charlie</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name_df1</th>
      <th>age</th>
      <th>name_df2</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Bob</td>
      <td>30</td>
      <td>David</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Charlie</td>
      <td>35</td>
      <td>Bob</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({'name':['陈明','王明','李明'],'id' :[1,2,3],'age': [22,33,44]})
df2 = pd.DataFrame({'id':[2,3,4],'name': ['王明', '李明','赵明'] ,'job': ['saler','CTO',' Programer']})
display(df1,df2)
df1. merge(df2,on='id',suffixes=['_表1','表2'] )

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>id</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>陈明</td>
      <td>1</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>王明</td>
      <td>2</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>李明</td>
      <td>3</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>王明</td>
      <td>saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>李明</td>
      <td>CTO</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>赵明</td>
      <td>Programer</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_表1</th>
      <th>id</th>
      <th>age</th>
      <th>name表2</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>王明</td>
      <td>2</td>
      <td>33</td>
      <td>王明</td>
      <td>saler</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李明</td>
      <td>3</td>
      <td>44</td>
      <td>李明</td>
      <td>CTO</td>
    </tr>
  </tbody>
</table>
</div>



**总结：**

    合并有三种现象:一对一,多对一,多对多.
    合并默认会找相同的列名进行合并,如果有多个列名相同,用on来指定.
    如果没有列名相同,但是数据又相同,可以通过left _on, right_ _on来分别指定要合并的列.
    如果想和index合并,使用left. index, right _index来指定.
    如果多个列相同,合并之后可以通过suffixes来区分.
    还可以通过how来控制合并的结果,默认是内合并,还有外合并outer,左合并Ieft,右合并right.



### 2.3 join()函数 

使用join()函数将DataFrame与另一个DataFrame进行连接。


```python
import pandas as pd  
  
# 创建两个DataFrame  
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})  
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})  
display(df1,df2)
# 
result = df1.join(df2)
result
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Pandas缺失值处理

### 3.1 None与np.nan



```python
print(None == None)  # 输出：True  
print(np.nan == np.nan)  # 输出：False  
print(None == np.nan)  # 输出：False
```

    True
    False
    False


在NumPy中，np.nan 代表 "Not a Number"，它是一种特殊的浮点数值，用于表示无法表示的或者未定义的数值。由于其特殊性质，np.nan 与其他任何值（包括它自己）进行比较都会返回 False，包括与自身的比较。

这是因为在数学和计算的上下文中，"不是一个数字" 不能被看作与任何其他值相等，即使是它自己。因此，np.nan 与任何值进行比较都会返回 False，即使两个 np.nan 也不例外。这是一种在处理缺失数据和非数值时保持一致性的方式。

如果你想检查一个值是否为 np.nan，应该使用 np.isnan() 函数而不是直接使用等号。


```python
import numpy as np    
print(np.isnan(np.nan))  # 输出：True
```

    True


在 Pandas 中，None 和 np.nan（NumPy 中的 "Not a Number"）在大多数情况下都被视为缺失值，即都被当作 NaN（Not a Number）来处理。这种处理是为了在处理数据时保持一致性和方便性。

在 Pandas 中，None 和 np.nan 都被视为缺失值的情况包括：

    在 Series 或 DataFrame 中，它们都被当作缺失值处理，并且可以通过一些方法（如 isnull() 和 fillna()）来处理这些缺失值。
    
    在数值计算中，它们都会被当作特殊的缺失值处理，比如在进行算术运算时，它们与其他值相加、相乘等都会得到 NaN。
    
    在逻辑运算中，它们都会被当作缺失的逻辑值处理，即与逻辑操作相关的运算会产生 NaN 结果。

需要注意的是，虽然在大多数情况下 None 和 np.nan 都被当作缺失值处理，但它们之间并不等价。None 是 Python 中的特殊对象，而 np.nan 是一个浮点数值。在某些特定情况下，它们可能会有不同的行为，尤其是在数据类型推断和某些操作中。

总之，Pandas 设计了这种处理方式，以便在数据处理中能够更方便地处理缺失值，而不必关心是使用 None 还是 np.nan。

### 3.2 检查缺失值： 

使用 isnull() 或 isna() 方法可以检查一个 Series 或 DataFrame 中的缺失值，返回一个布尔类型的结果。



```python
import pandas as pd
import numpy as np

data = pd.Series([1, 2, None, 4, np.nan, 6])
missing_values = data.isnull()
print(missing_values)
print("----------")
print(data.isna())
```

    0    False
    1    False
    2     True
    3    False
    4     True
    5    False
    dtype: bool
    ----------
    0    False
    1    False
    2     True
    3    False
    4     True
    5    False
    dtype: bool



```python
data = np.random.randint(0, 100, size=(5, 5))
df = pd.DataFrame(data=data, columns=list('ABCDE'))
df['B'][1] = np.nan
df['C'][2] = np.nan
df
```

    C:\Users\chens\AppData\Local\Temp\ipykernel_21680\690573573.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df['C'][2] = np.nan





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37</td>
      <td>17.0</td>
      <td>51.0</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>NaN</td>
      <td>53.0</td>
      <td>65</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>56</td>
      <td>87.0</td>
      <td>NaN</td>
      <td>53</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52</td>
      <td>33.0</td>
      <td>33.0</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>97.0</td>
      <td>94.0</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().all()  # 必须所有的全为空才能找到
```




    A    False
    B    False
    C    False
    D    False
    E    False
    dtype: bool




```python
df.isnull().any()  # 只要有1个为空就会找到 （常用）  有空的列
```




    A    False
    B     True
    C     True
    D    False
    E    False
    dtype: bool




```python
df.isnull().any(axis=1)  # 有空的行
```




    0    False
    1     True
    2     True
    3    False
    4    False
    dtype: bool




```python
# 取出非空的行
cond1 = df.isnull().any(axis=1)
cond1
df[ ~cond1 ]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37</td>
      <td>17.0</td>
      <td>51.0</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52</td>
      <td>33.0</td>
      <td>33.0</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>97.0</td>
      <td>94.0</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
cond1 = df.notnull().all(axis=1)
cond1
df[ cond1 ]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37</td>
      <td>17.0</td>
      <td>51.0</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52</td>
      <td>33.0</td>
      <td>33.0</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>97.0</td>
      <td>94.0</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.DataFrame(np.random.randint(40, 100, size=(4, 5)))
df3.index = list('ABCD')
df3.columns = ['C', 'R', 'Python', 'Java', 'C++']
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>R</th>
      <th>Python</th>
      <th>Java</th>
      <th>C++</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>86</td>
      <td>71</td>
      <td>72</td>
      <td>50</td>
      <td>77</td>
    </tr>
    <tr>
      <th>B</th>
      <td>62</td>
      <td>51</td>
      <td>58</td>
      <td>40</td>
      <td>91</td>
    </tr>
    <tr>
      <th>C</th>
      <td>72</td>
      <td>96</td>
      <td>80</td>
      <td>82</td>
      <td>97</td>
    </tr>
    <tr>
      <th>D</th>
      <td>66</td>
      <td>50</td>
      <td>92</td>
      <td>91</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 找出Python成绩小于60的数，并删除

cond = df3.Python < 60
~cond

# bool值索引
df3[~cond]

# drop
# df3.drop(index='B')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>R</th>
      <th>Python</th>
      <th>Java</th>
      <th>C++</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>86</td>
      <td>71</td>
      <td>72</td>
      <td>50</td>
      <td>77</td>
    </tr>
    <tr>
      <th>C</th>
      <td>72</td>
      <td>96</td>
      <td>80</td>
      <td>82</td>
      <td>97</td>
    </tr>
    <tr>
      <th>D</th>
      <td>66</td>
      <td>50</td>
      <td>92</td>
      <td>91</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>



### 3.3 过滤函数

> DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

参数说明：

     axis：指定要删除的轴，0表示删除行，1表示删除列。
    how：指定删除的方式，'any'表示删除包含NaN值的行或列，'all'表示删除所有值都为NaN的行或列。
    thresh：如果要删除的行或列的数量不是唯一的，可以指定要删除的行或列的数量。
    subset：指定要删除NaN值的子集。
    inplace：如果为True，则直接在原始DataFrame上修改，否则返回一个新的DataFrame。

用于从DataFrame中删除包含NaN值的行或列。可以选择过滤的是行还是列（默认为行）


```python
import pandas as pd  
  
# 创建一个包含NaN值的DataFrame  
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})  
display(df)
  
# 删除包含NaN值的行  
df_dropna = df.dropna()  
display(df_dropna)  
  
# 删除包含NaN值的列  
df_dropna = df.dropna(axis=1)  
display(df_dropna)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>


### 3.4 填充缺失值

使用 fillna() 方法可以将缺失值填充为指定的值。你可以传递一个特定的值、一个字典或者使用不同的填充方法。

> DataFrame.fillna(value=None, method=None, axis=0, inplace=False, limit=None, downcast=None)

参数说明：

    value：用于填充缺失值的值或一个字典，其中键是列名，值是要填充的值。
    method：指定填充方法，例如'ffill'（向前填充）、'bfill'（向后填充）或'mean'（使用列的平均值填充）。
    axis：指定要填充的轴，0表示行，1表示列。
    inplace：如果为True，则直接在原始DataFrame上修改，否则返回一个新的DataFrame。
    limit：向前或向后填充时，限制填充的次数。
    downcast：可选参数，用于指定输出数据的精度。


```python
import pandas as pd  
import numpy as np  
  
# 创建一个包含NaN值的DataFrame  
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})  
display(df)  
  
# 使用0填充NaN值  
df_filled = df.fillna(value=0)  
display(df_filled)  
  
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



```python
df = pd.DataFrame(data=data, columns=list(['age', 'salary', 'height', 'score', 'weight']))

df['age'][1] = np.nan
df['height'][2] = np.nan
df
```

    C:\Users\chens\AppData\Local\Temp\ipykernel_21680\3502519571.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df['height'][2] = np.nan





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>salary</th>
      <th>height</th>
      <th>score</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.0</td>
      <td>17</td>
      <td>51.0</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>41</td>
      <td>53.0</td>
      <td>65</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>56.0</td>
      <td>87</td>
      <td>NaN</td>
      <td>53</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52.0</td>
      <td>33</td>
      <td>33.0</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.0</td>
      <td>97</td>
      <td>94.0</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 填充： 平均值，中位数，众数，0

# height: 身高
df['height'].fillna(value=df['height'].mean(), inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>salary</th>
      <th>height</th>
      <th>score</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.0</td>
      <td>17</td>
      <td>51.00</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>41</td>
      <td>53.00</td>
      <td>65</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>56.0</td>
      <td>87</td>
      <td>57.75</td>
      <td>53</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52.0</td>
      <td>33</td>
      <td>33.00</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.0</td>
      <td>97</td>
      <td>94.00</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['age'].fillna(value=df['age'].median(),inplace=True)
df     
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>salary</th>
      <th>height</th>
      <th>score</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.0</td>
      <td>17</td>
      <td>51.00</td>
      <td>72</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44.5</td>
      <td>41</td>
      <td>53.00</td>
      <td>65</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>56.0</td>
      <td>87</td>
      <td>57.75</td>
      <td>53</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52.0</td>
      <td>33</td>
      <td>33.00</td>
      <td>48</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.0</td>
      <td>97</td>
      <td>94.00</td>
      <td>79</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Pandas处理重复值和异常值

### 4.1 删除重复值

使用drop_duplicates()函数可以删除DataFrame中的重复行。默认情况下，该函数将删除所有重复行，但也可以指定要删除哪些列的重复行。

> DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)

参数说明：

    subset：一个列的子集，用于确定哪些列应被视为唯一标识符。如果提供此参数，keep参数将无效。
    keep：控制哪些行应被视为重复。可能的值是'first'，'last'或False。
    inplace：如果为True，则直接在原始DataFrame上修改，否则返回一个新的DataFrame。


```python
import pandas as pd  
  
df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6], 'C': [7, 8, 8, 9]})  
display(df)
df = df.drop_duplicates()  
df
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({'A': [1, 1, 2, 3], 'B': [4, 4, 5, 6], 'C': [7, 7, 8, 9]})  
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>


使用duplicated()函数检测重复的行,返回元素为布尔类型的Series对象，每个元素对应一行，如果该行不是第一次出现，则元素为True


```python
# 检测是否重复
df.duplicated(keep='first')
```




    0    False
    1     True
    2    False
    3    False
    dtype: bool




```python
df['C'][1] = 666
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>666</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.duplicated(subset=['A', 'B'])
```




    0    False
    1     True
    2    False
    3    False
    dtype: bool



使用drop_duplicates()函数删除重复的行


```python
df.drop_duplicates(subset=['A', 'B'],inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



### 4.2 映射

映射的含义：创建一个映射关系列表，把values元素和一个特定的标签或者字符串绑定。

map()函数：适合处理某一单独的列

map()函数中可以使用lambda函数


```python
df = pd.DataFrame(data=np.random.randint(0, 100, size=(3, 4)), columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40</td>
      <td>6</td>
      <td>76</td>
      <td>24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>18</td>
      <td>10</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>86</td>
      <td>9</td>
      <td>38</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['B'] = df['B'].map(lambda x: x*10)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40</td>
      <td>60</td>
      <td>76</td>
      <td>24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>180</td>
      <td>10</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>860</td>
      <td>9</td>
      <td>38</td>
    </tr>
  </tbody>
</table>
</div>



### 4.3 异常值检测和过滤

#### 4.3.1 有关异常值检测的相关函数和操作

describe()是pandas库中DataFrame对象的一个方法，用于计算数据框中每列的描述性统计量。这些统计量包括：计数（count）、平均值（mean）、标准差（std）、最小值（min）、四分位数（25%，50%，75%）和最大值（max）。


```python
import pandas as pd  
  
# 创建一个简单的数据框  
data = {  
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],  
    'age': [25, 32, 18, 47, 22],  
    'salary': [50000, 70000, 30000, 90000, 60000]  
}  
  
df = pd.DataFrame(data)  

display(df)
# 查看数据框的描述性统计量  
df.describe()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>28.800000</td>
      <td>60000.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>11.388591</td>
      <td>22360.679775</td>
    </tr>
    <tr>
      <th>min</th>
      <td>18.000000</td>
      <td>30000.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>22.000000</td>
      <td>50000.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>25.000000</td>
      <td>60000.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>32.000000</td>
      <td>70000.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>47.000000</td>
      <td>90000.000000</td>
    </tr>
  </tbody>
</table>
</div>



df.drop(): 删除特定索引


```python
df.drop(index=[1, 2])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(columns=['age'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>



unique() : 唯一,去重


```python
df2 = pd.DataFrame(data=np.random.randint(5, 10, size=(3, 4)), columns=list('ABCD'))
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>5</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>6</td>
      <td>5</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2['B'].unique()
```




    array([5, 6])



df.sort_values(): 根据值排序


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='age')  # 升序
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='salary', ascending=False)  # 降序
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df ##排序后不改变原来数据框的结构
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>



df.info(): 查看数据信息


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   name    5 non-null      object
     1   age     5 non-null      int64 
     2   salary  5 non-null      int64 
    dtypes: int64(2), object(1)
    memory usage: 248.0+ bytes


#### 4.3.2 异常值过滤


```python
# 创建一个简单的数据框  
data = {  
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],  
    'age': [25, 32, 18, 47, 22],  
    'salary': [50000, 70000, 30000, 90000, 60000]  
}  
  
df = pd.DataFrame(data)  
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>32</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>47</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# bool值索引过滤异常值
cond = df['age'] > 30
cond
```




    0    False
    1     True
    2    False
    3     True
    4    False
    Name: age, dtype: bool




```python
df[~cond]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>18</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>22</td>
      <td>60000</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
