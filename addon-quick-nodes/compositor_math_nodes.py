import bpy

class CompositorAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.add_math_node"
    bl_label = "Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ADD'
        return {'FINISHED'}

class CompositorSubtractMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.subtract_math_node"
    bl_label = "Subtract (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SUBTRACT'
        return {'FINISHED'}

class CompositorMultiplyMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.multiply_math_node"
    bl_label = "Multiply (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY'
        return {'FINISHED'}

class CompositorDivideMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.divide_math_node"
    bl_label = "Divide (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'DIVIDE'
        return {'FINISHED'}

class CompositorMultiplyAddMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.multiply_add_math_node"
    bl_label = "Multiply Add (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'MULTIPLY_ADD'
        return {'FINISHED'}


class CompositorPowerMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.power_math_node"
    bl_label = "Power (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'POWER'
        return {'FINISHED'}

class CompositorLogarithmMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.logarithm_math_node"
    bl_label = "Logarithm (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'LOGARITHM'
        return {'FINISHED'}

class CompositorSqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.sqrt_math_node"
    bl_label = "Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SQRT'
        return {'FINISHED'}

class CompositorInverseSqrtMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.inverse_sqrt_math_node"
    bl_label = "Inverse Square Root (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'INVERSE_SQRT'
        return {'FINISHED'}

class CompositorAbsoluteMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.absolute_math_node"
    bl_label = "Absolute (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ABSOLUTE'
        return {'FINISHED'}
    
class CompositorExponentMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.exponent_math_node"
    bl_label = "Exponent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'EXPONENT'
        return {'FINISHED'}



class CompositorMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.min_math_node"
    bl_label = "Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'MINIMUM'
        return {'FINISHED'}

class CompositorMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.max_math_node"
    bl_label = "Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'MAXIMUM'
        return {'FINISHED'}

class CompositorLessThanOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.less_than_node"
    bl_label = "Less Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'LESS_THAN'
        return {'FINISHED'}

class CompositorGreaterThanOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.greater_than_node"
    bl_label = "Greater Than (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'GREATER_THAN'
        return {'FINISHED'}

class CompositorSignMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.sign_math_node"
    bl_label = "Sign (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SIGN'
        return {'FINISHED'}

class CompositorCompareMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.compare_math_node"
    bl_label = "Compare (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'COMPARE'
        return {'FINISHED'}

class CompositorSmoothMinMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.smooth_min_math_node"
    bl_label = "Smooth Minimum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MIN'
        return {'FINISHED'}

class CompositorSmoothMaxMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.smooth_max_math_node"
    bl_label = "Smooth Maximum (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SMOOTH_MAX'
        return {'FINISHED'}




class CompositorRoundMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.round_math_node"
    bl_label = "Round (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ROUND'
        return {'FINISHED'}

class CompositorFloorMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.floor_math_node"
    bl_label = "Floor (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'FLOOR'
        return {'FINISHED'}

class CompositorCeilMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.ceil_math_node"
    bl_label = "Ceil (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'CEIL'
        return {'FINISHED'}

class CompositorTruncateMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.truncate_math_node"
    bl_label = "Truncate (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'TRUNC'
        return {'FINISHED'}



class CompositorFractionMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.fraction_math_node"
    bl_label = "Fraction (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'FRACT'
        return {'FINISHED'}  

class CompositorTruncatedModuloOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.truncated_modulo_node"
    bl_label = "Truncated Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'MODULO'
        return {'FINISHED'}

class CompositorFlooredModuloOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.floored_modulo_node"
    bl_label = "Floored Modulo (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'FLOORED_MODULO'
        return {'FINISHED'}

class CompositorWrapOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.wrap_node"
    bl_label = "Wrap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'WRAP'
        return {'FINISHED'}

class CompositorSnapOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.snap_node"
    bl_label = "Snap (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SNAP'
        return {'FINISHED'}

class CompositorPingPongOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.ping_pong_node"
    bl_label = "Ping-Pong (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'PINGPONG'
        return {'FINISHED'}



class CompositorSineMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.sine_math_node"
    bl_label = "Sine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SINE'
        return {'FINISHED'}

class CompositorCosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.cosine_math_node"
    bl_label = "Cosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'COSINE'
        return {'FINISHED'}

class CompositorTangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.tangent_math_node"
    bl_label = "Tangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'TANGENT'
        return {'FINISHED'}
    

class CompositorArcsineMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.arcsine_math_node"
    bl_label = "Arcsine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ARCSINE'
        return {'FINISHED'}

class CompositorArccosineMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.arccosine_math_node"
    bl_label = "Arccosine (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ARCCOSINE'
        return {'FINISHED'}

class CompositorArctangentMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.arctangent_math_node"
    bl_label = "Arctangent (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ARCTANGENT'
        return {'FINISHED'}

class CompositorArctan2MathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.arctan2_math_node"
    bl_label = "Arctan2 (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'ARCTAN2'
        return {'FINISHED'}
    

class CompositorSinehMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.sineh_math_node"
    bl_label = "Sinh (Hyperbolic Sine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'SINH'
        return {'FINISHED'}

class CompositorCoshMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.cosh_math_node"
    bl_label = "Cosh (Hyperbolic Cosine) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'COSH'
        return {'FINISHED'}

class CompositorTanhMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.tanh_math_node"
    bl_label = "Tanh (Hyperbolic Tangent) (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'TANH'
        return {'FINISHED'}



class CompositorRadiansMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.radians_math_node"
    bl_label = "To Radians (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'RADIANS'
        return {'FINISHED'}

class CompositorDegreesMathOperator(bpy.types.Operator):
    bl_idname = "quick_compositor_node.degrees_math_node"
    bl_label = "To Degrees (Math)"
    
    def execute(self, context):
        bpy.ops.node.add_node(type='CompositorNodeMath')
        bpy.context.active_node.operation = 'DEGREES'
        return {'FINISHED'}