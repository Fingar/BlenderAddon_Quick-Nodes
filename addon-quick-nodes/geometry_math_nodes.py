# Geometry nodes uses ShaderNode a lot of the time.
# So if Quick Nodes for Geometry Nodes break, its probably becayse they have updated the classes

import bpy

class GeometryAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.add_math_node"
    bl_label = "Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class GeometrySubtractMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.subtract_math_node"
    bl_label = "Subtract (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class GeometryMultiplyMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.multiply_math_node"
    bl_label = "Multiply (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class GeometryDivideMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.divide_math_node"
    bl_label = "Divide (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}

class GeometryMultiplyAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.multiply_add_math_node"
    bl_label = "Multiply Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}


class GeometryPowerMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.power_math_node"
    bl_label = "Power (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'POWER'
        return {'FINISHED'}

class GeometryLogarithmMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.logarithm_math_node"
    bl_label = "Logarithm (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LOGARITHM'
        return {'FINISHED'}

class GeometrySqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.sqrt_math_node"
    bl_label = "Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SQRT'
        return {'FINISHED'}

class GeometryInverseSqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.inverse_sqrt_math_node"
    bl_label = "Inverse Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'INVERSE_SQRT'
        return {'FINISHED'}

class GeometryAbsoluteMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.absolute_math_node"
    bl_label = "Absolute (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}
    
class GeometryExponentMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.exponent_math_node"
    bl_label = "Exponent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'EXPONENT'
        return {'FINISHED'}



class GeometryMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.min_math_node"
    bl_label = "Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class GeometryMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.max_math_node"
    bl_label = "Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class GeometryLessThanOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.less_than_node"
    bl_label = "Less Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LESS_THAN'
        return {'FINISHED'}

class GeometryGreaterThanOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.greater_than_node"
    bl_label = "Greater Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'GREATER_THAN'
        return {'FINISHED'}

class GeometrySignMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.sign_math_node"
    bl_label = "Sign (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SIGN'
        return {'FINISHED'}

class GeometryCompareMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.compare_math_node"
    bl_label = "Compare (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COMPARE'
        return {'FINISHED'}

class GeometrySmoothMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.smooth_min_math_node"
    bl_label = "Smooth Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MIN'
        return {'FINISHED'}

class GeometrySmoothMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.smooth_max_math_node"
    bl_label = "Smooth Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MAX'
        return {'FINISHED'}




class GeometryRoundMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.round_math_node"
    bl_label = "Round (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ROUND'
        return {'FINISHED'}

class GeometryFloorMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.floor_math_node"
    bl_label = "Floor (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class GeometryCeilMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.ceil_math_node"
    bl_label = "Ceil (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class GeometryTruncateMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.truncate_math_node"
    bl_label = "Truncate (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TRUNC'
        return {'FINISHED'}



class GeometryFractionMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.fraction_math_node"
    bl_label = "Fraction (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FRACT'
        return {'FINISHED'}  

class GeometryTruncatedModuloOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.truncated_modulo_node"
    bl_label = "Truncated Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class GeometryFlooredModuloOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.floored_modulo_node"
    bl_label = "Floored Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOORED_MODULO'
        return {'FINISHED'}

class GeometryWrapOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.wrap_node"
    bl_label = "Wrap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class GeometrySnapOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.snap_node"
    bl_label = "Snap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}

class GeometryPingPongOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.ping_pong_node"
    bl_label = "Ping-Pong (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'PINGPONG'
        return {'FINISHED'}



class GeometrySineMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.sine_math_node"
    bl_label = "Sine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class GeometryCosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.cosine_math_node"
    bl_label = "Cosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class GeometryTangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.tangent_math_node"
    bl_label = "Tangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
    

class GeometryArcsineMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.arcsine_math_node"
    bl_label = "Arcsine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCSINE'
        return {'FINISHED'}

class GeometryArccosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.arccosine_math_node"
    bl_label = "Arccosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCCOSINE'
        return {'FINISHED'}

class GeometryArctangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.arctangent_math_node"
    bl_label = "Arctangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTANGENT'
        return {'FINISHED'}

class GeometryArctan2MathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.arctan2_math_node"
    bl_label = "Arctan2 (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTAN2'
        return {'FINISHED'}
    

class GeometrySinehMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.sineh_math_node"
    bl_label = "Sinh (Hyperbolic Sine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINH'
        return {'FINISHED'}

class GeometryCoshMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.cosh_math_node"
    bl_label = "Cosh (Hyperbolic Cosine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSH'
        return {'FINISHED'}

class GeometryTanhMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.tanh_math_node"
    bl_label = "Tanh (Hyperbolic Tangent) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANH'
        return {'FINISHED'}



class GeometryRadiansMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.radians_math_node"
    bl_label = "To Radians (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'RADIANS'
        return {'FINISHED'}

class GeometryDegreesMathOperator(bpy.types.Operator):
    bl_idname = "quick_geometry_node.degrees_math_node"
    bl_label = "To Degrees (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DEGREES'
        return {'FINISHED'}