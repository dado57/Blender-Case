#CreaPath.py

import bpy
from mathutils import Vector

# cancella curve
for cur in bpy.data.curves:
    print(cur.name)
    bpy.data.curves.remove(cur)


coords_list = [
[  8, -4,  0],[  8,  2,  0],[  2,  2,  0],[  2, 16,  0],
[  8, 16,  0],[  8, 10,  0],[  6, 10,  0],[  6,  6,  0],
[ 12,  6,  0],[ 12, 12,  0],[ 10, 12,  0],[ 10, 16,  0],
[ 16, 16,  0],[ 16,  2,  0],[ 10,  2,  0],[ 10, -4,  0]]

# make a new curve
crv = bpy.data.curves.new('crv', 'CURVE')
crv.dimensions = '3D'

# make a new spline in that curve
#spline = crv.splines.new(type='NURBS') # arrotondata
spline = crv.splines.new(type='POLY')   # dritta

# a spline point for each point
spline.points.add(len(coords_list)-1) # theres already one point by default

#usa anche la prima e l'ultima coordinata
spline.use_endpoint_u = True
spline.use_endpoint_v = True

# assign the point coordinates to the spline points
for p, new_co in zip(spline.points, coords_list):
    p.co = (new_co + [1.0]) # (add nurbs weight)

# make a new object with the curve
obj = bpy.data.objects.new('Percorso', crv)
#bpy.context.scene.objects.link(obj) # per 7.xx
bpy.context.scene.collection.objects.link(obj) # per 8.81