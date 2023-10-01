# Geometry nodes uses ShaderNode a lot of the time.
# So if Quick Nodes for Geometry Nodes break, its probably becayse they have updated the classes

import bpy

class GeometryAddVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_vector_node"
    bl_label = "Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class GeometrySubtractVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.subtract_vector_node"
    bl_label = "Subtract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class GeometryMultiplyVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.multiply_vector_node"
    bl_label = "Multiply (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class GeometryDivideVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.divide_vector_node"
    bl_label = "Divide (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}
    
class GeometryMultiplyAddVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.multiply_add_vector_node"
    bl_label = "Multiply Add (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}



class GeometryCrossProductVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.cross_product_vector_node"
    bl_label = "Cross Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CROSS_PRODUCT'
        return {'FINISHED'}

class GeometryProjectVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.project_vector_node"
    bl_label = "Project (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'PROJECT'
        return {'FINISHED'}

class GeometryReflectVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.reflect_vector_node"
    bl_label = "Reflect (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFLECT'
        return {'FINISHED'}

class GeometryRefractVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.refract_vector_node"
    bl_label = "Refract (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'REFRACT'
        return {'FINISHED'}

class GeometryFaceForwardVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.faceforward_vector_node"
    bl_label = "Faceforward (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FACEFORWARD'
        return {'FINISHED'}

class GeometryDotProductVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.dot_product_vector_node"
    bl_label = "Dot Product (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DOT_PRODUCT'
        return {'FINISHED'}


class GeometryDistanceVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.distance_vector_node"
    bl_label = "Distance (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'DISTANCE'
        return {'FINISHED'}

class GeometryLengthVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.length_vector_node"
    bl_label = "Length (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'LENGTH'
        return {'FINISHED'}

class GeometryScaleVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.scale_vector_node"
    bl_label = "Scale (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SCALE'
        return {'FINISHED'}

class GeometryNormalizeVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.normalize_vector_node"
    bl_label = "Normalize (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'NORMALIZE'
        return {'FINISHED'}



class GeometryAbsoluteVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.absolute_vector_node"
    bl_label = "Absolute (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}

class GeometryMinimumVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.minimum_vector_node"
    bl_label = "Minimum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class GeometryMaximumVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.maximum_vector_node"
    bl_label = "Maximum (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class GeometryFloorVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.floor_vector_node"
    bl_label = "Floor (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class GeometryCeilVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.ceil_vector_node"
    bl_label = "Ceil (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class GeometryFractionVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.fraction_vector_node"
    bl_label = "Fraction (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'FRACTION'
        return {'FINISHED'}

class GeometryModuloVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.modulo_vector_node"
    bl_label = "Modulo (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class GeometryWrapVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.wrap_vector_node"
    bl_label = "Wrap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class GeometrySnapVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.snap_vector_node"
    bl_label = "Snap (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}



class GeometrySineVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.sine_vector_node"
    bl_label = "Sine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class GeometryCosineVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.cosine_vector_node"
    bl_label = "Cosine (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class GeometryTangentVectorOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.tangent_vector_node"
    bl_label = "Tangent (Vector Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeVectorMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
