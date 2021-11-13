from manim import *
import numpy as np

class Graphing(GraphScene):
    def construct(self):

        self.x_min = -3
        self.x_max = 5
        self.y_min = -10
        self.y_max = 10
        self.x_axis_width = 6
        self.y_axis_height = 7
        self.axes_color = WHITE
        self.graph_origin = LEFT*3+DOWN
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3,6,1))
        self.y_labeled_nums = list(range(-10,11,2))

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : 0.1*(x-1)*(x-3)*(x+1), color = YELLOW, x_min = -3,
        x_max = 5)
        graph_lab = self.get_graph_label(graph, label = "f(x)=0.1(x-1)(x-3)(x+1)", direction = UP).scale(0.4)

        dot = Dot().move_to(self.coords_to_point(-1,0))

        deriv = self.get_derivative_graph(graph, color = BLUE)
        deriv_lab = MathTex("f'(x)").next_to(deriv, UR, buff=0.25)

        slope = self.get_secant_slope_group(-1, graph, dx=0.1)

        h_line = DashedLine(self.coords_to_point(-1, deriv.underlying_function(-1)),
        self.coords_to_point(0, deriv.underlying_function(-1)), stroke_width = 5, stroke_color = ORANGE)

        self.play(ShowCreation(VGroup(graph, graph_lab, deriv, deriv_lab, dot, slope)))
        self.wait()
        self.play(ShowCreation(h_line))
        self.wait()

class WingLec3(GraphScene):
    def construct(self):

        self.x_min = -5
        self.x_max = 5
        self.y_min = -5
        self.y_max = 10
        self.axes_color = WHITE
        self.graph_origin = DOWN*1.5
        self.x_labeled_nums = list(range(-5, 6, 5))
        self.y_labeled_nums = list(range(-5, 11, 5))
        self.y_axis_height = 5
        self.x_axis_width = 5

        self.setup_axes(animate = False)

        func = self.get_graph(lambda x : (1/3)*x**3 + (1/2)*x**2 - 2*x, x_min = -4, x_max = 3, color = RED)

        deriv = self.get_graph(lambda x : x**2 + x - 2, x_min = -4, x_max = 3, color = GREEN)

        slope = self.get_secant_slope_group(-3, func, dx = 0.1, secant_line_length = 4,
        secant_line_color = YELLOW)

        def get_vertical_line_group(x, graph):
            result = VGroup()

            line = Line(self.coords_to_point(x, graph.underlying_function(x)),
            self.coords_to_point(x,0), stroke_width = 7, stroke_color = ORANGE)

            coord = Dot().move_to(self.coords_to_point(x, graph.underlying_function(x)))

            tri = RegularPolygon(n=3).scale(0.1).next_to(line, DOWN, buff=0)

            var = MathTex("x").next_to(tri, DOWN, buff=0.1)

            result.add(line, coord, tri, var)

            return result

        def get_horizontal_line_group(x, graph):
            result = VGroup()

            line = DashedLine(self.coords_to_point(x, graph.underlying_function(x)),
            self.coords_to_point(0, graph.underlying_function(x)), stroke_width = 15, stroke_color = BLUE)

            dot = Dot().move_to(self.coords_to_point(x, graph.underlying_function(x)))

            tri = RegularPolygon(n=3).scale(0.1).rotate(PI/2).next_to(line, RIGHT, buff=0)

            text = Tex("slope").scale(0.7).next_to(tri, RIGHT, buff=0.2)

            result.add(line, dot, tri, text)
            return result

        v_line = get_vertical_line_group(x = -3, graph = func)

        h_line = get_horizontal_line_group(x = -3, graph = deriv)

        self.play(ShowCreation(func), ShowCreation(deriv), ShowCreation(slope))
        self.wait()
        self.play(ShowCreation(v_line))
        self.wait()
        self.play(ShowCreation(h_line))
        self.wait()

