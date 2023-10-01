# Geometry nodes uses ShaderNode a lot of the time.
# So if Quick Nodes for Geometry Nodes break, its probably becayse they have updated the classes

import bpy

class GeometryMixFloatOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_float_mix_node"
    bl_label = "Mix / Lerp (Float)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'FLOAT'
        return {'FINISHED'}
    

class GeometryMixVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_vector_mix_node"
    bl_label = "Mix / Lerp (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'VECTOR'
        return {'FINISHED'}

class GeometryMixColorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_color_mix_node"
    bl_label = "Mix / Lerp (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'RGBA'
        return {'FINISHED'}
    
class GeometrySeparateVector(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_separate_vector_node"
    bl_label = "Split / Separate (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeSeparateXYZ')
        return {'FINISHED'}
    
class GeometrySeparateColor(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_separate_color_node"
    bl_label = "Split / Separate (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='FunctionNodeSeparateColor')
        return {'FINISHED'}