import bpy

class CompositorMixColorOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.add_color_mix_node"
    bl_label = "Mix / Lerp (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMixRGB')
        return {'FINISHED'}
    
class CompositorSeparateVector(bpy.types.Operator):
    bl_idname = "quick_compositor_node.add_separate_vector_node"
    bl_label = "Split / Separate (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeSeparateXYZ')
        return {'FINISHED'}
    
class CompositorSeparateColor(bpy.types.Operator):
    bl_idname = "quick_compositor_node.add_separate_color_node"
    bl_label = "Split / Separate (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeSeparateColor')
        return {'FINISHED'}