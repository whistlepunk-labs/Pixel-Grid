<<<<<<< HEAD
import bpy
import math
#Version 0.1

class Grid:
    
    def __init__(self,width,height):
        #Width and height of array
        self.sizeX = width
        self.sizeY = height
        #instantiate 2d array for grid
        self.grid = [[0 for i in range(self.sizeY)] for j in range(self.sizeX)]
        self.instantiate_grid()
        

            

    #Instantiates the grid objects
    #arranges it as a flat, vertical standing grid
    def instantiate_grid(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                
                
                
                cubename = "GridCube ({0},{1})".format(x,y)
                
                #try to reuse cubes from earlier generation to save processing time
                try:
                    ob = bpy.data.objects[cubename]
                    print("Found object {0},{1}".format(x,y))
                except:
                    print("instantiating object {0},{1}".format(x,y))
                    #create cube
                    bpy.ops.mesh.primitive_cube_add()
                    #bpy.ops.mesh.primitive_ico_sphere_add(radius=.5,location=(x*1, 0, sizeY - y))
                    ob = bpy.context.active_object
                    ob.name = "GridCube ({0},{1})".format(x,y)
                    
                    
                ob.scale = (.35,.35,.35)
                ob.location = (x*1,0,self.sizeY-y)
                
                #add it to object array
                self.grid[x][y] = ob
                
                #create new matherial and add it to the object
                mat_name = "Grid-Material({0},{1})".format(x,y)
                mat = bpy.data.materials.new(name=mat_name)
                ob.data.materials.append(mat)
                
                #make the new material use nodes, 
                #then set those nodes to an emission shader by making links between the shader to the output
                mat.use_nodes = True
                node = mat.node_tree.nodes.new(type="ShaderNodeEmission")
                inp = bpy.data.materials[mat_name].node_tree.nodes['Material Output'].inputs['Surface']
                outp = bpy.data.materials[mat_name].node_tree.nodes['Emission'].outputs['Emission']
                bpy.data.materials[mat_name].node_tree.links.new(inp,outp)
                

    #draws the image onto the array of objects
    #draws only the topleft pixels of pictures
    def draw_image(self,image):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                node = self.grid[x][y].active_material.node_tree.nodes['Emission']
                
                pix = image.getpixel((x,y))
                print("Painting Pixel: {0},{1}".format(x,y))
                
                rgb = self.color_correct(pix,3)
                node.inputs[0].default_value = rgb
                
                
                
                
    #Converts image color to blender friendly tuple
    #gamma color corrects the image because apparently blender doesn't color correct rgb automatically
    def color_correct(self,color,gamma):
        
        r = pow(color[0]/255,gamma)
        g = pow(color[1]/255,gamma)
        b = pow(color[2]/255,gamma)
        a = 1
        return (r,g,b,a)
    
    
    #arrange grid as a cyllinder of wrapping pixels
    def arrange_as_cyllinder(self):
        radius = (self.sizeY/(math.pi*2))*2
        theta = math.radians(360/self.sizeX)
        
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                ob = self.grid[x][y]
                ob.location = (radius*math.cos(x*theta),radius*math.sin(x*theta),self.sizeY-y)
                ob.rotation_euler = (0,0,x*theta)
                
            
    
    
    
    
#clears the screen and all materials (Includes camera BEWARE!)
def clear():
    #delte all objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    #delete materials
    for material in bpy.data.materials:
        material.user_clear()
        bpy.data.materials.remove(material)
=======
import bpy
import math


class Grid:
    
    def __init__(self,width,height):
        #Width and height of array
        self.sizeX = width
        self.sizeY = height
        #instantiate 2d array for grid
        self.grid = [[0 for i in range(self.sizeY)] for j in range(self.sizeX)]
        self.instantiate_grid()
        

            

    #Instantiates the grid objects
    #arranges it as a flat, vertical standing grid
    def instantiate_grid(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                
                
                
                cubename = "GridCube ({0},{1})".format(x,y)
                
                #try to reuse cubes from earlier generation to save processing time
                try:
                    ob = bpy.data.objects[cubename]
                    print("Found object {0},{1}".format(x,y))
                except:
                    print("instantiating object {0},{1}".format(x,y))
                    #create cube
                    bpy.ops.mesh.primitive_cube_add()
                    #bpy.ops.mesh.primitive_ico_sphere_add(radius=.5,location=(x*1, 0, sizeY - y))
                    ob = bpy.context.active_object
                    ob.name = "GridCube ({0},{1})".format(x,y)
                    
                    
                ob.scale = (.35,.35,.35)
                ob.location = (x*1,0,self.sizeY-y)
                
                #add it to object array
                self.grid[x][y] = ob
                
                #create new matherial and add it to the object
                mat_name = "Grid-Material({0},{1})".format(x,y)
                mat = bpy.data.materials.new(name=mat_name)
                ob.data.materials.append(mat)
                
                #make the new material use nodes, 
                #then set those nodes to an emission shader by making links between the shader to the output
                mat.use_nodes = True
                node = mat.node_tree.nodes.new(type="ShaderNodeEmission")
                inp = bpy.data.materials[mat_name].node_tree.nodes['Material Output'].inputs['Surface']
                outp = bpy.data.materials[mat_name].node_tree.nodes['Emission'].outputs['Emission']
                bpy.data.materials[mat_name].node_tree.links.new(inp,outp)
                

    #draws the image onto the array of objects
    #draws only the topleft pixels of pictures
    def draw_image(self,image):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                node = self.grid[x][y].active_material.node_tree.nodes['Emission']
                
                pix = image.getpixel((x,y))
                print("Painting Pixel: {0},{1}".format(x,y))
                
                rgb = self.color_correct(pix,3)
                node.inputs[0].default_value = rgb
                
                
                
                
    #Converts image color to blender friendly tuple
    #gamma color corrects the image because apparently blender doesn't color correct rgb automatically
    def color_correct(self,color,gamma):
        
        r = pow(color[0]/255,gamma)
        g = pow(color[1]/255,gamma)
        b = pow(color[2]/255,gamma)
        a = 1
        return (r,g,b,a)
    
    
    #arrange grid as a cyllinder of wrapping pixels
    def arrange_as_cyllinder(self):
        radius = (self.sizeY/(math.pi*2))*2
        theta = math.radians(360/self.sizeX)
        
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                ob = self.grid[x][y]
                ob.location = (radius*math.cos(x*theta),radius*math.sin(x*theta),self.sizeY-y)
                ob.rotation_euler = (0,0,x*theta)
                
            
    
    
    
    
#clears the screen and all materials (Includes camera BEWARE!)
def clear():
    #delte all objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    #delete materials
    for material in bpy.data.materials:
        material.user_clear()
        bpy.data.materials.remove(material)
>>>>>>> cffe98dc2dc2b8ab9e1218d7020e1cbc17f2812f
