bl_info = {
    "name": "Quick Nodes",
    "author": "Fingar Bøen",
    "version": (1, 1, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor, Geometry Node Editor",
    "description": """
        Uses Blender 4.0's new search functionality to increase productivity 
        in node editors by adding a bunch of new entries in the Add-menu. 
        You can now search for nodes like 'Add', 'Multiply', 'Dot Product', 
        'Lerp', etc., and this addon will create the correct blender node 
        with the correct settings for that function.
    """,
    "category": "Node",
}

import bpy
import importlib
import inspect

module_names = [
    "math_nodes",
    "vector_math_nodes",
    "extra_nodes",
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
    bl_label = "Quick Nodes"
    bl_idname = "NODE_MT_CustomMenu"
    
    def draw(self, context):
        layout = self.layout

        if context.space_data.node_tree is not None:
            for cls in all_classes:
                if hasattr(cls, "bl_idname") and hasattr(cls, "bl_label"):
                    layout.operator(cls.bl_idname, text=cls.bl_label)
        else:
            layout.label(text="No active node tree", icon='ERROR')            


def shader_node_menu_func(self, context):
    layout = self.layout
    if context.space_data.tree_type in {'ShaderNodeTree', 'GeometryNodeTree'}:
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
