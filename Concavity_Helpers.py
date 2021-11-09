from manim import *

def get_plane(x_min = -5, x_max = 5, 
    y_min = -5, y_max = 5,
    x_unit_size = 0.3, y_unit_size = 0.3,
    x_nums = range(-5, 5, 1), y_nums = range(-5, 5, 1), 
    num_scale = 0.5, **kwargs):
        plane_config = dict(
            axis_config = { 
            "include_tip": False, "include_numbers" : True,
            "include_ticks" : True, "line_to_number_buff" : 0.05,
            "stroke_color" : WHITE, "stroke_width": 0.5,
            "number_scale_val" : num_scale,
            "tip_scale": 0.5,
        },
            x_axis_config = {
            "exclude_zero_from_default_numbers": True,
            "label_direction" : DR, "stroke_color" : WHITE,
            "x_min" : x_min, "x_max" : x_max, "unit_size": x_unit_size, 
            "numbers_to_show": x_nums,
        },
            y_axis_config = {
            "exclude_zero_from_default_numbers": True,
            "label_direction" : DOWN, "stroke_color" : WHITE,
            "x_min" : y_min, # not y_min
            "x_max" : y_max,  # not y_max
            "unit_size": y_unit_size, "numbers_to_show": y_nums,
        },
            background_line_style = {
            "stroke_width" : 0.75, "stroke_opacity" : 0.5,
            "stroke_color" : GOLD,
        }  
    )
        return NumberPlane(**plane_config)

def get_secant_line(x, plane, graph, color, width):
    dx = 0.0001
    p1 = plane.input_to_graph_point(x, graph)
    p2 = plane.input_to_graph_point(x + dx, graph)
    secant_line = Line(p1, p2, color=color, width = width)
    secant_line.scale_in_place(2 / secant_line.get_length())
    return secant_line
        
def get_secant_group(x, plane, graph, color, width):
    dx = 0.0001
    p1 = plane.input_to_graph_point(x, graph)
    p2 = plane.input_to_graph_point(x + dx, graph)
    secant_line = Line(p1, p2, color=color)
    secant_line.scale_in_place(2 / secant_line.get_length())
    dot = Dot().set_color(color).move_to(p1)
    result = VGroup(secant_line, dot)
    return result


