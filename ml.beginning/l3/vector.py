from functools import reduce
from decimal import Decimal, getcontext
import math
getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
        except ValueError:
            print("value error!")
        except TypeError:
            print("type error!")

    #加法
    def plus(self,v):
        #将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        #a = [1,2,3]
        #b = [4,5,6]
        #zipped = zip(a,b)  => [(1, 4), (2, 5), (3, 6)]
        l = zip(self.coordinates, v.coordinates)
        return Vector([x+y for x,y in l])

    #减法
    def minus(self,v):
        l = zip(self.coordinates, v.coordinates)
        return Vector([x-y for x,y in l])

    #标量乘法
    def times_scalar(self,c):
        return Vector([x*Decimal(c) for x in self.coordinates])

    #向量大小
    def magnitude(self):
        r = reduce(fAdd, [x*x for x in self.coordinates])
        return math.sqrt(r)

    #向量大小 方法2
    #def magnitudeV2(self):
    #    r = [x**2 for x in self.coordinates]
    #    return math.sqrt(sum(r))

    #单位向量(即向量标准化)
    def normalized(self):
        try:
            c = self.magnitude() #计算向量大小
            return self.times_scalar(Decimal('1.0')/Decimal(c)) #对向量进行标量乘法
        except ZeroDivisionError:
            raise Exception('无法处理0向量')

    #点积(内积),返回是一个数
    def dot(self,v):
        l = zip(self.coordinates, v.coordinates)
        return sum([x*y for x,y in l])

    #两个向量夹角的余弦
    def angle(self,v):
        try:
            #点积
            dotValue = self.dot(v) 
            #两个向量的大小相乘
            magnitudeValue = self.magnitude() * v.magnitude()

            #acos的值范围是-1 to 1
            adjustValue = min(1,max(Decimal(dotValue)/Decimal(magnitudeValue),-1))
            a = math.acos(adjustValue) #弧度表示
            b = a*(180./math.pi) #由弧度转换为角度表示
            return a,b 
        except ZeroDivisionError:
            raise Exception("无法处理0向量")

    #两个向量是否平行
    def isParallelTo(self,v):
        try:
            p = True
            a = round(self.coordinates[0]/v.coordinates[0],3) 
            for i in range(len(self.coordinates)):
                if(round(self.coordinates[i]/v.coordinates[i],3) != a):
                    p =False
            return p
        except ZeroDivisionError:
            raise Exception('无法处理0向量')

    #两个向量是否平行V2
    def isParallelToV2(self,v):
        return (self.isZero() or 
                v.isZero() or 
                self.angle(v)[1] ==0 or 
                self.angle(v)[1] == math.pi)

    #判断是否是零向量
    def isZero(self,tolerance=1e-10):
        return self.magnitude() < tolerance
            

    #两个向量是否正交(垂直)
    def isOrthogonalTo(self,v):
        a = abs(round(self.dot(v),5)) 
        return a == 0

    #两个向量是否正交(垂直)V2
    def isOrthogonalToV2(self,v,tolerance=1e-10):
        return abs(self.dot(v)) <  tolerance

    #向量self在向量basis上的投影向量
    def component_paralle_to(self,basis):
        u = basis.normalized() #对向量basis计算单位向量
        num = self.dot(u) #向量self与上面的单位向量计算点积，得到一个数
        return u.times_scalar(num) #标量乘法

    #与向量self的投影相正交（垂直）的向量
    def component_orthogonal_to(self,basis):
        proj = self.component_paralle_to(basis) #计算v在b上的投影向量
        return self.minus(proj) #向量v = v投影+v正交 =》 v正交=向量v-v投影

    #计算两个向量组成的三角形的面积
    def area_of_triangle_with(self,v):
        return self.area_of_parallelogram_with(v) * 0.5

    #计算两个向量组成的平行四边形的面积
    def area_of_parallelogram_with(self,v):
        crossVector = self.cross(v)
        return crossVector.magnitude()

    #计算两个向量的向量积(外积) 方法1 公式法
    def cross(self,v):
        #x1,y1,z1 = self.coordinates[0],self.coordinates[1],self.coordinates[2]
        #x2,y2,z2 = v.coordinates[0],v.coordinates[1],v.coordinates[2]
        #上面的赋值简写为如下即可
        try:
            if(len(self.coordinates)==2):
                self.coordinates = self.coordinates + (0,)

            if(len(v.coordinates)==2):
                v.coordinates = v.coordinates + (0,)

            x1,y1,z1 = self.coordinates
            x2,y2,z2 = v.coordinates
            return Vector([y1*z2 - y2*z1, (x1*z2 - x2*z1)*-1, x1*y2 - x2*y1])
        except ValueError as e:
            raise e

    #计算两个向量的向量积(外积) 方法2 手算法
    def crossV2(self,v):
        if(len(self.coordinates)==2):
            self.coordinates = self.coordinates + (0,)

        if(len(v.coordinates)==2):
            v.coordinates = v.coordinates + (0,)

        #step1:写一遍,抄一遍
        a = self.coordinates + self.coordinates 
        b = v.coordinates + v.coordinates 

        #step2:去头尾    
        a1 = a[1:len(self.coordinates)*2-1]     
        b1 = b[1:len(v.coordinates)*2-1]
        
        #step3:画叉叉相乘相减
        resVector = []
        for i in range(len(a1)-1):
            num = a1[i]*b1[i+1] - a1[i+1]*b1[i]
            resVector.append(num)

        return Vector(resVector)



    #输出(print的时候会被调用)
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    #比较(==的时候会被调用)
    def __eq__(self,v):
        return self.coordinates == v.coordinates


def fAdd(x,y):
    return x+y
