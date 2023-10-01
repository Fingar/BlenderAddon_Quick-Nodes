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

module_names = [
    "shader_math_nodes",
    "shader_vector_math_nodes",
    "shader_extra_nodes",
]

# Import and optionally reload modules, then collect classes
all_classes = []
for name in module_names:
    # Reload if already loaded (useful during development)
    if name in locals():
        importlib.reload(locals()[name])
    
    # Import module
    module = importlib.import_module(f".{name}", __package__)
    
    # Collect classes from module
    all_classes.extend([
        cls for _, cls in inspect.getmembers(module)
        if inspect.isclass(cls) and issubclass(cls, bpy.types.Operator)
    ])

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
