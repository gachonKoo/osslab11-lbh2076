import geo.utils as utils

# calculate the length of hypotenuse(c) when a=3 and b=4
a, b = 3, 4
c = utils.hypotenuse(a, b)  # hypotenuse 함수 호출
print("c =", c)

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle_area(r)  # circle_area 함수 호출
print("area =", area)

