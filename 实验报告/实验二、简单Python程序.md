# **实验二、简单Python程序**

## 实验目的：

熟悉Python语言基本元素，了解Python语言函数库Turtle

## 实验要求：

​	1. 熟悉掌握Python语言基本元素，能仿照例题温度转换程序编写汇率兑换程序。

​	2. 基本掌握Turtle库的常用函数和用法，能绘制简单的图形

## 实验学时：

2学时

## 实验内容：

### 2.1 实例1的修改。改造实例代码1.1，采用eval(input(<提示内容>))替换现有输入部分，并使输出的温度值为整数。

```python
TempStr = input('请输入带有符号的温度：')
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print('转换后的温度是：{:.0f}C'.format(C))
elif TempStr[-1] in ['c','C']:
    F = 1.8*eval(TempStr[0:-1])+32
    print('转化后的温度是{：.0f}F'.format(F))
else:
    print("输入的格式错误")
```



### 2.2 汇率兑换程序。按照温度转换程序的设计思路，按照1美元=6 人民币汇率编写一个美元和人民币的双向兑换程序。

```python
MoneyStr = input('请输入带有符号的货币值：')
if MoneyStr[-1] in ['$']:
    C =eval(MoneyStr[0:-1])*6
    print("${:}=￥{:.2f}".format(eval(MoneyStr[:-1]),C))
elif MoneyStr[-1] in ['￥']:
    F = 1.8*eval(MoneyStr[0:-1])/6
    print("￥{:}=${:.2f}".format(eval(MoneyStr[:-1]),F))
else:
    print("输入格式错误")
```



### 2.3 实例2的修改。改造实例代码2.1，绘制一条彩色蟒蛇，即在绘制Python蟒蛇的每个小段时，画笔的绘制颜色会发生变化。

```python
from turtle import *
setup(660,360,100,100)
penup()
fd(-250)
pendown()
pensize(30)
seth(-40)
color=['red','pruple','green','yellow','blue']
for i in range(4):
    pencolor(color[i])
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40 * 2/3)
```



### 2.4 等边三角形的绘制。 使用turtle库中的trutle.fd()函数和trutle.seth()函数绘制一个等边三角形。

```python
from turtle import *
pensize(2)
fd(60)
left(120)
fd(60)
left(120)
fd(60)
```



### 2.5 叠加等边三角形的绘制。 使用turtle库中的turtle.fd()函数和turtle.seth()函数绘制一个叠加等边三角形。

```python
from turtle import *
def triangle():
    pd()
    pensize(3)
    fd(100)
    left(120)
    fd(100)
    left(120)
    fd(100)
    pu()
goto(0,0)
triangle()
goto(100,0)
triange()
goto(50,50*3**0.5)
triangle()
```



### 2.6 五角正方形的绘制。利用turtle库函数绘制一个没有角的正方形。

```python
from turtle import *
pensize(2)
for i in range(4):
	fd(25)
    pd()
    fd(50)
    pu()
    if i<3:
        fd(25)
        left(90)
```



### 2.7 六角形是绘制。 利用turtle库绘制一个六角形。

```python
from turtle import *
def triangle(time):
    pd()
    for i in range(3):
		fd(150)
    		if time ==2:
        left(120)
    		if time ==1:
        right(120)
    pu()
pensize(3)
left(30)
triangle(1)
goto(25*3**0.5,75)
seth(0)
right(90)
triangle(2)
fd(50)
left(120)

```



### 2.8 正方形螺旋线的绘制。利用turtle 库绘制正方形螺旋形。

```python
from turtle import *
len = 3
a = 100
pensize(1)
left(90)
pd()
while a:
    fd(len)
    left(90)
    len +=2
```

## 实验总结：

经过这次实验课，我们熟悉了Python语言基本元素，了解Python语言函数库Turtle。并且通过动手操作复习了课上学习的内容，这次我们照葫芦画瓢，尝试修改书上的实例代码，加深了我们对程序的理解。这节实验课我们使用turtle库绘制了更多的更复杂的图形，初步掌握了turtle库的基本函数的使用，在我们只引用turtle库绘制图形时，可以使用from <库名> import *的引用方式，这样就不用重复键入库名，提高了效率。为我们以后更好的绘制图形打下了基础。这次实验课我也发现我的打英文单词的速度很慢，所以需要加强打字速度的练习。
