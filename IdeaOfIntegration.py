from manimlib.imports import *
import numpy as np

class IntroductionToIntegration(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "graph_origin": DOWN+LEFT*3.5,
        "y_labeled_nums": range(-10,11,5),
        "x_labeled_nums": list(np.arange(-5, 6, 5)),
        "x_axis_label": "",
        "y_axis_label": "",
        "x_axis_width":5,
        "y_axis_height":6.5,
        }

    def construct(self):

        self.setup_axes(animate=True)

        #DEFINING THE NUMBER PLANES NEEDED FOR ANIMATION

        plane_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -5, "x_max" : 6, "unit_size": 0.4
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -10, # y_min
                "x_max" : 11,  # y_max
                "unit_size": 0.3
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.8,
                "stroke_color" : GOLD,
            }  
        )

        plane = NumberPlane(**plane_config)

        #shifting the origin

        new_origin = RIGHT*3.5+DOWN
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)


        #PLANE2
        plane2_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -5, "x_max" : 6, "unit_size": 0.4
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -10, # y_min
                "x_max" : 11,  # y_max
                "unit_size": 0.3
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.8,
                "stroke_color" : GOLD,
            }  
        )

        plane2 = NumberPlane(**plane2_config)

        #shifting the origin

        new2_origin = LEFT*4.5+DOWN
        plane2.shift(new2_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        #DEFINING THE FUNCTIONS

        graph = self.get_graph(lambda x : 0.2*x**3 - 0.2*x**2 - 4*x, 
        color = BLUE, x_min = -5, x_max = 5)

        graph2 = plane.get_graph(lambda x : 0.6*x**2 - 0.4*x - 4,
        color = GREEN, x_min = -4.5, x_max = 4.5)

        #DEFINING UPDATERS AND FUNCTIONS FOR NUMBERPLANE1

        input_tracker_p1 = ValueTracker(-4.5)

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph2.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return plane.coords_to_point(get_x_value(input_tracker),0)

        def get_y_point(input_tracker):
            return plane.coords_to_point(0,get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return plane.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

        def get_h_line(input_tracker):
            return Line(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4, color=PURPLE)

        def get_secant_line(input_tracker):
            x = interpolate(input_tracker.get_value(), 2, 0.01)
            dx = 0.01
            p1 = plane.input_to_graph_point(x, graph2)
            p2 = plane.input_to_graph_point(x + dx, graph2)
            secant_line = Line(p1, p2, color=GREEN)
            secant_line.scale_in_place(2 / secant_line.get_length())
            return secant_line

        def get_dot_on_axes(x):
            return self.coords_to_point(x.get_value(), graph.underlying_function(x.get_value()))


        x = ValueTracker(-5)
        vertline = always_redraw(lambda: self.get_vertical_line_to_graph(
            x.get_value(), graph, line_class = DashedLine, color = WHITE)
        )

        slopes = always_redraw(lambda : self.get_secant_slope_group(
            x.get_value(), graph, dx=0.01, secant_line_color = PURPLE, secant_line_length = 2)
        )

        graphdot = Dot().move_to(get_dot_on_axes(x)).scale(0.9)
        graphdot.add_updater(lambda d : d.move_to(get_dot_on_axes(x)))

        graph2dot = Dot().move_to(get_graph_point(input_tracker_p1)).scale(0.9)
        graph2dot.add_updater(lambda d : d.move_to(get_graph_point(input_tracker_p1)))

        slopetext = TexMobject("slope=").scale(0.8).set_color(PURPLE).next_to(self.axes, UP+RIGHT, buff=-0.5)

        slopevalue = DecimalNumber(0, num_decimal_places=2, include_sign=False).scale(0.8).set_color(PURPLE)
        slopevalue.next_to(slopetext, RIGHT, buff=0.1)
        slopevalue.add_updater(lambda s : s.set_value(get_y_value(x)))

        horizlineg2 = get_h_line(input_tracker_p1).set_color(PURPLE)
        horizlineg2.add_updater(lambda h : h.become(get_h_line(input_tracker_p1)))

        vertlineg2 = get_v_line(input_tracker_p1)
        vertlineg2.add_updater(lambda v : v.become(get_v_line(input_tracker_p1)))

        #TITLES FOR GRAPHS

        graph1name = TexMobject("Function - f(x)").set_color_by_gradient(BLUE).next_to(self.axes, UP, buff=0.5)
        und1 = Underline(graph1name)

        graph2name = TexMobject("Derivative - f'(x)").set_color_by_gradient(GREEN).next_to(plane, UP, buff=0.5)
        und2 = Underline(graph2name)


        self.play(ShowCreation(graph))
        self.add(vertline, slopes, graphdot, slopevalue, slopetext)
        self.play(x.set_value, 4.5, run_time=6, rate_func=linear)
        self.wait()
        self.play(x.set_value, -4.5, run_time=6, rate_func=smooth)
        self.wait()
        self.play(LaggedStart(Write(graph1name), ShowCreation(und1)), run_time=2)

        self.play(Write(plane))
        self.add(vertlineg2, horizlineg2, graph2dot)
        self.play(x.set_value, 4.5,
        input_tracker_p1.set_value, 4.5,
        ShowCreation(graph2), run_time=12, rate_func=smooth)
        self.wait()
        self.play(LaggedStart(Write(graph2name),ShowCreation(und2)),run_time=3)
        self.wait()

        self.play(FadeOut(slopes), FadeOut(slopetext), FadeOut(graphdot), FadeOut(graph2dot),
        FadeOut(vertline), FadeOut(graph), FadeOut(graph2), FadeOut(vertlineg2), FadeOut(horizlineg2),
        FadeOut(slopevalue), ReplacementTransform(plane, plane2),
        self.axes.shift, RIGHT*7, graph1name.shift, RIGHT*7, graph2name.shift, LEFT*8,
        und1.shift, RIGHT*7, und2.shift, LEFT*8)
        self.wait()


        #DEFINING UPDATERS AND FUNCTIONS FOR NUMBERPLANE2

        input_tracker_p2 = ValueTracker(-4.5)

        def get_x2_value(input_tracker):
            return input_tracker.get_value()

        def get_y2_value(input_tracker):
            return graph3.underlying_function(get_x2_value(input_tracker))

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
            x = interpolate(input_tracker.get_value(), 2, 0.01)
            dx = 0.01
            p1 = plane.input_to_graph_point(x, graph3)
            p2 = plane.input_to_graph_point(x + dx, graph3)
            secant_line = Line(p1, p2, color=GREEN)
            secant_line.scale_in_place(2 / secant_line.get_length())
            return secant_line

        k = ValueTracker(-4.5)
        p = ValueTracker(-4.5)
        q = ValueTracker(-4.5)

        def get_dot_on_axes2(k):
            return self.coords_to_point(k.get_value(), graph4.underlying_function(k.get_value()))

        def get_dot_on_axes3(p):
            return self.coords_to_point(p.get_value(), graph5.underlying_function(p.get_value()))

        def get_dot_on_axes4(q):
            return self.coords_to_point(q.get_value(), graph6.underlying_function(q.get_value()))

        #KNOWN DERIVTIVE FUNCTION ON NUMBERPLANE2
        graph3 = plane2.get_graph(lambda x : 0.6*x**2 - 0.4*x - 4, 
        color = GREEN, x_min = -4.5, x_max = 4.5)

        #UNKNOWN ORIGINAL FUNCTION ON AXES
        graph4 = self.get_graph(lambda x : 0.2*x**3 - 0.2*x**2 - 4*x, color = BLUE, x_min = -4.5, x_max = 4.5)

        g4slopes = always_redraw(lambda: self.get_secant_slope_group(
            k.get_value(), graph4, dx = 0.01, include_secant_line = True, 
            secant_line_color = PURPLE, secant_line_length = 2
        ))

        graph5 = self.get_graph(lambda x : 0.2*x**3 - 0.2*x**2 - 4*x+2, color = BLUE, x_min = -4.5, x_max = 4.5)

        g5slopes = always_redraw(lambda: self.get_secant_slope_group(
            p.get_value(), graph5, dx = 0.01, include_secant_line = True, 
            secant_line_color = PURPLE, secant_line_length = 2
        ))

        graph6 = self.get_graph(lambda x : 0.2*x**3 - 0.2*x**2 - 4*x+4, color = BLUE, x_min = -4.5, x_max = 4.5)

        g6slopes = always_redraw(lambda: self.get_secant_slope_group(
            q.get_value(), graph6, dx = 0.01, include_secant_line = True, 
            secant_line_color = PURPLE, secant_line_length = 2
        ))

        vertlineg3 = get_v2_line(input_tracker_p2)
        vertlineg3.add_updater(lambda v : v.become(get_v2_line(input_tracker_p2)))

        horizlineg3 = get_h2_line(input_tracker_p2).set_color(PURPLE)
        horizlineg3.add_updater(lambda h : h.become(get_h2_line(input_tracker_p2)))

        graph3dot = Dot().move_to(get_graph2_point(input_tracker_p2)).scale(0.9)
        graph3dot.add_updater(lambda g : g.move_to(get_graph2_point(input_tracker_p2)))

        graph4dot = Dot().move_to(get_dot_on_axes2(k)).scale(0.9)
        graph4dot.add_updater(lambda g : g.move_to(get_dot_on_axes2(k)))

        graph5dot = Dot().move_to(get_dot_on_axes3(p)).scale(0.9)
        graph5dot.add_updater(lambda g : g.move_to(get_dot_on_axes3(p)))

        graph6dot = Dot().move_to(get_dot_on_axes4(q)).scale(0.9)
        graph6dot.add_updater(lambda g : g.move_to(get_dot_on_axes4(q)))

        slopetext2 = TexMobject("slope=").scale(0.8).set_color(PURPLE).next_to(plane2, UP+RIGHT, buff=1).shift(DOWN)

        slopevalue2 = DecimalNumber(0, num_decimal_places=2, include_sign=False).scale(0.8).set_color(PURPLE)
        slopevalue2.next_to(slopetext2, RIGHT, buff=0.1)
        slopevalue2.add_updater(lambda s : s.set_value(get_y_value(k)))

        self.play(ShowCreation(graph3))
        self.add(slopetext2, slopevalue2, vertlineg3, horizlineg3, graph3dot)
        self.play(input_tracker_p2.set_value, 4.5,
        k.set_value, 4.5, run_time=5, rate_func=linear)
        self.play(input_tracker_p2.set_value, -4.5,
        k.set_value, -4.5, run_time=5, rate_func=smooth)
        self.wait()
        self.add(g4slopes, graph4dot)
        self.play(input_tracker_p2.set_value, 4.5, k.set_value, 4.5,
        ShowCreation(graph4), run_time=10, rate_func=smooth)
        self.play(graph4.set_stroke, {"opacity":0.3})
        self.remove(vertlineg3, horizlineg3, graph3dot, slopetext2, slopevalue2, g4slopes, graph4dot)
        self.play(input_tracker_p2.set_value, -4.5, k.set_value, -4.5, run_time=0.5)
        self.add(graph3dot, g4slopes, g5slopes, graph4dot, graph5dot, 
        vertlineg3, horizlineg3, slopetext2, slopevalue2)
        self.play(input_tracker_p2.set_value, 4.5, k.set_value, 4.5, p.set_value, 4.5,
        ShowCreation(graph5), run_time=10, rate_func=smooth)
        self.play(graph5.set_stroke, {"opacity":0.3})
        self.remove(vertlineg3, horizlineg3, graph3dot, slopetext2, slopevalue2, 
        graph4dot, graph5dot, g4slopes, g5slopes)
        self.play(input_tracker_p2.set_value, -4.5, k.set_value, -4.5, p.set_value, -4.5, run_time=0.5)
        self.add(graph3dot, g6slopes, graph6dot, vertlineg3, horizlineg3, 
        slopetext2, slopevalue2, g5slopes, g4slopes, graph4dot, graph5dot)
        self.play(input_tracker_p2.set_value, 4.5, k.set_value, 4.5, q.set_value, 4.5, p.set_value, 4.5,
        ShowCreation(graph6), run_time=10, rate_func=smooth)
        self.play(graph6.set_stroke, {"opacity":0.3})
        self.wait()
        self.play(input_tracker_p2.set_value, -2,
        k.set_value, -2, p.set_value, -2, q.set_value, -2, run_time=4, rate_func=smooth)
        self.play(input_tracker_p2.set_value, 3,
        k.set_value, 3, p.set_value, 3, q.set_value, 3, run_time=4, rate_func=smooth)
        self.wait()
        self.remove(*map(FadeOut, self.mobjects))











class Test(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : -1,
        "x_max" : 3,
        "x_min" : -1,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "graph_origin": DOWN+LEFT*3.5,
        "y_labeled_nums": range(-1,6,1),
        "x_labeled_nums": list(np.arange(-1, 4, 1)),
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "x_axis_width":4,
        "y_axis_height":4,
        }
    def construct(self):

        #DEFINING THE PLANE FOR F(x)
        plane_config = dict(
            axis_config = { 
                "include_tip": True, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -1, "x_max" : 4, "unit_size": 0.75
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -1, # not y_min
                "x_max" : 6,  # not y_max
                "unit_size": 0.75
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 1,
                "stroke_color" : GOLD,
            }  
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = RIGHT*3.5+DOWN
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        self.setup_axes(animate=True)

        graph1 = self.get_graph(lambda x : x**2+1,
        color = BLUE, x_min = 0, x_max = 2)

        x = ValueTracker(0)

        area = always_redraw(lambda : self.get_riemann_rectangles(
            graph1, 0, x.get_value(), dx=0.05, input_sample_type = "right",
            stroke_width = 0.5, stroke_color = BLACK, fill_opacity = 0.8,
            start_color = GREEN, end_color = YELLOW, width_scale_factor = 1.001))


        input_tracker_p1 = ValueTracker(0)
     
        graph2 = plane.get_graph(lambda x : (1/3)*x**3+x, color=(RED), x_min =0, x_max = 2)
        
        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph2.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return plane.coords_to_point(get_x_value(input_tracker),0)

        def get_y_point(input_tracker):
            return plane.coords_to_point(0,get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return plane.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4)

        def get_secant_line(input_tracker):
            x = interpolate(input_tracker.get_value(), 2, 0.01)
            dx = 0.01
            p1 = plane.input_to_graph_point(x, graph2)
            p2 = plane.input_to_graph_point(x + dx, graph2)
            secant_line = Line(p1, p2, color=GREEN)
            secant_line.scale_in_place(2 / secant_line.get_length())
            return secant_line




        v1_line = get_v_line(input_tracker_p1)
        v1_line.add_updater(lambda v : v.become(get_v_line(input_tracker_p1)))

        secant = get_secant_line(input_tracker_p1)
        secant.add_updater(lambda s : s.become(get_secant_line(input_tracker_p1)))

        dot = Dot()
        dot.move_to(get_graph_point(input_tracker_p1))
        dot.add_updater(lambda d : d.move_to(get_graph_point(input_tracker_p1)))

        self.play(Write(plane))
        self.play(ShowCreation(graph1), ShowCreation(graph2))
        self.add(v1_line, area, secant, dot)
       
        self.play(input_tracker_p1.set_value, 2, 
        x.set_value, 2,
        run_time=5, rate_func=smooth)
        self.wait()


      

