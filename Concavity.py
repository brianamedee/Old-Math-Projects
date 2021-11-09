from manim import *
import numpy as np
from Concavity_Helpers import *

class TestConcavity(MovingCameraScene):
    def construct(self):
        self.camera_frame.save_state()

        def get_secant_line(x, plane, graph, color):
            x = interpolate(x, 4, 0.01)
            dx = 0.01
            p1 = plane.input_to_graph_point(x, graph)
            p2 = plane.input_to_graph_point(x + dx, graph)
            secant_line = Line(p1, p2, color=color)
            secant_line.scale_in_place(2 / secant_line.get_length())
            dot = Dot().scale(0.6).set_color(color).move_to(
                plane.coords_to_point(x, graph.underlying_function(x)))
            text = Tex("m=").scale(0.6).next_to(secant_line, RIGHT, buff=0.2).set_color(color)
            num = DecimalNumber(num_decimal_places=2
            ).set_value(first_derivative.underlying_function(x)
            ).set_color(color).scale(0.6).next_to(text, RIGHT, buff=0.2)
            result = VGroup(secant_line, text, num, dot)
            return result

        def track_slopes(mob):
            mob.move_to(slopes.get_center())

        def get_vert_line_from_f_to_f(x, plane, graph1, graph2, width=1, color=WHITE):
            if graph2.underlying_function(x) < graph1.underlying_function(x):
                line = Line(
                    plane.coords_to_point(x, graph2.underlying_function(x)),
                    plane.coords_to_point(x, 0),
                    stoke_width = width, stroke_color = color
                )
            else:
                line = Line(
                    plane.coords_to_point(x, graph1.underlying_function(x)),
                    plane.coords_to_point(x, graph2.underlying_function(x)), 
                    stroke_width = width, stroke_color = color
                )
            return line

        plane_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DR, "stroke_color" : WHITE,
                "x_min" : -2, "x_max" : 4, "unit_size": 1, 
                "numbers_to_show": range(-2, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -20, # not y_min
                "x_max" : 20,  # not y_max
                "unit_size": 0.17, "numbers_to_show": range(-20, 21, 5),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_B,
            }  
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = LEFT
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        s = ValueTracker(-2) #Tracking the slope value

        function = plane.get_graph(lambda x : x**3-3*x**2-4*x, x_min = -2, x_max = 4, color = RED)
        func_concavedown = plane.get_graph(lambda x : x**3-3*x**2-4*x, x_min = -2, x_max = 1, color = PURPLE_D)
        func_concaveup = plane.get_graph(lambda x : x**3-3*x**2-4*x, x_min = 1, x_max = 4, color = ORANGE)
        function_label = MathTex("f(x)={x}^{3}-3{x}^{2}-4x").scale(0.7).set_color(RED).next_to(function, UR)

        first_derivative = plane.get_graph(lambda x : 3*x**2-6*x-4, x_min = -2, x_max = 4, color = BLUE)
        first_derivative_label = MathTex("f'(x)=3{x}^{2}-6x-4").scale(0.7).set_color(BLUE
        ).next_to(first_derivative, UR)

        second_derivative = plane.get_graph(lambda x : 6*x-6, x_min = -2, x_max = 4, color = GREEN)
        second_derivative_label = MathTex("f''(x)=6x-6").set_color(GREEN).scale(0.7
        ).next_to(second_derivative, UR).shift(DOWN*0.2)

        slopes = always_redraw(lambda : get_secant_line(x = s.get_value(), 
        plane = plane, graph = function, color = YELLOW))

        poi = Circle(radius=0.05, stroke_color = DARK_BLUE).move_to(plane.coords_to_point(1,-6))

        vert_line = always_redraw(lambda : get_vert_line_from_f_to_f(
            x = s.get_value(), plane = plane, graph1 = function, graph2 = second_derivative,
            width = 2, color = WHITE
        ))

        self.play(Write(plane))
        self.add(function, slopes)
        self.play(s.animate.set_value(4), run_time=3)
        self.play(function.animate.set_stroke(opacity=0.2))
        self.play(ShowCreation(poi))
        self.wait()
        self.play(s.animate.set_value(0.5), run_time=2)
        self.play(DrawBorderThenFill(func_concaveup))
        self.play(DrawBorderThenFill(func_concavedown))
        self.wait()
        self.play(self.camera.frame.animate.move_to(poi))
        self.play(self.camera.frame.animate.scale(0.4))
        self.play(s.animate.set_value(1.5), run_time=6)
        self.wait()
        self.play(s.animate.set_value(0.5), run_time=6)
        self.wait()
        self.play(Restore(self.camera_frame))
        self.remove(slopes)
        self.play(s.animate.set_value(-2), run_time=0.1)
        self.play(Write(VGroup(function_label, first_derivative_label)),
        ShowCreation(first_derivative))
        self.wait()
        self.play(ShowCreation(second_derivative), Write(second_derivative_label))
        self.wait()
        self.add(vert_line, slopes)
        self.play(s.animate.set_value(4), run_time=10, rate_func=linear)
        self.wait()

class SecondDerivativeConcavity(Scene):
    def construct(self):

        def get_num_plane(**kwargs):
            plane_config = dict(
                axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5,
            },
                x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DR, "stroke_color" : WHITE,
                "x_min" : -4, "x_max" : 4, "unit_size": 0.4, 
                "numbers_to_show": range(-4,4,1),
            },
                y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UP, "stroke_color" : WHITE,
                "x_min" : -4, # not y_min
                "x_max" : 4,  # not y_max
                "unit_size": 0.4, "numbers_to_show": range(-4, 4, 1),
            },
                background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_B,
            }  
        )
            return NumberPlane(**plane_config)
        
        plane = get_num_plane()
        
        new_origin = LEFT*0.5+DOWN*0.5
        plane.shift(new_origin)

        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

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
            dot = Dot().scale(0.6).set_color(color).move_to(p1)
            text = Tex("m=").scale(0.6).next_to(secant_line, RIGHT, buff=0.2).set_color(color)
            num = DecimalNumber(num_decimal_places=2
            ).set_value(graph2.underlying_function(x)
            ).set_color(color).scale(0.6).next_to(text, RIGHT, buff=0.2)
            result = VGroup(secant_line, text, num, dot)
            return result

        def get_horizontal_line(x, plane, graph, color, width):
            result = VGroup()
            line = Line(
                plane.coords_to_point(0, graph.underlying_function(x)),
                plane.coords_to_point(x, graph.underlying_function(x)),
                stroke_color = color, stroke_width = width
            )
            tri = RegularPolygon(n=3).scale(0.1
            ).set_color(color)
            if x > 0:
                tri.rotate(-PI/2).next_to(line, LEFT, buff=0)
            else:
                tri.rotate(PI/2).next_to(line, RIGHT, buff=0)
            result.add(line, tri)
            return result

        ##DEFINING ALL THE SHIT I NEED FOR THE SCENE##

        graph1 = plane.get_graph(lambda x : 1/3*x**3 - x**2 - 3*x + 1,
        x_min = -3.5, x_max = 5, color = RED)
        graph1concave = plane.get_graph(lambda x : 1/3*x**3 - x**2 - 3*x + 1,
        x_min = -3.5, x_max = 1, color = RED)
        graph1_lab = MathTex("f(x)=\\frac{1}{3}{x}^{3} - {x}^{2} - 3x + 1").scale(0.5
        ).next_to(graph1, UR, buff=0.2).set_color(RED).shift(DOWN*0.3)

        graph2 = plane.get_graph(lambda x : x**2 - 2*x - 3,
        x_min = -3.5, x_max = 5, color = BLUE)
        graph2_lab = MathTex("f'(x)={x}^{2}-2x-3").scale(0.5).next_to(
            graph2, UR, buff=0.2).set_color(BLUE).shift(DOWN*0.8)

        graph3 = plane.get_graph(lambda x : 2*x - 2, x_min = -3.5, x_max = 5, color = GREEN)
        graph3_lab = MathTex("f''(x)=2x-2").scale(0.5).next_to(
            graph3, UR, buff=0.2).set_color(GREEN).shift(DOWN*0.3)

        poi = Circle(radius = 0.05, color = PINK, stroke_width = 3).move_to(
            plane.coords_to_point(1, graph1.underlying_function(1))
        )

        s = ValueTracker(-3.5) #Tracking the slope on f(x) and horiz_line on f'(x)
        k = ValueTracker(-3.5) #Tracking the slope on f'(x) and horiz_line on f''(x)

        slope_group_graph1 = get_secant_group(x=-3.5,
        plane = plane, graph = graph1, color = PURPLE, width = 2)
        slope_group_graph1.add_updater(lambda k : k.become(
            get_secant_group(x=s.get_value(), plane=plane, graph=graph1,
            color = PURPLE, width=2
        )))

        horiz_line_graph2 = always_redraw(lambda : get_horizontal_line(x=s.get_value(),
        plane = plane, graph = graph2, color = ORANGE, width = 3))

        slope_line_graph1 = always_redraw(lambda : get_secant_line(x=s.get_value(),
        plane=plane, graph = graph1, color = PURPLE, width = 2))

        slope_line_graph2 = always_redraw(lambda : get_secant_line(x=k.get_value(),
        plane = plane, graph = graph2, color = YELLOW, width = 2))

        horiz_line_graph3 = always_redraw(lambda : get_horizontal_line(x=k.get_value(),
        plane = plane, graph = graph3, color = WHITE, width = 3))

        maxline1 = Line(LEFT*6, LEFT*5.6+UP*0.5, color = YELLOW)
        maxline2 = Line(LEFT*5.55+UP*0.5, LEFT*4.9+UP*0.5, color = YELLOW)
        maxline3 = Line(LEFT*4.85+UP*0.5, LEFT*4.45, color = YELLOW)

        minline1 = Line(RIGHT*4+DOWN*1, RIGHT*4.4+DOWN*1.5, color = YELLOW)
        minline2 = Line(RIGHT*4.45+DOWN*1.5, RIGHT*5.1+DOWN*1.5, color = YELLOW)
        minline3 = Line(RIGHT*5.15+DOWN*1.5, RIGHT*5.55+DOWN*1, color = YELLOW)

        #PLAYING THE ANIMATION
        
        self.play(Write(plane))
        self.wait()
        self.play(LaggedStart(
            ShowCreation(graph1), ShowCreation(graph2),
            Write(graph1_lab), Write(graph2_lab)), lag_ratio=0.5, run_time=3)
        self.add(slope_group_graph1, horiz_line_graph2)
        self.play(s.animate.set_value(1), run_time=3) #ADD more RUN TIME
        self.play(DrawBorderThenFill(poi))
        self.play(s.animate.set_value(4), run_time=3) #ADD more RUN TIME
        self.wait()
        self.play(graph1.animate.set_stroke(opacity=0.2))
        self.play(ShowCreation(graph1concave))
        self.play(s.animate.set_value(-3.5), run_time=3) #ADD more RUN TIME
        self.wait()
        self.play(s.animate.set_value(4), run_time=3) #ADD more RUN TIME
        self.play(graph1concave.animate.set_stroke(opacity=0.1),
        graph1.animate.set_stroke(opacity=0.1),
        graph1_lab.animate.set_stroke(opacity=0.1), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(graph3), Write(graph3_lab))
        self.wait()
        self.remove(slope_group_graph1, horiz_line_graph2)
        self.play(s.animate.set_value(-3.5), run_time=0.1)
        self.play(ShowCreation(VGroup(
            slope_line_graph2, horiz_line_graph3
        )))
        self.play(k.animate.set_value(4), run_time=3) #ADD more RUN TIME
        self.wait()
        self.remove(slope_line_graph2, horiz_line_graph3)
        self.play(graph2.animate.set_stroke(opacity=0.1),
        graph2_lab.animate.set_stroke(opacity=0.1),
        graph1.animate.set_stroke(opacity=1),
        graph1_lab.animate.set_stroke(opacity=1),
        graph1concave.animate.set_stroke(opacity=1))
        self.add(slope_group_graph1)
        self.play(s.animate.set_value(1), run_time=3) #ADD more RUN TIME
        self.play(Indicate(poi))
        self.play(s.animate.set_value(4), run_time=3) #ADD more RUN TIME
        self.play(graph1.animate.set_stroke(opacity=0.7))
        self.remove(slope_group_graph1)
        self.play(s.animate.set_value(-3.5))
        self.add(slope_line_graph1)
        self.play(s.animate.set_value(-1.3), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(maxline1))
        self.play(s.animate.set_value(-1), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(maxline2))
        self.play(s.animate.set_value(-0.7), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(maxline3))
        self.wait()
        self.play(s.animate.set_value(2.7), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(minline1))
        self.play(s.animate.set_value(3), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(minline2))
        self.play(s.animate.set_value(3.3), run_time=3) #ADD more RUN TIME
        self.play(ShowCreation(minline3))
        self.wait()
        self.play(s.animate.set_value(4))

class Concavity(Scene):
    def construct(self):
        self.show_concavity()

    def show_concavity(self):
        plane = get_plane(x_min = -4, x_max = 5, y_min = -15, y_max = 15,
        x_unit_size = 0.6, y_unit_size=0.2,
        x_nums = range(-4, 6, 1), y_nums = range(-15, 16, 5), 
        num_scale=0.3)

        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)
        
        curve = plane.get_graph(lambda x : 1/3 * x**3 - x**2 - 3*x + 1, 
        x_min = -3.5, x_max = 5, color = BLUE)
        curve_lab = MathTex("f(x)=\\frac{1}{3}{x}^{3} - {x}^{2} - 3x + 1").scale(0.5
        ).next_to(curve, UR, buff=0.2).set_color(BLUE).shift(DOWN*0.3)

        deriv_1 = plane.get_graph(lambda x : x**2 - 2*x -3, 
        x_min = -3.5, x_max = 5, color = RED)
        deriv_1_lab = MathTex("f'(x)={x}^{2}-2x-3").scale(0.5).next_to(
        deriv_1, UR, buff=0.2).set_color(RED).shift(DOWN*0.8)

        deriv_2 = plane.get_graph(lambda x : 2*x - 2,
        x_min = -3.5, x_max = 5, color = GREEN)
        deriv_2_lab = MathTex("f''(x)=2x-2").scale(0.5).next_to(
        deriv_2, UR, buff=0.2).set_color(GREEN).shift(DOWN*0.3)

        self.play(LaggedStart(
            Write(plane), ShowCreation(curve), Write(curve_lab),
            run_time = 2, lag_ratio = 0.4))
        self.wait()

        k = ValueTracker(-3.5)
        curve_slope = always_redraw(lambda : 
        get_secant_line(x = k.get_value(), plane = plane, graph = curve, color = PURPLE_B, width = 5))

        self.play(LaggedStart(
            ShowCreation(deriv_1), Write(deriv_1_lab), run_time=2, lag_ratio=0.5))
        self.add(curve_slope)
        self.play(k.animate.set_value(5), run_time=5, rate_func=linear)
        self.wait(2)
        self.remove(curve_slope)

        self.play(curve.animate.set_stroke(opacity=0.1), 
        FadeOut(curve_lab), ShowCreation(deriv_2),
        Write(deriv_2_lab), run_time=3)
        self.wait()

        r = ValueTracker(-3.5)
        deriv_1_slope = always_redraw(lambda :
        get_secant_line(x = r.get_value(), plane = plane, graph = deriv_1, color = PURPLE_B, width = 5))

        self.add(deriv_1_slope)
        self.play(r.animate.set_value(5), run_time=5, rate_func=linear)
        self.wait(2)
        self.remove(deriv_1_slope)

        self.play(curve.animate.set_stroke(opacity=1), 
        FadeIn(curve_lab),
        deriv_1.animate.set_stroke(opacity=0.1), 
        FadeOut(deriv_1_lab), run_time=3)

        self.play(LaggedStart(
            WiggleOutThenIn(curve), WiggleOutThenIn(deriv_2), run_time=3, lag_ratio=0.3)
        )
        self.wait()

        p = ValueTracker(-3.5)
        detailed_curve_slope = always_redraw(lambda : 
        get_secant_group(x = p.get_value(), plane = plane, graph = curve, color = YELLOW, width = 5))

        
        slope_text = always_redraw(lambda : Tex("m =").scale(0.6).next_to(
            detailed_curve_slope, RIGHT, buff=0.1).set_color(YELLOW))

        slope_val = always_redraw(lambda : DecimalNumber(num_decimal_places=2
        ).set_value(deriv_1.underlying_function(p.get_value())
        ).set_color(YELLOW).scale(0.6).next_to(slope_text, RIGHT, buff=0.1))

        

        poi = Dot().move_to(plane.coords_to_point(1, curve.underlying_function(1))).scale(0.8).set_color(BLUE)
        concave_down = plane.get_graph(lambda x : 1/3 * x**3 - x**2 - 3*x + 1, 
        x_min = -3.5, x_max = 1, color = PINK)
        concave_up = plane.get_graph(lambda x : 1/3 * x**3 - x**2 - 3*x + 1, 
        x_min = 1, x_max = 5, color = ORANGE)

        down_text = Tex("Concave Down").set_color(PINK).scale(0.7).next_to(concave_down, LEFT)
        up_text = Tex("Concave Up").set_color(ORANGE).scale(0.7).next_to(concave_up, RIGHT)

        self.add(detailed_curve_slope, slope_text, slope_val)
        self.play(p.animate.set_value(4), run_time=10, rate_func = smooth)
        self.wait()
        self.play(p.animate.set_value(-2), run_time=4, rate_func = linear)
        self.wait()
        self.play(p.animate.set_value(1), run_time=8, rate_func = smooth)
        self.play(FadeOut(curve), FadeIn(concave_down), 
        FadeIn(concave_up), DrawBorderThenFill(poi),
           run_time=6)
        self.play(p.animate.set_value(4), run_time=8, rate_func = smooth)
        self.wait()
        
        self.remove(detailed_curve_slope, slope_text, slope_val)

        self.play(LaggedStart(
            Write(down_text), Write(up_text), run_time=2, lag_ratio = 0.5)
        )

        ##END SCENE##
        self.play(*[FadeOut(m) for m in self.get_top_level_mobjects()])

class HorizPoi(Scene):
    def construct(self):
        self.show_horiz_poi()

    def show_horiz_poi(self):
        
        plane = get_plane(x_min = -3, x_max = 3, y_min = -8, y_max = 8, y_unit_size = 0.5, x_unit_size = 2,
            x_nums = range(-3, 4, 1), y_nums = range(-8, 9, 2), num_scale = 0.4)

        graph = plane.get_graph(lambda x : x**3, x_min = -3, x_max = 3, color = BLUE)
        graph_lab = MathTex("f(x)={x}^{3}").scale(0.8).next_to(graph, UR, buff=0.3)

        deriv = plane.get_graph(lambda x : 3*x**2, x_min = -3, x_max = 3)

        k = ValueTracker(-3)
        slope = always_redraw(lambda : get_secant_group(x = k.get_value(), plane = plane, graph = graph, color = YELLOW, width = 5))

        slope_text = always_redraw(lambda : Tex("m =").scale(0.6).next_to(
            slope, RIGHT, buff=0.1).set_color(YELLOW))

        slope_val = always_redraw(lambda : DecimalNumber(num_decimal_places=2
        ).set_value(deriv.underlying_function(k.get_value())
        ).set_color(YELLOW).scale(0.6).next_to(slope_text, RIGHT, buff=0.1))

        self.play(LaggedStart(
            Write(plane), ShowCreation(graph), Write(graph_lab), run_time=2, lag_ratio=0.3
        ))
        self.add(slope, slope_text, slope_val)
        self.play(k.animate.set_value(0), run_time=5, rate_func = smooth)
        self.play(k.animate.set_value(3), run_time=5, rate_func = smooth)
        self.wait()


class CurveSketchingExample(Scene):
    def construct(self):

        plane = get_plane(x_min = -6, x_max = 4, y_min = -10, y_max = 70, 
        x_unit_size = 0.6, y_unit_size = 0.08, x_nums = range(-6, 5, 1),
        y_nums = range(-10, 71, 10), num_scale = 0.3)

        new_origin = DOWN*2+RIGHT*1.5
        plane.shift(new_origin)

        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        curve = plane.get_graph(lambda x : 2/3 * x**3 + 4*x**2 - 10*x + 1/3, 
        x_min = -6, x_max = 4, color = BLUE)

        deriv = plane.get_graph(lambda x : 2*x**2 + 8*x - 10, x_min = -6, x_max = 4)

        curve_lab = MathTex("f(x)=\\frac{2}{3}{x}^{3} + 4{x}^{2} - 10x + \\frac{1}{3}"
        ).scale(0.47).next_to(curve, UR, buff=0.1).set_color(BLUE).shift(DOWN)

        deriv_1 = MathTex("f'(x)=2{x}^{2} + 8x - 10").scale(0.47).next_to(curve_lab, DOWN, aligned_edge = LEFT).set_color(RED)
        deriv_2 = MathTex("f''(x)=4x+8").scale(0.47).next_to(deriv_1, DOWN, aligned_edge = LEFT).set_color(GREEN)

        k = ValueTracker(-6) #Tracking the x value of the slope
        slope = always_redraw(lambda : get_secant_line(
            x = k.get_value(), plane = plane, graph = curve, color = YELLOW, width = 6))

        maxpt = Dot().move_to(plane.coords_to_point(-5,67)).set_color(RED)
        maxpt_lab = MathTex("(-5,67)").scale(0.5).next_to(maxpt, UP, buff=0.1).set_color(RED)

        minpt = Dot().move_to(plane.coords_to_point(1,-5)).set_color(RED)
        minpt_lab = MathTex("(1,-5)").scale(0.5).next_to(minpt, DOWN, buff=0.1).set_color(RED)

        poi = Dot().move_to(plane.coords_to_point(-2,31)).set_color(GREEN)
        poi_lab = MathTex("(-2,31)").scale(0.5).next_to(poi, RIGHT, buff=0.1).set_color(GREEN)

        p = ValueTracker(-4)
        detailed_slope = always_redraw(lambda : get_secant_group(
            x = p.get_value(), plane = plane, graph = curve, color = YELLOW, width = 6
        ))

        slope_text = always_redraw(lambda : Tex("m =").scale(0.6).next_to(
            detailed_slope, RIGHT, buff=0.1).set_color(YELLOW))

        slope_val = always_redraw(lambda : DecimalNumber(num_decimal_places=2
        ).set_value(deriv.underlying_function(p.get_value())
        ).set_color(YELLOW).scale(0.6).next_to(slope_text, RIGHT, buff=0.1))

        concave_down = plane.get_graph(lambda x : 2/3 * x**3 + 4*x**2 - 10*x + 1/3, 
        x_min = -6, x_max = -2, color = PINK)

        concave_up = plane.get_graph(lambda x : 2/3 * x**3 + 4*x**2 - 10*x + 1/3, 
        x_min = -2, x_max = 4, color = ORANGE)

        step1 = Tex("1. Evaluate $f'(x)$ and $f''(x)$")
        step2 = Tex("2. Let $f'(x)=0$ to find stationary points")
        step3 = Tex("3. Verify nature using $f''(x)$")
        step4 = Tex("4. Let $f''(x)=0$ to find points of inflection")
        step5 = Tex("5. Verify concavity by $f''(x)$ concavity table")

        inst = VGroup(step1, step2, step3, step4, step5).scale(0.45)
        inst.arrange(DOWN, aligned_edge = LEFT, buff=0.3).to_edge(UL, buff=0.4)

        self.play(LaggedStart(
            Write(plane), ShowCreation(curve), Write(curve_lab), run_time=1, lag_ratio = 0.3
        ))
        self.wait()
        self.play(Write(step1))
        self.wait()
        self.play(Write(VGroup(deriv_1, deriv_2)))
        self.play(WiggleOutThenIn(VGroup(step1, deriv_1, deriv_2)))
        self.wait()

        self.play(Write(step2))
        self.play(ShowCreation(VGroup(maxpt, minpt)))
        self.add(slope)
        self.play(k.animate.set_value(-5), run_time=3)
        self.wait()
        self.play(k.animate.set_value(1), run_time=7)
        self.wait()
        self.remove(slope)
        self.play(Write(VGroup(maxpt_lab, minpt_lab)))

        self.play(Write(step3))
        self.play(WiggleOutThenIn(VGroup(step3, deriv_2)))
        self.wait()
        self.play(Indicate(maxpt_lab))
        self.play(Indicate(minpt_lab))
        self.wait()

        self.play(Write(step4))
        self.play(ShowCreation(poi))
        self.add(detailed_slope, slope_text, slope_val)
        self.play(p.animate.set_value(0), run_time=8)
        self.wait()
        self.remove(detailed_slope, slope_text, slope_val)
        self.play(ShowCreation(poi_lab))

        self.play(Write(step5))
        self.wait()
        self.play(ShowCreation(concave_up), ShowCreation(concave_down))
        self.wait()

        self.play(*[FadeOut(m) for m in self.get_top_level_mobjects()])

class CurveSketchEx(Scene):
    def construct(self):

        plane = get_plane(x_min = -1, x_max = 5, y_min = 0, y_max = 60, 
        x_unit_size = 1, y_unit_size=0.12,
        x_nums = range(-1, 6, 1), y_nums = range(0, 61, 10), 
        num_scale = 0.4)

        plane.shift(DOWN*3.5)

        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        curve = plane.get_graph(lambda x : x**4 - 8*x**3 + 18*x**2 + 4,
        x_min = -1, x_max = 5, color = BLUE)

        deriv = plane.get_graph(lambda x : 4*x**3 - 24*x**2 + 36*x, x_min = -1, x_max = 5)

        curve_lab = MathTex("f(x)={x}^{4} - 8{x}^{3} + 18{x}^{2} + 4").scale(0.6
        ).next_to(curve, RIGHT).set_color(BLUE)

        minpt = Dot().move_to(plane.coords_to_point(0,4)).set_color(GREEN)
        minpt_lab = MathTex("(0,4)").scale(0.5).next_to(minpt, DOWN).set_color(GREEN).add_background_rectangle()

        poi1 = Dot().move_to(plane.coords_to_point(1,15)).set_color(GREEN)
        poi1_lab = MathTex("(1,15)").scale(0.5).next_to(poi1, RIGHT).set_color(GREEN)

        poi2 = Dot().move_to(plane.coords_to_point(3,31)).set_color(GREEN)
        poi2_lab = MathTex("(3,31)").scale(0.5).next_to(poi2, DOWN).set_color(GREEN)

        k = ValueTracker(-0.5)
        slope = always_redraw(lambda : get_secant_group(x = k.get_value(), plane = plane, graph = curve, color = YELLOW, width = 6))

        slope_text = always_redraw(lambda : Tex("m =").scale(0.6).next_to(
            slope, RIGHT, buff=0.1).set_color(YELLOW))

        slope_val = always_redraw(lambda : DecimalNumber(num_decimal_places=2
        ).set_value(deriv.underlying_function(k.get_value())
        ).set_color(YELLOW).scale(0.6).next_to(slope_text, RIGHT, buff=0.1))

        self.play(Write(plane))
        self.wait()

        self.play(LaggedStart(
            ShowCreation(minpt), FadeIn(minpt_lab), 
            ShowCreation(poi2), Write(poi2_lab), run_time=4, lag_ratio = 0.4))

        self.wait()
        self.add(slope)

        self.play(k.animate.set_value(0.5), run_time=5)
        self.wait()
        self.remove(slope)
        self.play(k.animate.set_value(2.5), run_time=0.1)
        self.add(slope)
        self.play(k.animate.set_value(3.5), run_time=5)
        self.wait()
        self.remove(slope)

        self.play(ShowCreation(poi1), Write(poi1_lab))
        self.wait()

        self.play(k.animate.set_value(0.5), run_time=0.1)
        self.add(slope, slope_text, slope_val)
        self.play(k.animate.set_value(1.5), run_time=8)
        self.wait()
        self.remove(slope, slope_text, slope_val)

        self.play(ShowCreation(curve), run_time=10)
        self.play(k.animate.set_value(-1), run_time=0.1)

        self.add(slope)
        self.play(k.animate.set_value(5), run_time=6)
       