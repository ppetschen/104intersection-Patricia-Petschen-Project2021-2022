#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## tests104
## File description:
## cone
##

import sys
import math

def print_help():

    print("USAGE")
    print("\t./104intersection opt xp yp zp xv yv zv p")
    print("\nDESCRIPTION")
    print("\topt\t\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("\t(xp, yp, zp)\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("\t(xv, yv, zv)\tcoordinates of a vector parallel to the light ray")
    print("\tp\t\tparameter: radius of the sphere, radius of the cylinder, or")
    print("\t\t\tangle formed by the cone and the Z-axis")

def sphere():
    print("Sphere of radius " + str(R))
    print("Line passing through the point (" + str(Xp) + ", " + str(Yp) + ", " + str(Zp) + ") and parallel to the vector (" + str(Xv) + ", " + str(Yv) + ", " + str(Zv) + ")")

    # 𝑥𝑣2+𝑦𝑣2+𝑧𝑣2𝑡2+2𝑥𝑝𝑥𝑣+𝑦𝑝𝑦𝑣+𝑧𝑝𝑧𝑣𝑡+𝑥𝑝2+𝑦𝑝2+𝑧𝑝2=𝑅2

    a = (Xv**2 + Yv**2 + Zv**2)
    b = 2 * (Xv * Xp + Yv * Yp + Zv * Zp)
    c = Xp**2 + Yp**2 + Zp**2 - R**2

    return(a, b, c)


def cylindre():
    print("Cylinder of radius " + str(R))
    print("Line passing through the point (" + str(Xp) + ", " + str(Yp) + ", " + str(Zp) + ") and parallel to the vector (" + str(Xv) + ", " + str(Yv) + ", " + str(Zv) + ")")
    
    a = Xv**2 + Yv**2
    b = 2 * (Xp * Xv + Yp * Yv)
    c = Xp**2 + Yp**2 - R**2

    return (a, b, c)


def cone():
    print("Cone with a " + str(R) + " degree angle")
    print("Line passing through the point (" + str(Xp) + ", " + str(Yp) + ", " + str(Zp) + ") and parallel to the vector (" + str(Xv) + ", " + str(Yv) + ", " + str(Zv) + ")")

    a = (Xv**2 + Yv**2) - (Zv**2 *math.tan(math.radians(R))**2)
    b = 2 * ((Xv * Xp) + (Yv * Yp)) - (2*(Zv * Zp) * math.tan(math.radians(R))**2)
    c = ((Xp**2 + Yp**2) - ((Zp**2) * math.tan(math.radians(R))**2))

    return (a, b, c)

if len(sys.argv) == 1:
    print("error: no parameters", file=sys.stderr)
    exit(84)

if sys.argv[1][0] == '-' and sys.argv[1][1] == 'h':
    print_help()
    exit(0)

if len(sys.argv) != 9:
    print("error: invalid number of parameters", file=sys.stderr)
    exit(84)

try:
    opt = int(sys.argv[1])
    Xp = int(sys.argv[2])
    Yp = int(sys.argv[3])
    Zp = int(sys.argv[4])
    Xv = int(sys.argv[5])
    Yv = int(sys.argv[6])
    Zv = int(sys.argv[7])
    R = int(sys.argv[8])
except ValueError:
    print("error: invalid non-integer parameter", file=sys.stderr)
    exit(84)

if opt < 1 or opt > 3:
    print("error: invalid parameter opt", file=sys.stderr)
    exit(84)

if opt == 1 :
    a, b, c = sphere()
elif opt == 2:
    a, b, c = cylindre()
elif opt == 3:
	a, b, c = cone()

delta = b**2 - 4 * a * c

if a == 0:
    print("There is an infinite number of intersection points.")
if (-b + (delta)) == 0 or (-b - (delta)) == 0 :
    exit(84)

if delta == 0:
    print("1 intersection point:")
    x1 = -b / (2 * a)
    print("(%.3f, %.3f, %.3f)" % (Xp + x1 * Xv, Yp + x1 * Yv, Zp + x1 * Zv))
elif delta < 0:
	print("No intersection point.")
elif delta > 0:
	print("2 intersection points:")
	x1 = ((-b) + math.sqrt(delta)) / (2 * a)
	x2 = ((-b) - math.sqrt(delta)) / (2 * a)
	print("(%.3f, %.3f, %.3f)" % (Xp + x1 * Xv, Yp + x1 * Yv, Zp + x1 * Zv))
	print("(%.3f, %.3f, %.3f)" % (Xp + x2 * Xv, Yp + x2 * Yv, Zp + x2 * Zv))

exit(0)