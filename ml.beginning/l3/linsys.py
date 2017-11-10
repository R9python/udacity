from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30

''' 线性方程组
 例如：
 |-Ax+By+Cz=k1
 |-Dx+Ey+Fz=k2
 |-Gx+Hy+Iz=k3
 |-...'''
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

    '''
     对一个方程式进行乘法(只能是乘以非零数字)
     coefficient 系数
     row 第几行 '''
    def multiply_coefficient_and_row(self, coefficient, row):
        if(coefficient == 0):
            print('请使用非零系数')
        else:
            #自己完成代码
            # n = Vector([x*coefficient for x in self[row].normal_vector.coordinates]) # 乘以系数后的新的法向量
            # c = self[row].constant_term * coefficient # 乘以系数后的新的常数项
            # self[row] = Plane(normal_vector=n, constant_term=c)

            #标准答案
            n = self[row].normal_vector
            k = self[row].constant_term
            new_normal_vector = n.times_scalar(coefficient)
            new_constant_term = k*coefficient
            self[row] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)

    '''把一个方程式进行倍数后加到另一个方程式'''
    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        if(coefficient == 0):
            print('')
        else:
            #自己完成代码 （针对linsyscall_step2.py 会出现 test case 3 failed）
            # self.multiply_coefficient_and_row(coefficient, row_to_add) #对第row_to_add个方程式倍数运算，产生一个新的平面
            # newPlane = self[row_to_add]
            # addedPlane = self[row_to_be_added_to] # 取出需要被运算的方程式

            # nv = newPlane.normal_vector
            # ct = newPlane.constant_term
            # n = nv.plus(addedPlane.normal_vector) #向量加法返回的就是一个向量对象，所以不用Vector()
            # c = ct + addedPlane.constant_term
            # self[row_to_be_added_to] = Plane(normal_vector=n, constant_term=c) 

            #标准答案
            n1 = self[row_to_add].normal_vector
            n2 = self[row_to_be_added_to].normal_vector
            k1 = self[row_to_add].constant_term
            k2 = self[row_to_be_added_to].constant_term
            new_normal_vector = n1.times_scalar(coefficient).plus(n2)
            new_constant_term = k1 * coefficient + k2
            self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector,constant_term=new_constant_term)

    '''找出每一个方程式中的第一个非零项,返回一个list'''
    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self) #该方程组中的方程式数量
        num_variables = self.dimension

        # 初始化一个list
        indices = [-1] * num_equations

        # 把每一个方程式的第一个非零项的位置index放入indices list,即list； 该函数会有助于寻找每个方程式中的主变量
        # 例如  Ax+Cz=k1 是第一个方程式，则indices[0] = 0 (indices[0]表示第一个方程式); 
        #      By+Cz=k2是第二个方程式,则indices[1] = 1 (indices[1]表示第二个方程式)
        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates) # 这里修改过，从课程下载下来的原始代码是n = self.normal_vector
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    '''使方程组形成三角形'''
    def compute_triangular_form(self):
        system = deepcopy(self)

        num_equations = len(self) #该方程组中的方程式数量
        num_variables = self.dimension #变量的数量
        j=0

        for i in range(num_equations):
           while j < num_variables:
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    #交换方程式上下位置
                    swap_succeeded = system.swap_with_row_below_for_noezero_coefficient_if_able(i,j)
                    if not swap_succeeded: #如果交换不成功（表明该变量在下面的方程式中已经不存在了），则处理下一个变量
                        j += 1
                        continue
            
                #清除下面方程式的对应变量
                system.clear_coefficients_below(i,j)
                j += 1
                break

        return system

    '''形成rref梯阵形式：
    首项系数都为1；并且该系数在其它方程式中不存在
    '''
    def compute_rref(self):
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(num_equations)[::-1]:
            j = pivot_indices[i] # 表示第i个方程式的第一个非零系数的位置 2y+2z=4, 则j=1
            if j < 0: # -1表示没找到,因为该方程式为0=0,或者0=k
                continue

            # c = self[i].normal_vector.coordinates[j] #把这个系数的具体值取出来,则为2
            # self.multiply_coefficient_and_row(Decimal('1.0')/c, i)
            tf.scale_row_to_make_coefficient_equal_one(i,j)
            tf.clear_coefficients_above(i,j)
        
        return tf


        
    def scale_row_to_make_coefficient_equal_one(self, row, col):
        try:
            v = self[row].normal_vector.coordinates[col]
            beta = Decimal('1.0') / v
            self.multiply_coefficient_and_row(beta,row)
        except ZeroDivisionError:
            print("")

    def clear_coefficients_above(self, row, col):
        for i in range(row)[::-1]:
            beta = MyDecimal(self[i].normal_vector.coordinates[col]) #例如 -x-y-z=1 这里就是取-1
            alpha = -beta
            self.add_multiple_times_row_to_row(alpha, row, i)
        

    '''交换方程式上下位置'''
    def swap_with_row_below_for_noezero_coefficient_if_able(self,row,col):
        num_equations = len(self) #该方程组中的方程式数量
        
        for i in range(row+1,num_equations):
            c = MyDecimal(self[i].normal_vector.coordinates[col])
            if not c.is_near_zero():
                self.swap_rows(row,i)
                return True
        
        return False


    '''清除下面方程式的对应变量'''
    def clear_coefficients_below(self,row,col):
        num_equations = len(self) #该方程组中的方程式数量
        beta = MyDecimal(self[row].normal_vector.coordinates[col]) #例如 -x-y-z=1 这里就是取-1

        for i in range(row+1, num_equations):
            c = self[i].normal_vector.coordinates[col] #例如第二个方程式是 -2x+y+z=2, 这里就是-2，下面要想如何让-2变为0 (加上 c * -1)
            #然后计算 第一个方程式的-1 要乘以多少变为 num1
            alpha = -c/beta
            self.add_multiple_times_row_to_row(alpha,row, i)

    def compute_solution(self):
        try:
            return self.do_gaussian()
        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG or str(e) == self.INF_SOLUTIONS_MSG :
                return str(e)
            else:
                raise e

    # 首先计算rref
    # 然后检查是否存在矛盾 0=k
    # 然后检查是否存在太多主变量
    # 上述情况都不存在，则返回唯一交点（向量形式）
    def do_gaussian(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()
        rref.raise_exception_if_too_few_pivots()

        num_equations = len(rref.planes)
        solution_coordinates = [rref.planes[i].constant_term for i in range(num_equations)]
        return Vector(solution_coordinates)

    def compute_solution_with_prametrize(self):
        try:
            return self.do_gaussian_with_prametrize()
        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG or str(e) == self.INF_SOLUTIONS_MSG :
                return str(e)
            else:
                raise e

    
    def do_gaussian_with_prametrize(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()

        #不同的在这里，上面是抛出异常，现在需要实例化为parametrize输出
        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()
        return Parametrization(basepoint, direction_vectors)

    # 输出参数化形式的方向向量，返回是list (还未理解，需要再反复看几遍)？
    def extract_direction_vectors_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indicies = set(range(num_variables)) - set(pivot_indices)

        direction_vectors = []
        for free_var in free_variable_indicies:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var]
            direction_vectors.append(Vector(vector_coords))
        
        return direction_vectors

    # 输出基准向量，返回是Vector (还未理解，需要再反复看几遍)？
    def extract_basepoint_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coodrs = [0] * num_variables

        for i, p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coodrs[pivot_var] = p.constant_term

        return Vector(basepoint_coodrs)

    # 检查是否存在矛盾 0=k；
    # 先查找左侧，即法向量； 再查找右侧，即常量；
    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG: #first_nonzero_index 返回这个message表示方程式法向量全是0
                    c = MyDecimal(p.constant_term)
                    if not c.is_near_zero(): #出现0=k
                        raise Exception(self.NO_SOLUTIONS_MSG) #无解
                else:
                    raise e


    # 检查是否存在太多主变量
    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index>=0 else 0 for index in pivot_indices])
        num_variables = self.dimension
        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG) #解为一条直线




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

# 直线的参数化类
# basepoint 基点
# direction_vectors方向向量的list
class Parametrization(object):
    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension
        except AssertionError:
            raise Exception("The basepoint and direction vectors should all live in the same dimension.")

    def __str__(self):
        basepoint_str  = '\nbasepoint : {}'.format(self.basepoint.coordinates) + ';\n'
        direction_vectors_str = ''
        for v in self.direction_vectors:
            direction_vectors_str += 'direction_vectors : {}'.format(self.direction_vectors[0])
        return basepoint_str + 'direction_vectors : {}'.format(v)

    # def __str__(self):
    #     ret = 'Linear System:\n'
    #     temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.direction_vectors)]
    #     ret += '\n'.join(temp)
    #     return ret
    

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
