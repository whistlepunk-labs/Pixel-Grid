<<<<<<< HEAD
bl_info = {
    "name": "Pix Grid",
    "blender": (2, 80, 0),
    "category": "Object",
}

import Grid

import bpy
from PIL import Image
from bpy.props import (
                BoolProperty,  
                PointerProperty,
                IntProperty,
                StringProperty,
                EnumProperty,
                )                
from bpy.types import Panel, PropertyGroup, Operator


#class that holds the property values to be used by the panel
class MyProperties(PropertyGroup):
    
    #Property Objects
    checkbox: BoolProperty(
        name="Y/N?",
        description ="This should be a checkbox",
        default=False
        )
        
    size_x : IntProperty(
        name="Width (px)",
        description = "Width of image to be displayed\nWARNING:Anything over 10 will take a while to load",
        default=10,
        min=0
        )
        
    size_y : IntProperty(
        name="Height (px)",
        description="Height of image to be displayed\nWARNING:Anything over 10 will take a while to load",
        default=10,
        min=0
        )
        
    file_path : StringProperty(
        name = "File Path:",
        default = "",
        maxlen = 1024,
        subtype = "FILE_PATH",
        )
'''
#TODO: add animation
    animation_type: EnumProperty(
        name = "Animation Type"
'''
        



class Test_Operator(Operator):
    bl_label = "Generate Grid"
    bl_idname = "hello.world"
    
    def execute(self,context):
        scene = context.scene
        mytool = scene.my_tool
        
        im = Image.open(mytool.file_path)
        x = mytool.size_x
        y = mytool.size_y
        im = im.resize((x,y))
        
        grid = Grid.Grid(x,y)
        grid.draw_image(im)
        
        
        

        
        return {'FINISHED'}



#Panel Class
class Test_Panel(Panel):
    bl_label = "Pixel Grid"
    bl_idname = "test_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create"
    bl_context = "objectmode"
    
    #Draws the panel
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        #panel objects to be drawn
        layout.prop(mytool, "checkbox")
        layout.prop(mytool, "size_x")
        layout.prop(mytool, "size_y")
        layout.prop(mytool, "file_path")
        layout.operator("hello.world")



   
#Register classes as an addon
def register():
    bpy.utils.register_class(Test_Panel)
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(Test_Operator)
    print("Test Panel Registered")
    
    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

#unregister classes as an addon
def unregister():
    bpy.utils.unregister_class(Test_Panel)
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(Test_Operator)
    print("Test Panel Unegistered")
    
    
if __name__ == "__main__":
    register()
=======
bl_info = {
    "name": "Pix Grid",
    "blender": (2, 80, 0),
    "category": "Object",
}

import Grid

import bpy
from PIL import Image
from bpy.props import (
                BoolProperty,  
                PointerProperty,
                IntProperty,
                StringProperty,
                )                
from bpy.types import Panel, PropertyGroup, Operator


#class that holds the property values to be used by the panel
class MyProperties(PropertyGroup):
    
    #Property Objects
    stupid_checkbox: BoolProperty(
        name="Y/N?",
        description ="This should be a checkbox",
        default=False
        )
        
    size_x : IntProperty(
        name="Width (px)",
        description = "Width of image to be displayed\nWARNING:Anything over 10 will take a while to load",
        default=10,
        min=0
        )
        
    size_y : IntProperty(
        name="Height (px)",
        description="Height of image to be displayed\nWARNING:Anything over 10 will take a while to load",
        default=10,
        min=0
        )
        
    file_path : StringProperty(
        name = "File Path:",
        default = "",
        maxlen = 1024,
        subtype = "FILE_PATH",
        )



class Test_Operator(Operator):
    bl_label = "Generate Grid"
    bl_idname = "hello.world"
    
    def execute(self,context):
        scene = context.scene
        mytool = scene.my_tool
        
        im = Image.open(mytool.file_path)
        x = mytool.size_x
        y = mytool.size_y
        im = im.resize((x,y))
        
        grid = Grid.Grid(x,y)
        grid.draw_image(im)
        
        
        

        
        return {'FINISHED'}



#Panel Class
class Test_Panel(Panel):
    bl_label = "Pixel Grid Ass"
    bl_idname = "test_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create"
    bl_context = "objectmode"
    
    #Draws the panel
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        #panel objects to be drawn
        layout.prop(mytool, "stupid_checkbox")
        layout.prop(mytool, "size_x")
        layout.prop(mytool, "size_y")
        layout.prop(mytool, "file_path")
        layout.operator("hello.world")



   
#Register classes as an addon
def register():
    bpy.utils.register_class(Test_Panel)
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(Test_Operator)
    print("Test Panel Registered")
    
    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

#unregister classes as an addon
def unregister():
    bpy.utils.unregister_class(Test_Panel)
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(Test_Operator)
    print("Test Panel Unegistered")
    
    
if __name__ == "__main__":
    register()
>>>>>>> cffe98dc2dc2b8ab9e1218d7020e1cbc17f2812f
