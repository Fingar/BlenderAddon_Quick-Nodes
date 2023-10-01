import bpy

class MixFloatOperator(bpy.types.Operator):
    bl_idname = "qmn_node.add_float_mix_node"
    bl_label = "Mix / Lerp (Float)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'FLOAT'
        return {'FINISHED'}
    

class MixVectorOperator(bpy.types.Operator):
    bl_idname = "qmn_node.add_vector_mix_node"
    bl_label = "Mix / Lerp (Vector)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'VECTOR'
        return {'FINISHED'}

class MixColorOperator(bpy.types.Operator):
    bl_idname = "qmn_node.add_color_mix_node"
    bl_label = "Mix / Lerp (Color)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMix')
        bpy.context.active_node.data_type = 'RGBA'
        return {'FINISHED'}