import bpy

class ShaderAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.add_math_node"
    bl_label = "Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class ShaderSubtractMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.subtract_math_node"
    bl_label = "Subtract (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class ShaderMultiplyMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.multiply_math_node"
    bl_label = "Multiply (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class ShaderDivideMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.divide_math_node"
    bl_label = "Divide (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}

class ShaderMultiplyAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.multiply_add_math_node"
    bl_label = "Multiply Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}


class ShaderPowerMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.power_math_node"
    bl_label = "Power (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'POWER'
        return {'FINISHED'}

class ShaderLogarithmMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.logarithm_math_node"
    bl_label = "Logarithm (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LOGARITHM'
        return {'FINISHED'}

class ShaderSqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.sqrt_math_node"
    bl_label = "Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SQRT'
        return {'FINISHED'}

class ShaderInverseSqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.inverse_sqrt_math_node"
    bl_label = "Inverse Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'INVERSE_SQRT'
        return {'FINISHED'}

class ShaderAbsoluteMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.absolute_math_node"
    bl_label = "Absolute (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}
    
class ShaderExponentMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.exponent_math_node"
    bl_label = "Exponent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'EXPONENT'
        return {'FINISHED'}



class ShaderMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.min_math_node"
    bl_label = "Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class ShaderMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.max_math_node"
    bl_label = "Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class ShaderLessThanOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.less_than_node"
    bl_label = "Less Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'LESS_THAN'
        return {'FINISHED'}

class ShaderGreaterThanOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.greater_than_node"
    bl_label = "Greater Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'GREATER_THAN'
        return {'FINISHED'}

class ShaderSignMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.sign_math_node"
    bl_label = "Sign (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SIGN'
        return {'FINISHED'}

class ShaderCompareMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.compare_math_node"
    bl_label = "Compare (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COMPARE'
        return {'FINISHED'}

class ShaderSmoothMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.smooth_min_math_node"
    bl_label = "Smooth Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MIN'
        return {'FINISHED'}

class ShaderSmoothMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.smooth_max_math_node"
    bl_label = "Smooth Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MAX'
        return {'FINISHED'}




class ShaderRoundMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.round_math_node"
    bl_label = "Round (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ROUND'
        return {'FINISHED'}

class ShaderFloorMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.floor_math_node"
    bl_label = "Floor (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class ShaderCeilMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.ceil_math_node"
    bl_label = "Ceil (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class ShaderTruncateMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.truncate_math_node"
    bl_label = "Truncate (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TRUNC'
        return {'FINISHED'}



class ShaderFractionMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.fraction_math_node"
    bl_label = "Fraction (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FRACT'
        return {'FINISHED'}  

class ShaderTruncatedModuloOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.truncated_modulo_node"
    bl_label = "Truncated Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class ShaderFlooredModuloOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.floored_modulo_node"
    bl_label = "Floored Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'FLOORED_MODULO'
        return {'FINISHED'}

class ShaderWrapOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.wrap_node"
    bl_label = "Wrap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class ShaderSnapOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.snap_node"
    bl_label = "Snap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}

class ShaderPingPongOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.ping_pong_node"
    bl_label = "Ping-Pong (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'PINGPONG'
        return {'FINISHED'}



class ShaderSineMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.sine_math_node"
    bl_label = "Sine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class ShaderCosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.cosine_math_node"
    bl_label = "Cosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class ShaderTangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.tangent_math_node"
    bl_label = "Tangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
    

class ShaderArcsineMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.arcsine_math_node"
    bl_label = "Arcsine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCSINE'
        return {'FINISHED'}

class ShaderArccosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.arccosine_math_node"
    bl_label = "Arccosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCCOSINE'
        return {'FINISHED'}

class ShaderArctangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.arctangent_math_node"
    bl_label = "Arctangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTANGENT'
        return {'FINISHED'}

class ShaderArctan2MathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.arctan2_math_node"
    bl_label = "Arctan2 (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'ARCTAN2'
        return {'FINISHED'}
    

class ShaderSinehMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.sineh_math_node"
    bl_label = "Sinh (Hyperbolic Sine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'SINH'
        return {'FINISHED'}

class ShaderCoshMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.cosh_math_node"
    bl_label = "Cosh (Hyperbolic Cosine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'COSH'
        return {'FINISHED'}

class ShaderTanhMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.tanh_math_node"
    bl_label = "Tanh (Hyperbolic Tangent) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'TANH'
        return {'FINISHED'}



class ShaderRadiansMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.radians_math_node"
    bl_label = "To Radians (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'RADIANS'
        return {'FINISHED'}

class ShaderDegreesMathOperator(bpy.types.Operator):
    bl_idname = "quick_shader_node.degrees_math_node"
    bl_label = "To Degrees (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='ShaderNodeMath')
        bpy.context.active_node.operation = 'DEGREES'
        return {'FINISHED'}