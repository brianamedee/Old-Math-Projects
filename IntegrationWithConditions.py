from manimlib.imports import *
import numpy as np

class SimpleExample(Scene):
        
        def construct(self):
            self.simple_example()

        def simple_example(self):

            #CODE FOR NUMBER PLANE FOR GRADIENT FUNCTION
            plane_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.25,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -2, "x_max" : 5, "unit_size": 0.4,
                "numbers_to_show": range(-2, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -6, # y_min
                "x_max" : 13,  # y_max
                "unit_size": 0.3,
                "numbers_to_show": range(-6, 14, 1),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : BLUE,
            }  
            )

            plane = NumberPlane(**plane_config)

            #shifting the origin

            new_origin = LEFT*4+DOWN*1.5
            plane.shift(new_origin)

            # rotate y labels
            for label in plane.y_axis.numbers:
                label.rotate(-PI/2)

            input_tracker_p1 = ValueTracker(-2)

            def get_x_value(input_tracker):
                return input_tracker.get_value()

            def get_y_value(input_tracker):
                return graph1.underlying_function(get_x_value(input_tracker))

            def get_x_point(input_tracker):
                return plane.coords_to_point(get_x_value(input_tracker),0)

            def get_y_point(input_tracker):
                return plane.coords_to_point(0,get_y_value(input_tracker))

            def get_graph_point(input_tracker):
                return plane.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

            def get_v_line(input_tracker):
                return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

            def get_h_line(input_tracker):
                return Line(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4, color=TEAL_B)

            def get_secant_line(input_tracker):
                x = interpolate(input_tracker.get_value(), 4, 0.01)
                dx = 0.01
                p1 = plane.input_to_graph_point(x, graph1)
                p2 = plane.input_to_graph_point(x + dx, graph1)
                secant_line = Line(p1, p2, color=GREEN)
                secant_line.scale_in_place(2 / secant_line.get_length())
                return secant_line

            #CODE FOR NUMBER PLANE FOR ORIGINAL FUNCTION

            plane2_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.25,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -2, "x_max" : 5, "unit_size": 0.4,
                "numbers_to_show": range(-2, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -6, # y_min
                "x_max" : 13,  # y_max
                "unit_size": 0.3,
                "numbers_to_show": range(-6, 14, 1),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : BLUE,
            }  
            )

            plane2 = NumberPlane(**plane2_config)

            #shifting the origin

            new2_origin = RIGHT*3+DOWN*1.5
            plane2.shift(new2_origin)

            # rotate y labels
            for label in plane2.y_axis.numbers:
                label.rotate(-PI/2)

            input_tracker_p2 = ValueTracker(-2)

            def get_x2_value(input_tracker):
                return input_tracker.get_value()

            def get_y2_value(input_tracker):
                return graph2.underlying_function(get_x2_value(input_tracker))

            def get_x2_point(input_tracker):
                return plane2.coords_to_point(get_x2_value(input_tracker),0)

            def get_y2_point(input_tracker):
                return plane2.coords_to_point(0,get_y2_value(input_tracker))

            def get_graph2_point(input_tracker):
                return plane2.coords_to_point(get_x2_value(input_tracker),get_y2_value(input_tracker))

            def get_v2_line(input_tracker):
                return DashedLine(get_x2_point(input_tracker), get_graph2_point(input_tracker), stroke_width=4)

            def get_h2_line(input_tracker):
                return Line(get_graph2_point(input_tracker), get_y2_point(input_tracker), stroke_width=4, color=PURPLE)

            def get_secant2_line(input_tracker):
                x = interpolate(input_tracker.get_value(), 4, 0.01)
                dx = 0.01
                p1 = plane2.input_to_graph_point(x, graph2)
                p2 = plane2.input_to_graph_point(x + dx, graph2)
                secant_line = Line(p1, p2, color=TEAL_B)
                secant_line.scale_in_place(1.5 / secant_line.get_length())
                return secant_line

            #DEFINING FUNCTIONS TO GO ON NUMBER PLANES
            def function_1(x):
                return -x**2 + 2*x + 4

            c = ValueTracker(0)

            def function_2(x):
                return -1/3*x**3 + x**2 + 4*x + c.get_value()  #CORRECT C VALUE AT c=-1

            graph1 = plane.get_graph(function_1, 
            color = YELLOW, x_min = -2, x_max = 4)

            graph1_lab = TexMobject("f(x) = -{ x }^{ 2 }+2x+ 4")
            graph1_lab.set_color(YELLOW).next_to(plane, UP, buff=0.4).scale(0.6)

            slopetext = TexMobject("slope=").scale(0.6)
            slopetext.set_color(TEAL_B).next_to(plane, RIGHT, buff=0.5)

            slopevalue = DecimalNumber(0, num_decimal_places=2, include_sign=False).scale(0.6).set_color(TEAL_B)
            slopevalue.next_to(slopetext, RIGHT, buff=0.1)
            slopevalue.add_updater(lambda s : s.set_value(get_y_value(input_tracker_p1)))

            horiz1 = get_h_line(input_tracker_p1)
            horiz1.add_updater(lambda h : h.become(get_h_line(input_tracker_p1)))

            vert1 = get_v_line(input_tracker_p1)
            vert1.add_updater(lambda v : v.become(get_v_line(input_tracker_p1)))

            graph1dot = Dot().move_to(get_graph_point(input_tracker_p1)).scale(0.7)
            graph1dot.add_updater(lambda d : d.move_to(get_graph_point(input_tracker_p1)))

            graph2= always_redraw(lambda : plane2.get_graph(function_2, color = RED,
            x_min = -2, x_max = 4))

            graph2_lab = TexMobject("F(x) = -\\frac { 1 }{ 3 } { x }^{ 3 }+{ x }^{ 2 }+4x+", "c")
            graph2_lab.next_to(plane2, UP, buff = 0.4).scale(0.6)
            graph2_lab[0].set_color(RED)
            graph2_lab[1].set_color(DARK_BLUE).scale(1)

            graph2dot = Dot().move_to(get_graph2_point(input_tracker_p2)).scale(0.7)
            graph2dot.add_updater(lambda d : d.move_to(get_graph2_point(input_tracker_p2)))

            vert2 = get_v2_line(input_tracker_p2)
            vert2.add_updater(lambda v : v.become(get_v2_line(input_tracker_p2)))

            graph2_slopes = get_secant2_line(input_tracker_p2)
            graph2_slopes.add_updater(lambda s : s.become(get_secant2_line(input_tracker_p2)))

            condition_dot = Dot().move_to(plane2.coords_to_point(3,11)).scale(0.8).set_color(DARK_BLUE)

            c_text = TextMobject("c $=$").scale(0.8).set_color(DARK_BLUE).next_to(slopetext, DOWN)
            c_value = DecimalNumber(c.get_value(), num_decimal_places = 2, include_sign = False)
            c_value.next_to(c_text, RIGHT, buff=0.1).scale(0.8).set_color(DARK_BLUE)
            c_value.add_updater(lambda k : k.set_value(c.get_value()))

            #INTEGRATING TEXT

            solve_text_1 = TexMobject("F(x)", " =", "\int{", "-{ x }^{ 2 }", "+2x","+4", "\quad dx" "}")
            solve_text_1.scale(0.6).next_to(graph1_lab, RIGHT, buff=0.5)

            solve_text_2 = TexMobject("F(x) = ", "-\\frac { 1 }{ 3 } { x }^{ 3 }", "+{ x }^{ 2 }", "+4x", "+c")
            solve_text_2.scale(0.6).next_to(solve_text_1, DOWN, buff=0.5)

            initial_question = TextMobject("Equation of curve that passes", " (3,11)?").add_background_rectangle()


            #PLAYING ANIMATION, FORMULATING THE PROBLEM
            self.play(Write(plane))
            self.play(Write(plane2))
            self.play(LaggedStart(
                ShowCreation(graph1), Write(graph1_lab), lag_ratio = 1, run_time = 3))
            self.add(slopetext, slopevalue, horiz1, vert1,
            graph1dot, graph2_slopes)
            self.play(input_tracker_p1.set_value, 4,
            input_tracker_p2.set_value, 4, run_time=3)
            self.play(input_tracker_p1.set_value, -2,
            input_tracker_p2.set_value, -2, run_time=3)
            self.play(FadeOut(graph2_slopes))
            self.play(Write(initial_question), run_time=2)
            self.wait()
            self.play(ReplacementTransform(initial_question[2].copy(), condition_dot))
            self.play(FadeOut(initial_question))

            #PLAYING THE SLOPE AND CREATION
            self.add(graph2_slopes, graph2dot, vert2)
            self.play(input_tracker_p2.set_value, 4,
            input_tracker_p1.set_value, 4,
            ShowCreation(graph2), run_time=10, rate_func = linear)
            self.wait()
            self.play(FadeOut(VGroup(graph1dot, graph2dot, graph2_slopes,
            slopevalue, slopetext, horiz1, vert1, vert2)))
            self.play(Indicate(graph1_lab), rate_func = wiggle, run_time=2)

            #PLAY THE TEX FOR INTEGRATING THE FUNCTION
            self.play(Write(solve_text_1), run_time=2)
            self.play(Indicate(solve_text_1[0]))
            self.play(ShowCreation(solve_text_2[0]))
            self.play(
            LaggedStart(
                ReplacementTransform(solve_text_1[3].copy(), solve_text_2[1]),
                ReplacementTransform(solve_text_1[4].copy(), solve_text_2[2]),
                ReplacementTransform(solve_text_1[5].copy(), solve_text_2[3]),
                lag_ratio = 2, run_time = 4, rate_func = smooth))
            self.play(DrawBorderThenFill(solve_text_2[4], run_time=3))
            self.play(ReplacementTransform(graph1_lab.copy(), graph2_lab),
            FadeOut(VGroup(solve_text_1, solve_text_2)))

            #PLAYING THE MANIPULATION OF THE C VALUE
            self.play(LaggedStart(ReplacementTransform(graph2_lab[1].copy(), c_text), Write(c_value), 
            lag_ratio = 1, run_time = 3, rate_func = smooth))
            self.play(c.set_value, 1, run_time = 2, rate_func = smooth)
            self.play(c.set_value, -3, run_time = 5, rate_func = smooth)
            self.play(c.set_value, -1, run_time = 3, rate_func = smooth)
            self.wait()
            self.add(horiz1, vert1, graph2_slopes, graph1dot, graph2dot, vert2, slopevalue, slopetext)
            self.play(input_tracker_p1.set_value, 0,
            input_tracker_p2.set_value, 0, run_time=5, rate_func=smooth)
            self.play(input_tracker_p1.set_value, 3.2, 
            input_tracker_p2.set_value, 3.2, run_time=5, rate_func=smooth)
            self.wait()

class Kinematics(GraphScene):
        CONFIG = {
        "y_max" : 6,
        "y_min" : -6,
        "x_max" : 4,
        "x_min" : 0,
        "y_tick_frequency" : 2, 
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "graph_origin": RIGHT*3 + DOWN*0.5,
        "y_labeled_nums": range(-6, 7, 2),
        "x_labeled_nums": list(np.arange(0, 5, 1)),
        "x_axis_label": "",
        "y_axis_label": "",
        "x_axis_width":3,
        "y_axis_height":5,
        }
        def construct(self):
            self.complex_scene()

        def complex_scene(self):

            #CODE FOR NUMBER PLANE FOR GRADIENT FUNCTION
            plane_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.3,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : 0, "x_max" : 5, "unit_size": 0.6,
                "numbers_to_show": range(0, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -6, # y_min
                "x_max" : 7,  # y_max
                "unit_size": 0.42,
                "numbers_to_show": range(-6, 7, 1),
            },
            background_line_style = {
                "stroke_width" : 2, "stroke_opacity" : 1,
                "stroke_color" : BLUE_D,
            }  
            )

            plane = NumberPlane(**plane_config)

            #shifting the origin

            new_origin = DOWN*0.5+LEFT
            plane.shift(new_origin)

            # rotate y labels
            for label in plane.y_axis.numbers:
                label.rotate(-PI/2)

            input_tracker_p1 = ValueTracker(0.01) #TRACKING DOTS AND V/H LINES ON VELOCITY GRAPH

            def get_x_value(input_tracker):
                return input_tracker.get_value()

            def get_y_value(input_tracker):
                return vel_graph.underlying_function(get_x_value(input_tracker))

            def get_x_point(input_tracker):
                return plane.coords_to_point(get_x_value(input_tracker),0)

            def get_y_point(input_tracker):
                return plane.coords_to_point(0,get_y_value(input_tracker))

            def get_graph_point(input_tracker):
                return plane.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

            def get_v_line(input_tracker):
                return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

            def get_h_line(input_tracker):
                return Line(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4, color=ORANGE)
            


            #VALUETRACKER FOR CREATING GRAPHS NICELY
            v = ValueTracker(0.01)  #FOR CREATING VELOCITY GRAPH
            d = ValueTracker(0.01)  #FOR CREATING THE DISPLACEMENT GRAPHS
            s = ValueTracker(0.01)  #FOR GENERATING SLOPES WITH DOT ON DISPLACEMENT GRAPHS
            
            vel_graph = always_redraw(lambda : plane.get_graph(
                lambda x : x**3 - 6*x**2 + 11*x - 6,
                color = YELLOW_C, x_min = 0, x_max = v.get_value()))
            
            vel_vert = get_v_line(input_tracker_p1)
            vel_vert.add_updater(lambda v : v.become(get_v_line(input_tracker_p1)))

            vel_dot = Dot().move_to(get_graph_point(input_tracker_p1)).scale(0.5)
            vel_dot.add_updater(lambda d : d.move_to(get_graph_point(input_tracker_p1)))

            vel_horiz = get_h_line(input_tracker_p1)
            vel_horiz.add_updater(lambda h : h.become(get_h_line(input_tracker_p1)))
            
            vel_graph_lab = TexMobject("v(t)={t}^{3} - {6t}^{2} + 11t - 6")
            vel_graph_lab.set_color(YELLOW_C).scale(0.5).next_to(plane, UP, buff=0.4)

            vel_graph_title = TextMobject("Velocity Graph").next_to(plane, UP, buff=0.9).scale(0.8)
            vel_und = Underline(vel_graph_title)


            #ADDING COMPONENTS TO THE DISPLACEMENT FUNCTION ON GRAPH
            self.setup_axes(animate=True)

            #GRAPH ELEMENTS FOR WHEN C=4
            dis_graph_4c = always_redraw(lambda : self.get_graph(
                lambda x : 1/4*x**4 - 2*x**3 + 11/2*x**2 - 6*x + 4, 
            color = PURPLE_A, x_min =0, x_max = d.get_value()))

            dis_graph_4c_slopes = always_redraw(lambda : self.get_secant_slope_group(
                s.get_value(), dis_graph_4c, dx = 0.01, secant_line_color = ORANGE, secant_line_length=1
            ))

            dis_graph_4c_lab = TexMobject("d(t)=\\frac{{t}^{4}}{4} - 2{t}^{3} + \\frac{{11}{t}^{2}}{2} - 6t + 4")
            dis_graph_4c_lab.scale(0.3).next_to(dis_graph_4c, UP+RIGHT, buff=0.5).set_color(PURPLE_A).shift(LEFT*0.2+DOWN*1.85)
            
            #GRAPH ELEMENTS FOR WHEN C=2
            dis_graph_2c = always_redraw(lambda : self.get_graph(
                lambda x : 1/4*x**4 - 2*x**3 + 11/2*x**2 - 6*x + 1, 
            color = RED_C, x_min =0, x_max = d.get_value()))

            dis_graph_2c_slopes = always_redraw(lambda : self.get_secant_slope_group(
                s.get_value(), dis_graph_2c, dx = 0.01, secant_line_color = ORANGE, secant_line_length=1
            ))

            dis_graph_2c_lab = TexMobject("d(t)=\\frac{{t}^{4}}{4} - 2{t}^{3} + \\frac{{11}{t}^{2}}{2} - 6t + 1")
            dis_graph_2c_lab.scale(0.3).next_to(dis_graph_2c, UP+RIGHT, buff=0.5).set_color(RED_C).shift(DOWN*1.85+LEFT*0.2)

            #GRAPH ELEMENTS FOR WHEN C=-1
            dis_graph_1c = always_redraw(lambda : self.get_graph(
                lambda x : 1/4*x**4 - 2*x**3 + 11/2*x**2 - 6*x + -1, 
            color = GREEN_C, x_min =0, x_max = d.get_value()))

            dis_graph_1c_slopes = always_redraw(lambda : self.get_secant_slope_group(
                s.get_value(), dis_graph_1c, dx = 0.01, secant_line_color = ORANGE, secant_line_length=1
            ))

            dis_graph_1c_lab = TexMobject("d(t)=\\frac{{t}^{4}}{4} - 2{t}^{3} + \\frac{{11}{t}^{2}}{2} - 6t - 1")
            dis_graph_1c_lab.scale(0.3).next_to(dis_graph_1c, UP+RIGHT, buff=0.5).set_color(GREEN_C).shift(DOWN*1.85+LEFT*0.2)

            dis_graph_title = TextMobject("Displacement Graph")
            dis_graph_title.next_to(vel_graph_title, RIGHT, buff=0.75).scale(0.8)
            dis_und = Underline(dis_graph_title)

            #ADDING COMPONENTS FOR PARTICLES MOVING AROUND

            case1_text = TextMobject("Case 1").set_color(GREEN_C).shift(UP*3+LEFT*4)
            case2_text = TextMobject("Case 2").set_color(RED_C).shift(UP+LEFT*4)
            case3_text = TextMobject("Case 3").set_color(PURPLE_A).shift(DOWN+LEFT*4)

            case1_fixed = Dot().next_to(case1_text.get_center(), DOWN, buff=0.5).scale(0.5)
            case2_fixed = Dot().next_to(case2_text.get_center(), DOWN, buff=0.5).scale(0.5)
            case3_fixed = Dot().next_to(case3_text.get_center(), DOWN, buff=0.5).scale(0.5)

            fixed1_origin_text = TextMobject("Fixed Origin").scale(0.4).next_to(case1_fixed, UP+LEFT, buff=0.2)
            fixed2_origin_text = TextMobject("Fixed Origin").scale(0.4).next_to(case2_fixed, UP+LEFT, buff=0.2)
            fixed3_origin_text = TextMobject("Fixed Origin").scale(0.4).next_to(case3_fixed, UP+LEFT, buff=0.2)

            case1_particle = Dot().next_to(case1_fixed, LEFT, buff=0.5).set_color(GREEN_C).scale(0.8)
            case2_particle = Dot().next_to(case2_fixed, RIGHT, buff=0.5).set_color(RED_C).scale(0.8)
            case3_particle = Dot().next_to(case3_fixed, RIGHT, buff=2).set_color(PURPLE_C).scale(0.8)

            vector1 = Vector().set_color(GREEN_C)
            vector1.put_start_and_end_on(case1_fixed.get_center(), case1_particle.get_center())
            vector1.add_updater(lambda v : v.put_start_and_end_on(
                case1_fixed.get_center(), case1_particle.get_center()))

            vector2 = Vector().set_color(RED_C)
            vector2.put_start_and_end_on(case2_fixed.get_center(), case2_particle.get_center())
            vector2.add_updater(lambda v : v.put_start_and_end_on(
                case2_fixed.get_center(), case2_particle.get_center()))

            vector3 = Vector().set_color(PURPLE_A)
            vector3.put_start_and_end_on(case3_fixed.get_center(), case3_particle.get_center())
            vector3.add_updater(lambda v : v.put_start_and_end_on(
                case3_fixed.get_center(), case3_particle.get_center()))

            question_mark = TextMobject("?").scale(6).move_to(self.axes.get_center())

            case_win_group = VGroup(vector3, case3_particle, fixed3_origin_text,
            case3_fixed, case3_text)
            case_win_box = SurroundingRectangle(case_win_group).set_color(WHITE)

            dis_graph_lab = TexMobject("d(t)=\\frac{{t}^{4}}{4} - 2{t}^{3} + \\frac{{11}{t}^{2}}{2} - 6t + c")
            dis_graph_lab.scale(0.5).next_to(dis_graph_title, DOWN, buff=0.5).set_color_by_gradient(GREEN_C, PURPLE_A)


            #PLAYING THE GRAPHS
            self.play(LaggedStart(
                Write(plane), Write(vel_graph_title),
                ShowCreation(vel_und),
                Write(dis_graph_title), ShowCreation(dis_und),
                lag_ratio=1.5, run_time=4, rate_func=smooth))
            self.add(vel_graph)

            #PLAYING THE ANIMATION OF THE INITIAL DOT MOVING WITH VELOCITY GRAPH
            self.play(LaggedStart(
                ShowCreation(case1_particle), ShowCreation(case2_particle),
            ShowCreation(case3_particle), lag_ratio = 1, run_time=3, rate_func=smooth))

            self.play(case1_particle.shift, LEFT*1.125,
            case2_particle.shift, LEFT*1.125,
            case3_particle.shift, LEFT*1.125,
            v.set_value, 1, run_time=3, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*0.055,
            case2_particle.shift, RIGHT*0.055,
            case3_particle.shift, RIGHT*0.055,
            v.set_value, 1.42, run_time=1.26, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*0.07,
            case2_particle.shift, RIGHT*0.07,
            case3_particle.shift, RIGHT*0.07,
            v.set_value, 2, run_time=1.74, rate_func=linear)

            self.play(case1_particle.shift, LEFT*0.07,
            case2_particle.shift, LEFT*0.07,
            case3_particle.shift, LEFT*0.07,
            v.set_value, 2.58, run_time=1.74, rate_func=linear)

            self.play(case1_particle.shift, LEFT*0.055,
            case2_particle.shift, LEFT*0.055,
            case3_particle.shift, LEFT*0.055,
            v.set_value, 3, run_time=1.26, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*1.125,
            case2_particle.shift, RIGHT*1.125,
            case3_particle.shift, RIGHT*1.125,
            v.set_value, 4, run_time=3, rate_func=linear)

            self.play(Write(vel_graph_lab))

            self.wait()
            self.play(FadeIn(question_mark), run_time=2)
            self.play(Indicate(question_mark), run_time=2)
            self.play(ReplacementTransform(vel_graph_lab.copy(), dis_graph_lab), run_time=5)
            self.play(FadeOut(question_mark), run_time=2)
            self.play(FadeOut(VGroup(case1_particle, case2_particle,
            case3_particle, vel_graph)))

            #RESETING VALUETRACKERS
            self.play(v.set_value, 0.01, run_time=0.5)
            self.wait()

            #PLACING THE FIXED ORIGINS TO THEN GIVE A SCOPE OF DISPLACEMENT
            self.add(case1_particle, case2_particle, case3_particle)
            self.play(ShowCreation(case1_fixed), Write(fixed1_origin_text), run_time=2)
            self.play(LaggedStart(
            ReplacementTransform(case1_fixed.copy(), case2_fixed),
            ReplacementTransform(fixed1_origin_text.copy(), fixed2_origin_text),
            ReplacementTransform(case1_fixed.copy(), case3_fixed),
            ReplacementTransform(fixed1_origin_text.copy(), fixed3_origin_text),
            lag_ratio = 1.5, run_time=4))
            self.play(DrawBorderThenFill(VGroup(vector1, vector2, vector3)))
            self.wait()
            self.add(dis_graph_4c, dis_graph_2c, dis_graph_1c, vel_graph)

            self.play(case1_particle.shift, LEFT*1.125,
            case2_particle.shift, LEFT*1.125,
            case3_particle.shift, LEFT*1.125,
            v.set_value, 1,
            d.set_value, 1, run_time=3, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*0.055,
            case2_particle.shift, RIGHT*0.055,
            case3_particle.shift, RIGHT*0.055,
            v.set_value, 1.42, 
            d.set_value, 1.42, run_time=1.26, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*0.07,
            case2_particle.shift, RIGHT*0.07,
            case3_particle.shift, RIGHT*0.07,
            v.set_value, 2, 
            d.set_value, 2, run_time=1.74, rate_func=linear)

            self.play(case1_particle.shift, LEFT*0.07,
            case2_particle.shift, LEFT*0.07,
            case3_particle.shift, LEFT*0.07,
            v.set_value, 2.58, 
            d.set_value, 2.58, run_time=1.74, rate_func=linear)

            self.play(case1_particle.shift, LEFT*0.055,
            case2_particle.shift, LEFT*0.055,
            case3_particle.shift, LEFT*0.055,
            v.set_value, 3, 
            d.set_value, 3, run_time=1.26, rate_func=linear)

            self.play(case1_particle.shift, RIGHT*1.125,
            case2_particle.shift, RIGHT*1.125,
            case3_particle.shift, RIGHT*1.125,
            v.set_value, 4, 
            d.set_value, 4, run_time=3, rate_func=linear)


            #SHOWING THAT RATE OF CHANGE OF DISPLACEMENT IS VELOCITY, AS A GUT CHECK
            self.play(LaggedStart(
                Write(dis_graph_1c_lab), Write(dis_graph_2c_lab), Write(dis_graph_4c_lab)
            ))

            self.add(vel_vert, vel_dot, vel_horiz,
            dis_graph_4c_slopes, dis_graph_2c_slopes, dis_graph_1c_slopes)

            self.play(s.set_value, 4, input_tracker_p1.set_value, 4,
            run_time = 12, rate_func = smooth)
            self.wait()

            self.play(ShowCreation(case_win_box), run_time=2)
            self.play(FadeOut(VGroup(vel_vert, vel_dot, vel_horiz, case_win_box,
            dis_graph_4c_slopes, dis_graph_2c_slopes, dis_graph_1c_slopes)))
            
            self.wait()