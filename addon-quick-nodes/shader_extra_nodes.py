import bpy

class ShaderMixFloatOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_float_mix_node"
    bl_label = "Mix / Lerp (Float)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'FLOAT'
        return {'FINISHED'}
    

class ShaderMixVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_vector_mix_node"
    bl_label = "Mix / Lerp (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'VECTOR'
        return {'FINISHED'}

class ShaderMixColorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_color_mix_node"
    bl_label = "Mix / Lerp (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'RGBA'
        return {'FINISHED'}
    
class ShaderSeparateVector(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_separate_vector_node"
    bl_label = "Split / Separate (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeSeparateXYZ')
        return {'FINISHED'}
    
class ShaderSeparateColor(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_separate_color_node"
    bl_label = "Split / Separate (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeSeparateColor')
        return {'FINISHED'}