from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30

# 线性方程组
# 例如：
# |-Ax+By+Cz=k1
# |-Dx+Ey+Fz=k2
# |-Gx+Hy+Iz=k3
# |-...
class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    # planes 平面对象构成的list
    def __init__(self, planes):
        # 这个try except是确保所有平面都在同一个纬度空间
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    # 交换方程式位置
    def swap_rows(self, row1, row2):
        self[row1],self[row2] = self[row2],self[row1]

    # 对一个方程式进行乘法(只能是乘以非零数字)
    # coefficient 系数
    # row 第几行
    def multiply_coefficient_and_row(self, coefficient, row):
        if(coefficient == 0):
            print('请使用非零系数')
        else:
            #自己完成代码
            n = Vector([x*coefficient for x in self[row].normal_vector.coordinates]) # 乘以系数后的新的法向量
            c = self[row].constant_term * coefficient # 乘以系数后的新的常数项
            self[row] = Plane(normal_vector=n, constant_term=c)
            # return Plane(normal_vector=n, constant_term=c) #返回一个新的平面

            #标准答案
            # n = self[row].normal_vector
            # k = self[row].constant_term
            # new_normal_vector = n.times_scalar(coefficient)
            # new_constant_term = k*coefficient
            # self[row] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)

    # 把一个方程式进行倍数后加到另一个方程式
    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        if(coefficient == 0):
            print('请使用非零系数')
        else:
            #自己完成代码
            self.multiply_coefficient_and_row(coefficient, row_to_add) #对第row_to_add个方程式倍数运算，产生一个新的平面
            newPlane = self[row_to_add]
            addedPlane = self[row_to_be_added_to] # 取出需要被运算的方程式

            nv = newPlane.normal_vector
            ct = newPlane.constant_term
            n = nv.plus(addedPlane.normal_vector) #向量加法返回的就是一个向量对象，所以不用Vector()
            c = ct + addedPlane.constant_term
            self[row_to_be_added_to] = Plane(normal_vector=n, constant_term=c) 

            #标准答案
            # n1 = self[row_to_add].normal_vector
            # n2 = self[row_to_be_added_to].normal_vector
            # k1 = self[row_to_add].constant_term
            # k2 = self[row_to_be_added_to].constant_term
            # new_normal_vector = n1.times_scalar(coefficient).plus(n2)
            # new_constant_term = k1 * coefficient + k2
            # self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector,constant_term=new_constant_term)

    # 找出每一个方程式中的第一个非零项
    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self) #该方程组中的方程式数量
        num_variables = self.dimension

        # 初始化一个list
        indices = [-1] * num_equations

        # 把每一个方程式的第一个非零项的位置index放入indices list； 该函数会有助于寻找每个方程式中的主变量
        # 例如 Ax+Cz=k1 是第一个方程式，则indices[0] = 0; By+Cz=k2是第二个方程式,则indices[1] = 1
        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates) # 这里修改过，从课程下载下来的原始代码是n = self.normal_vector
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    # 返回方程组的方程式数量（亦即平面数量）
    def __len__(self):
        return len(self.planes)

    # 获取方程组中的某一个方程式（亦即某一个平面）
    def __getitem__(self, i):
        return self.planes[i]

    # 给方程组中的某一个方程式（亦即某一个平面）赋值
    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

s = LinearSystem([p0,p1,p2,p3])

# print(s.indices_of_first_nonzero_terms_in_each_row())
# print('{}\n{}\n{}\n{}'.format(s[0],s[1],s[2],s[3]))
# print('linear system length is ',len(s))
# print(s)

# s[0] = p1
# print(s)

# print('1e-9 is near zero:',MyDecimal('1e-9').is_near_zero())
# print('1e-11 is near zero:',MyDecimal('1e-11').is_near_zero())

# s.swap_rows(1,3)
# print(s)

# s.multiply_coefficient_and_row(2,1)
# print(s)

# s.add_multiple_times_row_to_row(-1,1,2);
# print(s)

s.swap_rows(0,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 1 failed')

s.swap_rows(1,3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print('test case 2 failed')

s.swap_rows(3,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 3 failed')

s.multiply_coefficient_and_row(1,0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 4 failed')

s.multiply_coefficient_and_row(-1,2)
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 5 failed')

s.multiply_coefficient_and_row(10,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 6 failed')

s.add_multiple_times_row_to_row(0,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 7 failed')

s.add_multiple_times_row_to_row(1,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 8 failed')

s.add_multiple_times_row_to_row(-1,1,0)
if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
        s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 9 failed')