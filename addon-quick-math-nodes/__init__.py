bl_info = {
    "name": "Quick Math Nodes",
    "author": "Fingar Bøen",
    "version": (1, 0, 1),
    "blender": (4, 0, 0),
    "location": "Shader Editor",
    "description": "Adds create menu entries for quick math operations.",
    "category": "Node",
}

import bpy
import importlib
import inspect
from . import vector_math_nodes, math_nodes, extra_nodes

# Reload modules if they are already loaded (useful during development)
if "vector_math_nodes" in locals():
    importlib.reload(vector_math_nodes)

if "math_nodes" in locals():
    importlib.reload(math_nodes)

if "extra_nodes" in locals():
    importlib.reload(extra_nodes)

# Combine all classes
all_classes = [cls for name, cls in inspect.getmembers(math_nodes) if inspect.isclass(cls) and issubclass(cls, bpy.types.Operator)]
all_classes += [cls for name, cls in inspect.getmembers(vector_math_nodes) if inspect.isclass(cls) and issubclass(cls, bpy.types.Operator)]
all_classes += [cls for name, cls in inspect.getmembers(extra_nodes) if inspect.isclass(cls) and issubclass(cls, bpy.types.Operator)]


# Custom menu stuff
class NODE_MT_CustomMenu(bpy.types.Menu):
    bl_label = "Quick Math Nodes"
    bl_idname = "NODE_MT_CustomMenu"
    
    def draw(self, context):
        layout = self.layout

        for cls in all_classes:
            if hasattr(cls, "bl_idname") and hasattr(cls, "bl_label"):
                layout.operator(cls.bl_idname, text=cls.bl_label)

def shader_node_menu_func(self, context):
    layout = self.layout
    layout.menu("NODE_MT_CustomMenu")

# Resigter / Unregister
def register():
    for cls in all_classes:
        bpy.utils.register_class(cls)

    bpy.utils.register_class(NODE_MT_CustomMenu)
    bpy.types.NODE_MT_add.append(shader_node_menu_func)

def unregister():
    bpy.types.NODE_MT_add.remove(shader_node_menu_func)
    bpy.utils.unregister_class(NODE_MT_CustomMenu)

    for cls in all_classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
