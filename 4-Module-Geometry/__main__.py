#!/usr/bin/env python
# coding: utf-8

# In[32]:


import nose

def test_module():

    print("***** Geometry Calulator *****\n",'### menu ###\n', 'p - perimeter\n',
         'a - area\n', 'v - volume\n', 'b - busbar\n', 'pytha - pythagorean theorem\n')

    user_menu = str(input())

    if user_menu == 'p':

        import perimeter as p

        print("### perimeter - shape ###\nYou can type\nsquare, rectangle, circle, triangle, parrelleogram, circular sector, trapezoid\n")

        shape = str(input())

        if shape == 'square':

            print("type - s")
            s = int(input())
            print(p.square(s))

        elif shape == 'rectangle':

            print("type - a, b")
            a = int(input())
            b = int(input())
            print(p.rectangle(a,b))

        elif shape == 'circle':

            print("type - r")
            r = int(input())
            print(p.circle(r))

        elif shape == 'triangle':

            print("type - a, b, c")
            a = int(input())
            b = int(input())
            c = int(input())
            print(p.triangle(a,b,c))

        elif shape == 'parallelogram':

            print("type - a, b")
            a = int(input())
            b = int(input())
            print(p.parallelogram(a,b))

        elif shape == 'circular sector':

            print("type - r, seta")
            r = int(input())
            seta = int(input())
            print(p.circular_sector(r, seta))

        elif shape == 'trapezoid':

            print("type - a, b, c, d")
            a = int(input())
            b = int(input())
            c = int(input())
            d = int(input())
            print(p.trapezoid(a,b,c,d))

    elif user_menu == 'a':

        import area as ar

        print("### area - shape ###\nYou can type\nsquare, rectangle, circle, triangle, parallelogram, circular sector, circular ring, trapezoid, rectangular box, right circular cone, cube, cylinder\n")

        shape = str(input())

        if shape == 'square':

            print("type - s")
            s = int(input())
            print(ar.square(s))

        elif shape == 'rectangle':

            print("type - a, b")
            a = int(input())
            b = int(input())
            print(ar.rectangle(a,b))

        elif shape == 'circle':

            print("type - r")
            r = int(input())
            print(ar.circle(r))

        elif shape == 'triangle':

            print("type - b, h")
            b = int(input())
            h = int(input())
            print(ar.triangle(b, h))

        elif shape == 'parallelogram':

            print("type - b, h")
            b = int(input())
            h = int(input())
            print(ar.parallelogram(b, h))

        elif shape == 'circular sector':

            print("type - r, seta")
            r = int(input())
            seta = int(input())
            print(ar.circular_sector(r, seta))

        elif shape == 'circular ring':

            print("type - R, r")
            R = int(input())
            r = int(input())
            print(ar.circular_ring(R, r))

        elif shape == 'trapezoid':

            print("type - h, a, b")
            h = int(input())
            a = int(input())
            b = int(input())
            print(ar.trapezoid(h,a,b))

        elif shape == 'rectangular box':

            print("type - a, b, c")
            a = int(input())
            b = int(input())
            c = int(input())
            print(ar.rectangular_box(a, b, c))

        elif shape == 'right circular cone':

            print("type - r, s")
            r = int(input())
            s = int(input())
            print(ar.right_circular_cone(r,s))

        elif shape == 'cube':

            print("type - l")
            l = int(input())
            print(ar.cube(l))

        elif shape == 'cylinder':

            print("type - r, h")
            r = int(input())
            h = int(input())
            print(ar.cylinder(r,h))

    elif user_menu == 'v':

        import volume as v

        print("### volume - shape ###\nYou can type\nsphere, rectangular box, right circular cone, cube, cylinder, frustum of a cone\n")

        shape = str(input())

        if shape == 'sphere':

            print("type - r")
            r = int(input())
            print(v.sphere(r))

        elif shape == 'rectangular box':

            print("type - a, b, c")
            a = int(input())
            b = int(input())
            c = int(input())
            print(v.rectangular_box(a,b,c))

        elif shape == 'right circular cone':

            print("type - r, h")
            r = int(input())
            h = int(input())
            print(v.right_circular_cone(r,h))

        elif shape == 'cube':

            print("type - l")
            l = int(input())
            print(v.cube(l))

        elif shape == 'cylinder':

            print("type - r, h")
            r = int(input())
            h = int(input())
            print(v.cyliner(r,h))

        elif shape == 'frustum of a cone':

            print("type - r, R, h")
            r = int(input())
            R = int(input())
            h = int(input())
            print(v.frustum_of_a_cone(r,R,h))

    elif user_menu == 'pytha':

        import pythagorean as pytha

        print("### pythagorean - shape ###\nYou can type\npythagorean theorem\n")

        shape = str(input())

        if shape == 'pythagorean theorem':

            print("type - a, b")
            a = int(input())
            b = int(input())
            print(pytha.pythagorean_theorem(a,b))

    elif user_menu == 'b':

        import busbar as bb

        print("### busbar - shape ###\nYou can type\nright circular cone\n")

        shape = str(input())

        if shape == 'right circular cone':

            print("type - r, h")
            r = int(input())
            h = int(input())
            print(bb.right_circular_cone(r,h))
            
if __name__ == '__main__':
    print("NOSE - Run Module")
    nose.runmodule()


# In[ ]: