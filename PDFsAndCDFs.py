from manimlib.imports import *
import numpy as np
import random
import scipy.stats as scipy_stats

class Transition_Discrete_to_Cont_PDF(GraphScene):
    CONFIG = {
        "y_max" : 0.3,
        "y_min" : 0,
        "x_max" : 20,
        "x_min" : 0,
        "y_tick_frequency" : 0.05, 
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        "graph_origin": DOWN*3+LEFT*5.5,
        "y_labeled_nums": None,
        "x_labeled_nums": list(np.arange(0, 21, 1)),
        "x_axis_label": "",
        "y_axis_label": "",
        "x_axis_width":10,
        "y_axis_height":5,
        "x_label_decimal":0,
        "y_label_decimal":2
        }
    def construct(self):

        ##ADD IN SOME CONTEXT? eg. Consider the data containing weight/height of 'something'
        ##and explain that larger intervals = lower accuracy of representing the true weight/height
        ##leads in to saying area is probability, rather than height to avoid paradox

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : (1 / (2*(2*PI)**0.5))*np.exp((-0.5)*((x-12)/2)**2),
        x_min = 0, x_max = 20, color=PURPLE_B)  ##FUNCTION OF THE BELL CURVE##


        kwargs = {"x_min": 0, "x_max": 20, "fill_opacity":0.8, 
        "stroke_width":1, "stroke_color":BLACK}

        self.graph = graph
        iterations = 9
        self.rect_list = self.get_riemann_rectangles_list(graph, iterations, max_dx = 2, 
        start_color = BLUE, end_color = GREEN, **kwargs)

        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x : 0), dx = 2, start_color = invert_color(GREEN), input_sample_type = "center",
            end_color = invert_color(YELLOW), **kwargs
            )

        rects = self.rect_list[0] # Define the size of rectangles (bigger number = smaller rectangles)
        self.transform_between_riemann_rects(
            flat_rects,rects,
            replace_mobject_with_target_in_scene = True, run_time = 2.5
            )


        for j in range(1,9):
            self.transform_between_riemann_rects(
                self.rect_list[j-1], self.rect_list[j], dx=2,
                replace_mobject_with_target_in_scene = True,
                run_time = 2.5
                )


        self.wait()

        self.play(ShowCreation(graph))
        self.wait()

class PDF_and_CDF(Scene):

    def construct(self):

        #DEFINING THE PLANE FOR THE PDF
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
                "x_min" : 0, "x_max" : 4, "unit_size": 1,
                "numbers_to_show": range(0, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UP, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 2,  # not y_max
                "unit_size": 1,
                "numbers_to_show": range(0, 3, 1),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GOLD,
            }  
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = LEFT*6+UP
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        graph = plane.get_graph(lambda x : 0.5*x-1, color = ORANGE, x_min = 2, x_max = 4)
        tri_func_low = plane.get_graph(lambda x : 0, color = ORANGE, x_min = 2, x_max = 4)
        tri_func_up = Line(plane.c2p(4,0), plane.c2p(4,1), stroke_width = 5, stroke_color = ORANGE)
        tri_func_diag = Line(plane.c2p(4,1), plane.c2p(2,0), stroke_width = 5, stroke_color = ORANGE)

        x = ValueTracker(2) #TRACKER FOR NUMBER PLANE of F(x)

        def get_pdf_dot(x):
            return Dot(plane.c2p(x.get_value(), graph.underlying_function(x.get_value()))).scale(0.6)

        def get_pdf_v_line(x):
            return DashedLine(
                plane.coords_to_point(x.get_value(),0), 
                plane.coords_to_point(x.get_value(), graph.underlying_function(x.get_value())))
        
        def get_pdf_h_line(x):
            return Line(
                plane.c2p(0, graph.underlying_function(x.get_value())),
                plane.c2p(x.get_value(), graph.underlying_function(x.get_value())),
                stroke_width=4, color=RED_C)

        def get_area_under_pdf(graph, x_min=None,
        x_max=None, dx=0.02, input_sample_type="center", stroke_width=0.1, stroke_color=BLACK,
        fill_opacity=1, start_color=BLUE_B, end_color=GREEN_C,
        width_scale_factor=1.001
        ):
            x_min = x_min if x_min is not None else self.x_min
            x_max = x_max if x_max is not None else self.x_max
            rectangles = VGroup()
            x_range = np.arange(x_min, x_max, dx)
            colors = color_gradient([start_color, end_color], len(x_range))
            for x, color in zip(x_range, colors):
                if input_sample_type == "center":
                    sample_type = x + dx*0.5
                else:
                    raise Exception("Invalid input sample type")
                graph_point = plane.input_to_graph_point(sample_type, graph)
                points = VGroup(*list(map(VectorizedPoint, [
                    plane.coords_to_point(x, 0),
                    plane.coords_to_point(x + width_scale_factor * dx, 0), graph_point
                ])))
                rect = Rectangle()
                rect.replace(points, stretch = True)
                rect.set_fill(colors, opacity=fill_opacity)
                rect.set_stroke(stroke_color, width=stroke_width)
                rectangles.add(rect)
            return rectangles

        ##DEFINING PLANE FOR THE CDF
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
                "x_min" : 0, "x_max" : 4, "unit_size": 1,
                "numbers_to_show": range(0, 5, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UP, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 2,  # not y_max
                "unit_size": 1,
                "numbers_to_show": range(0, 3, 1),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GOLD,
            }  
        )
        plane2 = NumberPlane(**plane2_config)

        # shift origin to desired point
        new_origin2 = RIGHT+UP
        plane2.shift(new_origin2)

        # rotate y labels
        for label in plane2.y_axis.numbers:
            label.rotate(-PI/2)

        graph2 = plane2.get_graph(lambda x : 0.25 * x ** 2 - x + 1, color = ORANGE, x_min = 2, x_max = 4)
        lower_graph2 = plane2.get_graph(lambda x : 0, color = ORANGE, x_min = 0, x_max = 2)
        upper_graph2 = plane2.get_graph(lambda x : 1, color = ORANGE, x_min = 4, x_max = 4.2)

        c = ValueTracker(2)

        def get_cdf_dot(c):
            return Dot(plane2.c2p(c.get_value(), graph2.underlying_function(c.get_value()))).scale(0.6)

        def get_cdf_v_line(c):
            return DashedLine(
                plane2.coords_to_point(c.get_value(),0), 
                plane2.coords_to_point(c.get_value(), graph2.underlying_function(c.get_value())),
                stroke_width=4, color=WHITE)
        
        def get_cdf_h_line(c):
            return DashedLine(
                plane2.c2p(0, graph2.underlying_function(c.get_value())),
                plane2.c2p(c.get_value(), graph2.underlying_function(c.get_value())),
                stroke_width=4, color=WHITE)

        def get_cdf_secant_line(c):
            x = interpolate(c.get_value(), 4, 0.01)
            dx = 0.01
            p1 = plane2.input_to_graph_point(x, graph2)
            p2 = plane2.input_to_graph_point(x + dx, graph2)
            secant_line = Line(p1, p2, color=PURPLE_A)
            secant_line.scale_in_place(1.5 / secant_line.get_length())
            return secant_line


        ##DEFINING THE TEXT MOBJECTS FOR THE SCENE##

        pdf_title = TextMobject("PDF").scale(0.8).next_to(plane, UP, buff=0.2)
        pdf_und = Underline(pdf_title, stroke_width=0.5, buff=0.1)

        cdf_title = TextMobject("CDF").scale(0.8).next_to(plane2, UP, buff=0.2)
        cdf_und = Underline(cdf_title, stroke_width=0.5, buff=0.1)

        solve_for_cdf_1 = TexMobject("CDF = \\int_{2}^{x}\\frac{x}{2}-1\\quad dx").set_height(0.7).to_edge(LEFT)
        solve_for_cdf_2 = TexMobject("CDF = { \\left[ \\frac { { x }^{ 4 } }{ 2 } -x \\right]  }_{ 2 }^{ x }"
        ).set_height(0.7).next_to(solve_for_cdf_1, DOWN, buff=0.3, aligned_edge=LEFT)
        solve_for_cdf_3 = TexMobject("CDF = (\\frac{{x}^{2}}{4}-x) - (1-2)"
        ).set_height(0.7).next_to(solve_for_cdf_2, DOWN, buff=0.3, aligned_edge=LEFT)
        solve_for_cdf_4 = TexMobject("CDF = \\frac{{x}^{2}}{4}-x+1"
        ).set_height(0.7).next_to(solve_for_cdf_3, DOWN, buff=0.3, aligned_edge = LEFT)

        explain1 = TextMobject("y values on F(x) correspond").scale(0.6).next_to(plane2, DOWN, buff=1, aligned_edge=LEFT)
        explain2 = TextMobject("to the area under f(x).").scale(0.6).next_to(explain1, DOWN, buff=0.3, aligned_edge=LEFT)
        explain3 = TextMobject("Fundamental Theorem of Calculus").scale(0.8).next_to(explain2, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT*0.5)

        arrow = Line(plane.get_right(), plane2.get_left(), buff=0.5).add_tip()
        how = TextMobject("How?").set_height(0.3).next_to(arrow, UP)

        graph_lab = TexMobject("f(x)=\\frac{x}{2}-1").set_height(0.5).next_to(graph, UP)
        graph2_lab = TexMobject("F(x)=\\frac{{x}^{2}}{4}-x+1").set_height(0.5).next_to(graph2, UP)

        ##ADDING THE ELEMENTS TO THE PDF AND CDF##
        pdf_dot = get_pdf_dot(x)
        pdf_dot.add_updater(lambda d : d.move_to(get_pdf_dot(x)))

        pdf_h_line = get_pdf_v_line(x)
        pdf_h_line.add_updater(lambda v : v.become(get_pdf_h_line(x)))

        cdf_dot = get_cdf_dot(c)
        cdf_dot.add_updater(lambda d : d.move_to(get_cdf_dot(c)))

        pdf_area = always_redraw(lambda : get_area_under_pdf(graph, x_min = 2, x_max = x.get_value()))

        cdf_secant = get_cdf_secant_line(c)
        cdf_secant.add_updater(lambda s : s.become(get_cdf_secant_line(c)))

        cdf_h_line = get_cdf_h_line(c)
        cdf_h_line.add_updater(lambda h : h.become(get_cdf_h_line(c)))

        prob_dens_func = TextMobject("Probability Density Function")
        cum_dens_func = TextMobject("Cumulative Density Function")

        self.play(Write(plane))
        self.play(FadeIn(prob_dens_func))
        self.play(Transform(prob_dens_func, pdf_title))
        self.play(ShowCreation(pdf_und))
        self.play(ShowCreation(graph), run_time=2)
        self.wait()
        self.play(Write(graph_lab))
        self.wait()
        self.add(pdf_area, pdf_dot)
        self.play(x.set_value, 4, run_time=5, rate_func = smooth)
        self.play(ShowCreation(VGroup(tri_func_low, tri_func_up, tri_func_diag)), run_time=2)
        self.wait()
        self.play(FadeOut(VGroup(tri_func_low, tri_func_up, tri_func_diag)))
        self.wait()
        self.play(x.set_value, 2, run_time=2)
        self.wait()
        self.remove(pdf_dot)

        self.play(LaggedStart(Write(plane2), ShowCreation(graph2)),
        run_time=2, lag_ratio = 0.75)
        self.play(FadeIn(cum_dens_func))
        self.play(Transform(cum_dens_func, cdf_title))
        self.play(ShowCreation(cdf_und))
        self.wait()
        self.add(cdf_h_line, cdf_dot, pdf_dot)
        self.play(c.set_value, 3.2, x.set_value, 3.2, run_time=6)
        self.wait()
        self.play(c.set_value, 2, x.set_value, 2, run_time=2)
        self.remove(cdf_h_line, cdf_dot, pdf_dot)
        self.wait()
        self.play(ShowCreation(arrow))
        self.play(Write(how))
        self.wait(2)
        self.play(ShowCreation(explain3))
        self.play(Indicate(explain3))
        self.wait()
        self.play(FadeOut(explain3))

        self.play(Write(solve_for_cdf_1), run_time=2)
        self.wait()
        self.play(Write(solve_for_cdf_2), run_time=2)
        self.wait(2)
        self.play(Write(solve_for_cdf_3), run_time=2)
        self.wait(2)
        self.play(Write(solve_for_cdf_4), run_time=2)
        self.wait()

        self.play(Transform(solve_for_cdf_4.copy(), graph2_lab),
        FadeOut(VGroup(arrow, how)), run_time=3)
        self.wait()

        self.play(ShowCreation(VGroup(lower_graph2, upper_graph2)))

        self.add(cdf_h_line, pdf_dot, cdf_dot)
        self.play(c.set_value, 4, x.set_value, 4, run_time=10)
        self.wait()

        self.play(Write(explain1))
        self.play(Write(explain2))

        self.play(c.set_value, 2, x.set_value, 2, run_time=3)
        self.wait()

        self.play(Write(explain3))
        self.wait()

        self.play(Indicate(explain3), run_time=2)
    
        self.play(x.set_value, 4, c.set_value, 4, run_time=10)
        self.wait()





        







        

        


        

class SlopeTesting(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": -5,
        "y_max": 10,
        "y_axis_height": 5,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": WHITE,
        "graph_origin": LEFT*4
    }
    

    def construct(self):

        self.setup_axes(animate=True)

        graph1 = self.get_graph(lambda x : x**2, color = PURPLE_A, x_min = -3, x_max=3)

        k = ValueTracker(-3)
        p = ValueTracker(1)

        slopes = always_redraw(lambda : 
        self.get_secant_slope_group(k.get_value(), graph1, dx=p.get_value(), secant_line_color=BLUE_B, secant_line_length=5))

        self.play(ShowCreation(graph1))
        self.add(slopes)
        self.wait()

        self.play(k.set_value, -1, run_time = 3)
        self.wait()
        self.play(p.set_value, 0.001, run_time=10)
        self.wait()

        self.play(k.set_value, 3, run_time=4)
        self.wait()



