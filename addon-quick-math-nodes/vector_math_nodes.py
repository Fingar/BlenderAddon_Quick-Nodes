import bpy

class AddVectorOperator(bpy.types.Operator):
    bl_idname = "node.add_vector_node"
    bl_label = "Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class SubtractVectorOperator(bpy.types.Operator):
    bl_idname = "node.subtract_vector_node"
    bl_label = "Subtract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class MultiplyVectorOperator(bpy.types.Operator):
    bl_idname = "node.multiply_vector_node"
    bl_label = "Multiply (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class DivideVectorOperator(bpy.types.Operator):
    bl_idname = "node.divide_vector_node"
    bl_label = "Divide (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}
    
class MultiplyAddVectorOperator(bpy.types.Operator):
    bl_idname = "node.multiply_add_vector_node"
    bl_label = "Multiply Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}



class CrossProductVectorOperator(bpy.types.Operator):
    bl_idname = "node.cross_product_vector_node"
    bl_label = "Cross Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CROSS_PRODUCT'
        return {'FINISHED'}

class ProjectVectorOperator(bpy.types.Operator):
    bl_idname = "node.project_vector_node"
    bl_label = "Project (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'PROJECT'
        return {'FINISHED'}

class ReflectVectorOperator(bpy.types.Operator):
    bl_idname = "node.reflect_vector_node"
    bl_label = "Reflect (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFLECT'
        return {'FINISHED'}

class RefractVectorOperator(bpy.types.Operator):
    bl_idname = "node.refract_vector_node"
    bl_label = "Refract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFRACT'
        return {'FINISHED'}

class FaceForwardVectorOperator(bpy.types.Operator):
    bl_idname = "node.faceforward_vector_node"
    bl_label = "Faceforward (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FACEFORWARD'
        return {'FINISHED'}

class DotProductVectorOperator(bpy.types.Operator):
    bl_idname = "node.dot_product_vector_node"
    bl_label = "Dot Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DOT_PRODUCT'
        return {'FINISHED'}


class DistanceVectorOperator(bpy.types.Operator):
    bl_idname = "node.distance_vector_node"
    bl_label = "Distance (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DISTANCE'
        return {'FINISHED'}

class LengthVectorOperator(bpy.types.Operator):
    bl_idname = "node.length_vector_node"
    bl_label = "Length (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'LENGTH'
        return {'FINISHED'}

class ScaleVectorOperator(bpy.types.Operator):
    bl_idname = "node.scale_vector_node"
    bl_label = "Scale (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SCALE'
        return {'FINISHED'}

class NormalizeVectorOperator(bpy.types.Operator):
    bl_idname = "node.normalize_vector_node"
    bl_label = "Normalize (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'NORMALIZE'
        return {'FINISHED'}



class AbsoluteVectorOperator(bpy.types.Operator):
    bl_idname = "node.absolute_vector_node"
    bl_label = "Absolute (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}

class MinimumVectorOperator(bpy.types.Operator):
    bl_idname = "node.minimum_vector_node"
    bl_label = "Minimum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class MaximumVectorOperator(bpy.types.Operator):
    bl_idname = "node.maximum_vector_node"
    bl_label = "Maximum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class FloorVectorOperator(bpy.types.Operator):
    bl_idname = "node.floor_vector_node"
    bl_label = "Floor (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class CeilVectorOperator(bpy.types.Operator):
    bl_idname = "node.ceil_vector_node"
    bl_label = "Ceil (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class FractionVectorOperator(bpy.types.Operator):
    bl_idname = "node.fraction_vector_node"
    bl_label = "Fraction (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FRACTION'
        return {'FINISHED'}

class ModuloVectorOperator(bpy.types.Operator):
    bl_idname = "node.modulo_vector_node"
    bl_label = "Modulo (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class WrapVectorOperator(bpy.types.Operator):
    bl_idname = "node.wrap_vector_node"
    bl_label = "Wrap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class SnapVectorOperator(bpy.types.Operator):
    bl_idname = "node.snap_vector_node"
    bl_label = "Snap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}



class SineVectorOperator(bpy.types.Operator):
    bl_idname = "node.sine_vector_node"
    bl_label = "Sine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class CosineVectorOperator(bpy.types.Operator):
    bl_idname = "node.cosine_vector_node"
    bl_label = "Cosine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class TangentVectorOperator(bpy.types.Operator):
    bl_idname = "node.tangent_vector_node"
    bl_label = "Tangent (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
