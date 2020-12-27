bl_info = {
    "name": "Pix Grid",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from . import Grid, PixGrid

#Register classes as an addon
def register():
    bpy.utils.register_class(PixGrid.Test_Panel)
    bpy.utils.register_class(PixGrid.MyProperties)
    bpy.utils.register_class(PixGrid.Test_Operator)
    print("Test Panel Registered")
    
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=PixGrid.MyProperties)

#unregister classes as an addon
def unregister():
    bpy.utils.unregister_class(PixGrid.Test_Panel)
    bpy.utils.unregister_class(PixGrid.MyProperties)
    bpy.utils.unregister_class(PixGrid.Test_Operator)
    print("Test Panel Unegistered")
    
    
if __name__ == "__main__":
    register()
