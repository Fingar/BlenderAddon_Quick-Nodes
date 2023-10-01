import bpy

class AddMathOperator(bpy.types.Operator):
    bl_idname = "node.add_math_node"
    bl_label = "Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class SubtractMathOperator(bpy.types.Operator):
    bl_idname = "node.subtract_math_node"
    bl_label = "Subtract (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class MultiplyMathOperator(bpy.types.Operator):
    bl_idname = "node.multiply_math_node"
    bl_label = "Multiply (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class DivideMathOperator(bpy.types.Operator):
    bl_idname = "node.divide_math_node"
    bl_label = "Divide (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}

class MultiplyAddMathOperator(bpy.types.Operator):
    bl_idname = "node.multiply_add_math_node"
    bl_label = "Multiply Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}


class PowerMathOperator(bpy.types.Operator):
    bl_idname = "node.power_math_node"
    bl_label = "Power (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'POWER'
        return {'FINISHED'}

class LogarithmMathOperator(bpy.types.Operator):
    bl_idname = "node.logarithm_math_node"
    bl_label = "Logarithm (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LOGARITHM'
        return {'FINISHED'}

class SqrtMathOperator(bpy.types.Operator):
    bl_idname = "node.sqrt_math_node"
    bl_label = "Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SQRT'
        return {'FINISHED'}

class InverseSqrtMathOperator(bpy.types.Operator):
    bl_idname = "node.inverse_sqrt_math_node"
    bl_label = "Inverse Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'INVERSE_SQRT'
        return {'FINISHED'}

class AbsoluteMathOperator(bpy.types.Operator):
    bl_idname = "node.absolute_math_node"
    bl_label = "Absolute (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}
    
class ExponentMathOperator(bpy.types.Operator):
    bl_idname = "node.exponent_math_node"
    bl_label = "Exponent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'EXPONENT'
        return {'FINISHED'}



class MinMathOperator(bpy.types.Operator):
    bl_idname = "node.min_math_node"
    bl_label = "Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class MaxMathOperator(bpy.types.Operator):
    bl_idname = "node.max_math_node"
    bl_label = "Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class LessThanOperator(bpy.types.Operator):
    bl_idname = "node.less_than_node"
    bl_label = "Less Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LESS_THAN'
        return {'FINISHED'}

class GreaterThanOperator(bpy.types.Operator):
    bl_idname = "node.greater_than_node"
    bl_label = "Greater Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'GREATER_THAN'
        return {'FINISHED'}

class SignMathOperator(bpy.types.Operator):
    bl_idname = "node.sign_math_node"
    bl_label = "Sign (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SIGN'
        return {'FINISHED'}

class CompareMathOperator(bpy.types.Operator):
    bl_idname = "node.compare_math_node"
    bl_label = "Compare (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COMPARE'
        return {'FINISHED'}

class SmoothMinMathOperator(bpy.types.Operator):
    bl_idname = "node.smooth_min_math_node"
    bl_label = "Smooth Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MIN'
        return {'FINISHED'}

class SmoothMaxMathOperator(bpy.types.Operator):
    bl_idname = "node.smooth_max_math_node"
    bl_label = "Smooth Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MAX'
        return {'FINISHED'}




class RoundMathOperator(bpy.types.Operator):
    bl_idname = "node.round_math_node"
    bl_label = "Round (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ROUND'
        return {'FINISHED'}

class FloorMathOperator(bpy.types.Operator):
    bl_idname = "node.floor_math_node"
    bl_label = "Floor (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class CeilMathOperator(bpy.types.Operator):
    bl_idname = "node.ceil_math_node"
    bl_label = "Ceil (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class TruncateMathOperator(bpy.types.Operator):
    bl_idname = "node.truncate_math_node"
    bl_label = "Truncate (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TRUNC'
        return {'FINISHED'}



class FractionMathOperator(bpy.types.Operator):
    bl_idname = "node.fraction_math_node"
    bl_label = "Fraction (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FRACT'
        return {'FINISHED'}  

class TruncatedModuloOperator(bpy.types.Operator):
    bl_idname = "node.truncated_modulo_node"
    bl_label = "Truncated Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class FlooredModuloOperator(bpy.types.Operator):
    bl_idname = "node.floored_modulo_node"
    bl_label = "Floored Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOORED_MODULO'
        return {'FINISHED'}

class WrapOperator(bpy.types.Operator):
    bl_idname = "node.wrap_node"
    bl_label = "Wrap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class SnapOperator(bpy.types.Operator):
    bl_idname = "node.snap_node"
    bl_label = "Snap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}

class PingPongOperator(bpy.types.Operator):
    bl_idname = "node.ping_pong_node"
    bl_label = "Ping-Pong (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'PINGPONG'
        return {'FINISHED'}



class SineMathOperator(bpy.types.Operator):
    bl_idname = "node.sine_math_node"
    bl_label = "Sine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class CosineMathOperator(bpy.types.Operator):
    bl_idname = "node.cosine_math_node"
    bl_label = "Cosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class TangentMathOperator(bpy.types.Operator):
    bl_idname = "node.tangent_math_node"
    bl_label = "Tangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
    

class ArcsineMathOperator(bpy.types.Operator):
    bl_idname = "node.arcsine_math_node"
    bl_label = "Arcsine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCSINE'
        return {'FINISHED'}

class ArccosineMathOperator(bpy.types.Operator):
    bl_idname = "node.arccosine_math_node"
    bl_label = "Arccosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCCOSINE'
        return {'FINISHED'}

class ArctangentMathOperator(bpy.types.Operator):
    bl_idname = "node.arctangent_math_node"
    bl_label = "Arctangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTANGENT'
        return {'FINISHED'}

class Arctan2MathOperator(bpy.types.Operator):
    bl_idname = "node.arctan2_math_node"
    bl_label = "Arctan2 (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTAN2'
        return {'FINISHED'}
    

class SinehMathOperator(bpy.types.Operator):
    bl_idname = "node.sineh_math_node"
    bl_label = "Sinh (Hyperbolic Sine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINH'
        return {'FINISHED'}

class CoshMathOperator(bpy.types.Operator):
    bl_idname = "node.cosh_math_node"
    bl_label = "Cosh (Hyperbolic Cosine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSH'
        return {'FINISHED'}

class TanhMathOperator(bpy.types.Operator):
    bl_idname = "node.tanh_math_node"
    bl_label = "Tanh (Hyperbolic Tangent) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANH'
        return {'FINISHED'}



class RadiansMathOperator(bpy.types.Operator):
    bl_idname = "node.radians_math_node"
    bl_label = "To Radians (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'RADIANS'
        return {'FINISHED'}

class DegreesMathOperator(bpy.types.Operator):
    bl_idname = "node.degrees_math_node"
    bl_label = "To Degrees (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DEGREES'
        return {'FINISHED'}