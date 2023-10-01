import bpy

class ShaderAddVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_vector_node"
    bl_label = "Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class ShaderSubtractVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.subtract_vector_node"
    bl_label = "Subtract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class ShaderMultiplyVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.multiply_vector_node"
    bl_label = "Multiply (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class ShaderDivideVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.divide_vector_node"
    bl_label = "Divide (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}
    
class ShaderMultiplyAddVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.multiply_add_vector_node"
    bl_label = "Multiply Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}



class ShaderCrossProductVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.cross_product_vector_node"
    bl_label = "Cross Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CROSS_PRODUCT'
        return {'FINISHED'}

class ShaderProjectVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.project_vector_node"
    bl_label = "Project (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'PROJECT'
        return {'FINISHED'}

class ShaderReflectVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.reflect_vector_node"
    bl_label = "Reflect (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFLECT'
        return {'FINISHED'}

class ShaderRefractVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.refract_vector_node"
    bl_label = "Refract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFRACT'
        return {'FINISHED'}

class ShaderFaceForwardVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.faceforward_vector_node"
    bl_label = "Faceforward (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FACEFORWARD'
        return {'FINISHED'}

class ShaderDotProductVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.dot_product_vector_node"
    bl_label = "Dot Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DOT_PRODUCT'
        return {'FINISHED'}


class ShaderDistanceVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.distance_vector_node"
    bl_label = "Distance (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DISTANCE'
        return {'FINISHED'}

class ShaderLengthVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.length_vector_node"
    bl_label = "Length (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'LENGTH'
        return {'FINISHED'}

class ShaderScaleVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.scale_vector_node"
    bl_label = "Scale (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SCALE'
        return {'FINISHED'}

class ShaderNormalizeVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.normalize_vector_node"
    bl_label = "Normalize (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'NORMALIZE'
        return {'FINISHED'}



class ShaderAbsoluteVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.absolute_vector_node"
    bl_label = "Absolute (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}

class ShaderMinimumVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.minimum_vector_node"
    bl_label = "Minimum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class ShaderMaximumVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.maximum_vector_node"
    bl_label = "Maximum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class ShaderFloorVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.floor_vector_node"
    bl_label = "Floor (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class ShaderCeilVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.ceil_vector_node"
    bl_label = "Ceil (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class ShaderFractionVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.fraction_vector_node"
    bl_label = "Fraction (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FRACTION'
        return {'FINISHED'}

class ShaderModuloVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.modulo_vector_node"
    bl_label = "Modulo (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class ShaderWrapVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.wrap_vector_node"
    bl_label = "Wrap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class ShaderSnapVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.snap_vector_node"
    bl_label = "Snap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}



class ShaderSineVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.sine_vector_node"
    bl_label = "Sine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class ShaderCosineVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.cosine_vector_node"
    bl_label = "Cosine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class ShaderTangentVectorOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.tangent_vector_node"
    bl_label = "Tangent (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
