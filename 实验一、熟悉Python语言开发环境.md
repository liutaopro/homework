# **实验一、熟悉Python语言开发环境**

## 实验目的：

了解Python语言，熟悉课程所使用的Python语言开发环境

## 实验要求：

能编辑、运行给定的代码，熟练掌握集成开发环境

## 实验学时：

2学时

## 实验内容：

### 一、完成教材29页程序练习题1.1-1.6

#### 1.1 字符串拼接。接收用户输入的两个字符串，将它们组合后输出。

```python
str1 = input("请输入一个人的名字:")
str2 = input("请输入一个国家的名字:")
print("世界这么大，{}想去{}看看。".format(str1,str2))
```



#### 1.2 整数序列求和。用户输入一个正整数N，计算从1到N（包含1和N）相加后的结果。

```python
n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
	sum += i+1
print("1到N求和结果："，sum)
```



#### 1.3  九九乘法表输出。工整打印输出日常的九九乘法表， 格式不限。

```python
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end='')
    print('') 
```



#### 1.4 计算1+2！+3！+……+10!的结果。

```python
sum, tmp =0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运行结果是：{}".format(sum))
```



#### 1.5 猴子吃桃问题： 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到第五天早上想再吃时，就只剩下一个桃子了。请编写程序计算猴子第一天一共摘了多少桃子。

```python
n =1
for i in range(4,0,-1):
    n = (n+1)<<1
print(n)
```



#### 1.6  健康食谱输出， 列出5种不同食材，输出它们可能组成的所有菜式名称。

```python
diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
```



小结：这6道题的代码展示了Python语言的一些基本语法，要注意python语言中的缩进很重要，一旦写错了，程序就会出语法错误.

 

### 2、完成程序练习题1.7-1.8

#### 1.7 五角星的绘制： 绘制一个红色的五角星图形， 如图所示。

```python
from turtle import*
fillcolor("red")
begin_fill()
while True: 
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()        
```



#### 1.8 太阳花的绘制：绘制一个太阳花的图案，如图所示。

```python
from turtle import*
coclor('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
```

小结：这两道题展示了Python语言中的绘图功能，可以修改程序中的数据，观察绘制出的图形的不同点。

## 实验总结：

这是我第一次接触python 语言，了解到了这是一种被广泛运用的高级通用脚本编程语言。并且熟悉了课程所使用的Python语言开发环境。之前自己学习过一些C语言，直观的感觉就是python要比C简洁许多，但也有许多要注意的地方，比如要注意代码的缩进，代码的缩进代表语句的从属关系；键盘的中英文转化，编写代码要使用英文输入，不然就会出现一些意想不到的错误。并且python语言可以用来绘制图案，我感到十分的神奇，一行行代码最终转化为一个个不同的图案，非常得有意思，也有助于激发我们学习python语言的兴趣和积极性。