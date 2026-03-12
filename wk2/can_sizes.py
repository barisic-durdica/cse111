import math
def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    efficiency = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency = {efficiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    can_efficiency(name, radius, height)

    can_efficiency("#2", 8.73, 11.59)
    can_efficiency("#2.5", 10.32, 11.91)
    can_efficiency("#3 Cylinder", 10.79, 17.78)

def can_efficiency(name, radius, height):
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    efficiency = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency = {efficiency:.2f}")

def can_vol(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def can_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

main()    