import math

ab = int(input())
bc = int(input())

ac = (ab**2 + bc**2)**(1/2)

mc = ac/2

angle_cab = math.atan(bc/ab)


angle_mbc = round(math.degrees(math.acos((ab*bc)/(2*(mc**2)))+angle_cab))

print(f'{angle_mbc}\u00B0')


