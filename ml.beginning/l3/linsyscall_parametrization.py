from linsys import LinearSystem
from plane import Plane
from vector import Vector
from decimal import Decimal, getcontext

p1 = Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714')
p2 = Plane(normal_vector=Vector(['-0.138','-0.138','0.244']), constant_term='0.319')
s = LinearSystem([p1,p2])
print(s.compute_solution_with_prametrize())

p1 = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')
s = LinearSystem([p1,p2,p3])
print(s.compute_solution_with_prametrize())

p1 = Plane(normal_vector=Vector(['0.935','1.76','-9.365']), constant_term='-9.955')
p2 = Plane(normal_vector=Vector(['0.187','0.352','-1.873']), constant_term='-1.991')
p3 = Plane(normal_vector=Vector(['0.374','0.704','-3.746']), constant_term='-3.982')
p4 = Plane(normal_vector=Vector(['-0.561','-1.056','5.619']), constant_term='5.973')
s = LinearSystem([p1,p2,p3])
print(s.compute_solution_with_prametrize())