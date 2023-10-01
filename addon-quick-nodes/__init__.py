bl_info = {
    "name": "Quick Nodes",
    "author": "Fingar Bøen",
    "version": (1, 1, 1),
    "blender": (4, 0, 0),
    "location": "Shader Editor, Geometry Node Editor, Compositor",
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


shader_module_names = [
    "shader_math_nodes",
    "shader_vector_math_nodes",
    "shader_extra_nodes",
]

geometry_module_names = [
    "geometry_math_nodes",
    "geometry_vector_math_nodes",
    "geometry_extra_nodes",
]

compositor_module_names = [
    "compositor_math_nodes",
    "compositor_extra_nodes",
]


# Import and optionally reload modules, then collect classes
all_classes = []
shader_classes = []
geometry_classes = []
compositor_classes = []


def collect_classes(module_names, target_list):
    for name in module_names:
        # Reload if already loaded (useful during development)
        if name in locals():
            importlib.reload(locals()[name])

        # Import module
        module = importlib.import_module(f".{name}", __package__)

        # Collect classes from module
        target_list.extend([
            cls for _, cls in inspect.getmembers(module)
            if inspect.isclass(cls) and issubclass(cls, bpy.types.Operator)
        ])

    all_classes.extend(target_list)


collect_classes(shader_module_names, shader_classes)
collect_classes(geometry_module_names, geometry_classes)
collect_classes(compositor_module_names, compositor_classes)


# Custom menu stuff
class NODE_MT_ShaderCustomMenu(bpy.types.Menu):
    bl_label = "Quick Shader Nodes"
    bl_idname = "NODE_MT_ShaderCustomMenu"
    
    def draw(self, context):
        layout = self.layout
        if context.space_data.node_tree is not None:
            for cls in shader_classes:
                if hasattr(cls, "bl_idname") and hasattr(cls, "bl_label"):
                    layout.operator(cls.bl_idname, text=cls.bl_label)
        else:
            layout.label(text="No active shader node tree", icon='ERROR')


class NODE_MT_GeometryCustomMenu(bpy.types.Menu):
    bl_label = "Quick Geometry Nodes"
    bl_idname = "NODE_MT_GeometryCustomMenu"

    def draw(self, context):
        layout = self.layout
        if context.space_data.node_tree is not None:
            for cls in geometry_classes:
                if hasattr(cls, "bl_idname") and hasattr(cls, "bl_label"):
                    layout.operator(cls.bl_idname, text=cls.bl_label)
        else:
            layout.label(text="No active geometry node tree", icon='ERROR')


class NODE_MT_CompositorCustomMenu(bpy.types.Menu):
    bl_label = "Quick Compositor Nodes"
    bl_idname = "NODE_MT_CompositorCustomMenu"

    def draw(self, context):
        layout = self.layout
        if context.space_data.node_tree is not None:
            for cls in compositor_classes:
                if hasattr(cls, "bl_idname") and hasattr(cls, "bl_label"):
                    layout.operator(cls.bl_idname, text=cls.bl_label)
        else:
            layout.label(text="No active compositor node tree", icon='ERROR')


def display_quick_node_menu(self, context):
    layout = self.layout
    if context.space_data.tree_type == 'ShaderNodeTree':
        layout.menu("NODE_MT_ShaderCustomMenu")
    elif context.space_data.tree_type == 'GeometryNodeTree':
        layout.menu("NODE_MT_GeometryCustomMenu")
    elif context.space_data.tree_type == 'CompositorNodeTree':
        layout.menu("NODE_MT_CompositorCustomMenu")


# Resigter / Unregister


def register():
    for cls in all_classes:
        bpy.utils.register_class(cls)

    bpy.utils.register_class(NODE_MT_ShaderCustomMenu)
    bpy.utils.register_class(NODE_MT_GeometryCustomMenu)
    bpy.utils.register_class(NODE_MT_CompositorCustomMenu)
    bpy.types.NODE_MT_add.append(display_quick_node_menu)


def unregister():
    bpy.types.NODE_MT_add.remove(display_quick_node_menu)
    bpy.utils.unregister_class(NODE_MT_ShaderCustomMenu)
    bpy.utils.unregister_class(NODE_MT_GeometryCustomMenu)
    bpy.utils.unregister_class(NODE_MT_CompositorCustomMenu)

    for cls in all_classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
