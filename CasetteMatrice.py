# CasetteMatrice.py

import bpy
import random
import os
import ntpath

#
#  Testato su Window 10  
#
def dir(path): # ritorna la testa del percorso del file
    head, tail = ntpath.split(path)
    return head

Percorso = os.path.dirname(__file__)    # da "C:" fino a "nomefile.blend"
DirTex = (dir(Percorso)+'\\texture\\')  # toglie "nomefile.blend" e aggiunge "\texture\"

# Carica texture
P1M = bpy.data.images.load( DirTex + "P1M.png" )
P1C = bpy.data.images.load( DirTex + "P1C.png" )
P2M = bpy.data.images.load( DirTex + "P2M.png" )
P2C = bpy.data.images.load( DirTex + "P2C.png" ) 


# Cancello tutte le mesh
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete(use_global=False, confirm=False)

# Poi rimuovo i materiali
for m in bpy.data.materials:
    bpy.data.materials.remove(m)

# crea la mesh
def add_mesh(name, verts, faces, edges=None, col_name="Collection"):    
    if edges is None:
        edges = []
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections.get(col_name)
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)
    mesh.update()
    mesh.validate()
    # aggiunto per rendere l'oggetto attivo (il pivot_point è a (0,0)
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

# creo tetto a piramide 4 falde
def tettoP(x,y,lx,ly,hb,hc,ht): #h-base, h-cornicione , h-totale
    verts = [(x+lx,y+ly, hb), 
             (x+lx,y-ly, hb),
             (x-lx,y-ly, hb),
             (x-lx,y+ly, hb),
             (x+lx,y+ly, hb+hc), 
             (x+lx,y-ly, hb+hc),
             (x-lx,y-ly, hb+hc),
             (x-lx,y+ly, hb+hc),
             (x,y,hb+hc+ht) ]             
    faces = [[0, 1, 2, 3],
             [0, 1, 5, 4],
             [1, 2, 6, 5],
             [2, 3, 7, 6],
             [3, 0, 4, 7],
             [4,5,8],
             [5,6,8],
             [6,7,8],
             [7,4,8] ]             
    add_mesh("tettoP", verts, faces)
 
# creo tetto a terrazza
def tettoT(x,y,lx,ly,lc,hb,hc,ht): # lc larghezza connicione, h-base, h-cornicione , h-terrazzo
    verts = [(x+lx,y+ly, hb), 
             (x+lx,y-ly, hb),
             (x-lx,y-ly, hb),
             (x-lx,y+ly, hb),
             (x+lx,y+ly, hb+hc), 
             (x+lx,y-ly, hb+hc),
             (x-lx,y-ly, hb+hc),
             (x-lx,y+ly, hb+hc),
             (x+lx-lc,y+ly-lc, hb+hc), 
             (x+lx-lc,y-ly+lc, hb+hc),
             (x-lx+lc,y-ly+lc, hb+hc),
             (x-lx+lc,y+ly-lc, hb+hc),
             (x+lx-lc,y+ly-lc, hb+hc-ht), 
             (x+lx-lc,y-ly+lc, hb+hc-ht),
             (x-lx+lc,y-ly+lc, hb+hc-ht),
             (x-lx+lc,y+ly-lc, hb+hc-ht)
              ]             
    faces = [[0, 1, 2, 3],
             [0, 1, 5, 4],[1, 2, 6, 5],[2, 3, 7, 6],[3, 0, 4, 7],
             [4, 5, 9, 8],[5, 6, 10, 9],[6, 7, 11, 10],[7, 4, 8, 11],
             [8,12, 13, 9],[9, 13, 14,10],[10, 11, 15, 14],[8, 12,15, 11],
             [12, 13, 14, 15]  ]             
    add_mesh("tettoT", verts, faces)


def tettoS(x,y,lx,ly,ht,hc): #2 falde
    verts = [(x+lx,y+ly, ht), 
             (x+lx,y-ly, ht),
             (x-lx,y-ly, ht),
             (x-lx,y+ly, ht),
             (x+lx,y,ht+hc),
             (x-ly,y,ht+hc) ]             
    faces = [[0, 1, 2, 3],
             [0,4,1],
             [3,5,2],
             [1,2,5,4],
             [0,3,5,4] ]             
    add_mesh("tettoS", verts, faces)
 
def tettoI(x,y,lx,ly,ht,hc): # 1 falda
    verts = [(x+lx,y+ly, ht), 
             (x+lx,y-ly, ht),
             (x-lx,y-ly, ht),
             (x-lx,y+ly, ht),
             (x+lx,y+ly,ht+hc),
             (x-lx,y+ly,ht+hc) ]             
    faces = [[0, 1, 2, 3],
             [0,4,1],
             [3,5,2],
             [1,2,5,4],
             [0,3,5,4] ]             
    add_mesh("tettoI", verts, faces)
 

def CreaMateriale ( imageM ,imageC , Color) :
    mat = bpy.data.materials.new(name = 'm') 
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]

    # Crea nodo per texture 
    TeI = mat.node_tree.nodes.new('ShaderNodeTexImage')
    TeI.image = imageC 
        
    TeIA = mat.node_tree.nodes.new('ShaderNodeTexImage')
    TeIA.image = imageM

    mixer = mat.node_tree.nodes.new('ShaderNodeMixRGB')

    colore = mat.node_tree.nodes.new('ShaderNodeGamma')
    colore.inputs[0].default_value = Color
            
    mat.node_tree.links.new(  TeIA.outputs['Color'], mixer.inputs['Fac'] )
    mat.node_tree.links.new(   TeI.outputs['Color'], mixer.inputs[2] )
    mat.node_tree.links.new(colore.outputs['Color'], mixer.inputs[1] )
    mat.node_tree.links.new( mixer.outputs['Color'],  bsdf.inputs['Base Color'] )
    return mat

Angoli = [0.0 , 1.5708 , 3.14159 , 4.71239 ]


''' DATI INPUT '''
NX=10
NY=10
DC=2 # distanza case

#Altezza case 0-3
MH= [3,2,2,3,0,0,3,2,2,3,
     2,0,0,0,0,0,0,0,0,2,
     2,0,2,1,1,1,1,2,0,2,
     2,0,1,0,0,0,0,1,0,2,
     2,0,1,0,2,3,0,1,0,2,
     2,0,1,0,0,2,0,1,0,2,
     2,0,1,0,0,0,0,1,0,2,
     2,0,2,1,0,0,1,2,0,2,
     2,0,0,0,0,0,0,0,0,2,
     3,2,2,2,2,2,2,2,2,3]

# mappa tetto (1-8)
MT= [2,3,3,7,0,0,7,3,3,2,
     4,0,0,0,0,0,0,0,0,4,
     4,0,1,3,3,3,3,1,0,4,
     4,0,4,0,0,0,0,4,0,4,
     4,0,4,0,3,1,0,4,0,4,
     4,0,4,0,0,4,0,4,0,4,
     4,0,4,0,0,0,0,4,0,4,
     4,0,1,3,3,3,3,1,0,4,
     4,0,0,0,0,0,0,0,0,4,
     2,3,3,3,3,3,3,3,3,2]


SP=NX*DC+18

# Creo il piano
bpy.ops.mesh.primitive_plane_add(size=SP, enter_editmode=False, location=(SP/2-9, SP/2-9, 0))
mat = bpy.data.materials.new(name = 'mP')            # Crea il materiale
mat.diffuse_color = (0.5,0.3,0.3,0)                  # Assegna il colore
bpy.context.active_object.data.materials.append(mat) # Assegna il materiale all'oggetto attivo   


for xn in range(NX):
    for yn in range(NY): 
        
        # COLORE di tutta la casa        
        COLORE = (random.random(), random.random(),random.random(), 1) 
        # Crea materiali con texture per primo piano e successivi
        mat1 = CreaMateriale(P1M,P1C,COLORE)
        mat2 = CreaMateriale(P2M,P2C,COLORE) 
       
        # gira il cubo e quindi anche la texture       
        rr=random.randint(0,3)
        angolo=Angoli[rr]
         
        # zn=random.randint(0,3 ) #definisce altezza
        zn= MH [xn+yn*10]

        # Crea 1, 2 o 3 cubi
        if zn > 0 :
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(xn*DC, yn*DC, 1))
            bpy.ops.transform.resize(value=(2, 2, 2))
            bpy.context.active_object.data.materials.append(mat1) # Assegna il materiale all'oggetto attivo
            bpy.context.object.rotation_euler[2] = angolo
        if zn > 1 :
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(xn*DC, yn*DC, 3))
            bpy.ops.transform.resize(value=(2, 2, 2))
            bpy.context.active_object.data.materials.append(mat2) # Assegna il materiale all'oggetto attivo
            bpy.context.object.rotation_euler[2] = angolo
        if zn > 2 :
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(xn*DC, yn*DC, 5))
            bpy.ops.transform.resize(value=(2, 2, 2))
            bpy.context.active_object.data.materials.append(mat2) # Assegna il materiale all'oggetto attivo            
            bpy.context.object.rotation_euler[2] = angolo            

        #crea i tetti 
        if zn > 0 :
            tr=  MT [xn+yn*10]
            #tr=random.randint(1,4 )

            if tr == 1 :
                tettoP( xn*DC, yn*DC, 1.1 , 1.1 , zn*2 , 0.1, 1 ) # lar.X/2 , lar.Y/2 , h.base , h.cornicione , h.totale
  
            if tr == 2 :
                tettoT( xn*DC, yn*DC, 1.1 , 1.1 , 0.2 , zn*2 , 0.2, 0.18 ) # lc larghezza connicione, h-base, h-cornicione , h-terrazzo
    
            if tr == 3 :
                tettoS( 0.0, 0.0 , 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
            if tr == 4 :
                tettoS( 0.0, 0.0 , 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
                bpy.context.object.rotation_euler[2] = angolo=Angoli[1]

            if tr == 5 :
                tettoI( 0.0, 0.0, 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
            if tr == 6 :
                tettoI( 0.0, 0.0, 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
                bpy.context.object.rotation_euler[2] = angolo=Angoli[1]
            if tr == 7 :
                tettoI( 0.0, 0.0, 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
                bpy.context.object.rotation_euler[2] = angolo=Angoli[2]
            if tr == 8 :
                tettoI( 0.0, 0.0, 1.1 , 1.1 , zn*2 , 1 ) # lar.X/2 , lar.Y/2 , h.base , h.colmo
                bpy.ops.transform.translate(value=(xn*DC, yn*DC, 0))
                bpy.context.object.rotation_euler[2] = angolo=Angoli[3]

        mat = bpy.data.materials.new(name = 'mRxx')   # Crea il materiale
        mat.diffuse_color = (0.6+random.random()*0.4, random.random()*0.4, random.random()*0.4, 0)   
        bpy.context.active_object.data.materials.append(mat)       # Assegna il materiale all'oggetto
