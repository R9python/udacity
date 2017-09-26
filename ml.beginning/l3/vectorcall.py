from vector import Vector

#plus
v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])
print("v+w=", v.plus(w))

#minus
v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print("v-w=", v.minus(w))

#times_scalar
v = Vector([1.671,-1.012,-0.318])
print("v*c=", v.times_scalar(7.41))

#向量大小
v = Vector([-0.221,7.437])
print("v size=", v.magnitude())
v = Vector([8.813,-1.331,-6.247])
print("v size=", v.magnitude())

#单位向量(即向量标准化)
v = Vector([5.581,-2.136])
print("v normalized=", v.normalized())
v = Vector([1.996,3.108,-4.554])
print("v normalized=", v.normalized())

#点积
v = Vector(['7.887','4.138'])
w = Vector(['-8.802','6.776'])
print("v dot w=", v.dot(w))

#点积
v = Vector(['-5.955','-4.904','-1.874'])
w = Vector(['-4.496','-8.755','7.103'])
print("v dot w=", v.dot(w))

#余弦值,角度
v = Vector(['3.183','-7.627'])
w = Vector(['-2.668','5.319'])
print("v w a=", v.angle(w)[0], ",v w angle=", v.angle(w)[1])

#余弦值,角度
v = Vector(['7.35','0.221','5.188'])
w = Vector(['2.751','8.259','3.985'])
print("v w a=", v.angle(w)[0], ",v w angle=", v.angle(w)[1])

#向量平行和正交
v = Vector(['-7.579','-7.88'])
w = Vector(['22.737','23.64'])
print("v w parallel=", v.isParallelTo(w), ",v w orthogonal=", v.isOrthogonalTo(w))

#向量平行和正交
v = Vector(['-2.029','9.97','4.172'])
w = Vector(['-9.231','-6.639','-7.245'])
print("v w parallel=", v.isParallelTo(w), ",v w orthogonal=", v.isOrthogonalTo(w))

#向量平行和正交
v = Vector(['-2.328','-7.284','-1.214'])
w = Vector(['-1.821','1.072','-2.94'])
print("v w parallel=", v.isParallelTo(w), ",v w orthogonal=", v.isOrthogonalTo(w))

#向量平行和正交
v = Vector(['2.118','4.827'])
w = Vector(['0','0'])
print("v w parallel=", v.isParallelToV2(w), ",v w orthogonal=", v.isOrthogonalTo(w))

#计算向量v在b上的投影向量
v = Vector([3.039,1.879])
b = Vector([0.825,2.036])
print("v proj on basis=", v.component_paralle_to(b))

#计算与上面一个投影向量相正交的向量
v = Vector([-9.88,-3.264,-8.159])
b = Vector([-2.155,-9.353,-9.473])
print("v orthogonal on basis=", v.component_orthogonal_to(b))

#向量v分解为两个向量，一个是在b上的投影向量（平行），一个是在b上的正交向量（垂直）
v = Vector([3.009,-6.172,3.692,-2.51])
b = Vector([6.404,-9.144,2.759,8.718])
print("v proj on basis=", v.component_paralle_to(b), ",v orthogonal on basis=", v.component_orthogonal_to(b))

#计算两个向量的向量积(外积)
v = Vector(['8.462','7.893','-8.187'])
w = Vector(['6.984','-5.975','4.778'])
print("v cross w=", v.crossV2(w))

#计算两个向量组成的平行四边形的面积
v = Vector(['-8.987','-9.838','5.031'])
w = Vector(['-4.268','-1.861','-8.866'])
print("area of parallelogram=", v.area_of_parallelogram_with(w))

#计算两个向量组成的三角形的面积
v = Vector(['1.5','9.547','3.691'])
w = Vector(['-6.007','0.124','5.772'])
print("area of triangle=", v.area_of_triangle_with(w))