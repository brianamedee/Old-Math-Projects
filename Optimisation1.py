from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

class FarmOpt(GraphScene):
        CONFIG = {
        "y_max" : 650,
        "y_min" : 0,
        "x_max" :50,
        "x_min" : 0,
        "y_tick_frequency" : 50, 
        "x_tick_frequency" : 5, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,651,50),
        "x_labeled_nums": list(np.arange(0, 51, 5)),
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "graph_origin": 3*DOWN, 
        "x_axis_label": "$w$",
        "y_axis_label": "$A(w)$",
        "x_axis_width":5,
        "y_axis_height":6.5,
     }

        def construct(self):

            #ADDING GRAPH TO NUMBER PLANE#

            self.setup_axes(animate=True)

            graph = self.get_graph(lambda x: 50*x-x**2,
                                x_min = 0,
                                x_max = 50,
                                color = RED)
        
            graph_lab = self.get_graph_label(graph,
                                         r"A(w)=50w-w^2")
            graph_lab.scale(0.5).shift(UP*5+RIGHT*0.5)

        #ADDING TANGENT TO NUMBER PLANE#

            input_tracker_p1 = ValueTracker(0)
            input_tracker_p2 = ValueTracker(50)

            def get_x_value(input_tracker):
                return input_tracker.get_value()

            def get_y_value(input_tracker):
                return graph.underlying_function(get_x_value(input_tracker))

            def get_graph_point(input_tracker):
                return self.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

            def get_x_point(input_tracker):
                return self.coords_to_point(get_x_value(input_tracker),0)

            def get_y_point(input_tracker):
                return self.coords_to_point(0,get_y_value(input_tracker))

            def get_v_line(input_tracker):
                return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

            def get_h_line(input_tracker):
                return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4)



        #Adding Tangent1 Updater

            tandot1 = Dot()
            def update_tandot1(mob, alpha):
                td1 = mob
                td1.move_to(get_graph_point(input_tracker_p1)).alpha=0.1

            tangent_group = always_redraw(lambda:

                                      self.get_secant_slope_group(input_tracker_p1.get_value(),
                                                                  graph, 0.01,
                                                                  secant_line_color=YELLOW,
                                                                  secant_line_length=2)
                                      )

            #ADDING VERT AND HORIZ LINES#

            v_line_p1 = get_v_line(input_tracker_p1)
            def update_v_line_p1(mob, alpha):
                v1 = mob
                v1.become(get_v_line(input_tracker_p1)).alpha=0.1

            h_line_p1 = get_h_line(input_tracker_p1)
            def update_h_line_p1(mob, alpha):
                h1 = mob
                h1.become(get_h_line(input_tracker_p1)).alpha=0.1
                                         


        #ADDING RECTANGLES AS A VGROUP CALLED RECTANGLES#

            rect1 = Polygon((-4, 3.33,0), (-4, -3.33,0), (-4,-3.33,0), (-4,3.33,0))

            rect2 = Polygon((-4.33,3,0), (-4.33,-3,0), (-3.67,-3,0), (-3.67,3,0))

            rect3 = Polygon((-4.67,2.66,0), (-4.67,-2.67,0), (-3.33,-2.67,0), (-3.33,2.67,0))

            rect4 = Polygon((-5,2.33,0), (-5,-2.33,0), (-3,-2.33,0), (-3,2.33,0))

            rect5 = Polygon((-5.33,2,0), (-5.33,-2,0), (-2.67, -2, 0), (-2.67,2,0))

            rect6 = Polygon((-5.67,1.67,0),(-5.67,-1.67,0),(-2.33,-1.67,0),(-2.33,1.67,0))

            rect7 = Polygon((-6,1.33,0),(-6,-1.33,0),(-2,-1.33,0),(-2,1.33,0))

            rect8 = Polygon((-6.33,1,0),(-6.33,-1,0),(-1.67,-1,0),(-1.67,1,0))

            rect9 = Polygon((-6.67,0.67,0),(-6.67,-0.67,0),(-1.33,-0.67,0),(-1.33,0.67,0))

            rect10 = Polygon((-7,0.33,0),(-7,-0.33,0),(-1,-0.33,0),(-1,0.33,0))

            rect11 = Polygon((-7.33,0,0), (-7.33,0,0),(-0.67,0,0),(-0.67,0,0))


            rectangles = VGroup(
                rect1, rect2, rect3, rect4, rect5, rect6,
                rect7, rect8, rect9, rect10, rect11)
            rectangles.set_fill(GREEN,opacity=0.7).set_stroke(width=4)       

        #ADDING AREA VALUE TRACKER#

            area = TextMobject("Area:")
            area.scale(0.6).next_to(rect1)
            area.add_updater(lambda a : a.next_to(rect1, 0.5*UP))
            

            areanumber = DecimalNumber(
                0, num_decimal_places=2,
                include_sign=False,
                )
            areanumber.scale(0.6)
            areanumber.next_to(area, 0.5*UP)
            areanumber.set_color(GREEN)
            areanumber.add_updater(lambda g : g.next_to(area, 0.5*RIGHT))
            areanumber.add_updater(lambda g : g.set_value(
                get_y_value(input_tracker_p1))
                          )

            #ADDING ELEMENTS TO RECTANGLE#

            width = TextMobject("Width:")
            width.scale(0.6).next_to(rect1, DOWN*0.5)
            width.add_updater(lambda w : w.next_to(rect1, DOWN*0.5))

            widthnumber = DecimalNumber(
                0, num_decimal_places=2,
                include_sign = False,
                )
            widthnumber.scale(0.6).next_to(width, 0.5*RIGHT)
            widthnumber.add_updater(lambda w : w.next_to(width, 0.5*RIGHT))
            widthnumber.add_updater(lambda w : w.set_value(
                get_x_value(input_tracker_p1))
                                     )

            length = TextMobject("Length:")
            length.scale(0.7).next_to(rect1, RIGHT*0.5)
            length.rotate(PI/2)
            length.add_updater(lambda l : l.next_to(rect1, RIGHT*0.5))

            lengthnumber = DecimalNumber(
                0, num_decimal_places=2,
                include_sign=False,
                )
            lengthnumber.scale(0.7).next_to(length, 0.5*UP)
            lengthnumber.rotate(PI/2)
            lengthnumber.add_updater(lambda l : l.next_to(length, 0.5*UP))
            lengthnumber.add_updater(lambda l : l.set_value(
                50-get_x_value(input_tracker_p1))
                                     )

            

            rules = TextMobject("Find MAX area if you have 100m of fence.")
            rules.scale(0.6).shift(UP*3.8+LEFT*3.7)
            rules.add_background_rectangle()

        #PLAYING THE ANIMATION#

            self.play(Write(rules))

            self.play(DrawBorderThenFill(rect1), ShowCreation(graph),
                      Write(graph_lab), run_time=3)
        
            self.add(width, area, areanumber, tandot1, tangent_group,
                     v_line_p1, h_line_p1, widthnumber,
                     length, lengthnumber)

            self.play(Indicate(width))
        
            self.play(input_tracker_p1.set_value, 5,
                  UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                  Transform(rect1,rect2),
                  run_time=2, rate_func=linear)
        
            self.play(input_tracker_p1.set_value, 10,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect3),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 15,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect4),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 20,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect5),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 25,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect6),
                      run_time=2, rate_func=linear)
            
            self.wait(2)
            
            self.play(input_tracker_p1.set_value, 30,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      FadeOut(length), FadeOut(lengthnumber),
                      Transform(rect1,rect7),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 35,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect8),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 40,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect9),
                      run_time=2, rate_func=linear)
            
            self.play(input_tracker_p1.set_value, 45,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect10),
                      run_time=2, rate_func=linear)

            self.play(input_tracker_p1.set_value, 50,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      Transform(rect1,rect11),
                      FadeOut(rules), FadeOut(width), FadeOut(widthnumber),
                      run_time=2, rate_func=linear)
            self.wait()


def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class TrapOpt(GraphScene):
    CONFIG = {
        "y_max" : 6,
        "y_min" : 0,
        "x_max" : PI/2,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : PI/6,
        "graph_origin" : 2.5*DOWN+RIGHT,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
        "x_axis_width":5,
        "y_axis_height":5,
        }
    

    def construct(self):
        self.setup_axes()

    def setup_axes(self):
            GraphScene.setup_axes(self)
            # width of edges
            self.x_axis.set_stroke(width=2)
            self.y_axis.set_stroke(width=2)
            # color of edges
            self.x_axis.set_color(WHITE)
            self.y_axis.set_color(WHITE)
            # Add x,y labels
            func = TexMobject("A(\\theta)")
            var = TexMobject("\\theta")
            func.set_color(WHITE)
            var.set_color(WHITE)
            func.next_to(self.y_axis,0.7*UP)
            var.next_to(self.x_axis,0.7*RIGHT+0.7*UP)
            # Y labels
            self.y_axis.label_direction = LEFT*1.5
            self.y_axis.add_numbers(*[0, 1, 2, 3, 4, 5, 6])
            #Parametters of x labels
            init_val_x = 0
            step_x = PI/6
            end_val_x = PI/2
            # List of the positions of x labels
            values_decimal_x=Range(init_val_x,end_val_x,step_x)
            # List of tex objects
            list_x=TexMobject("0",
                              "\\frac{\\pi}{6}",
                              "\\frac{\\pi}{3}",
                              "\\frac{\\pi}{2}",
                              )
                            
            #List touples (position,label)
            values_x = [(i,j)
                for i,j in zip(values_decimal_x,list_x)
            ]
            self.x_axis_labels = VGroup()
            for x_val, x_tex in values_x:
                x_tex.scale(0.7)
                if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                    x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
                else: # In another case
                    x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
                self.x_axis_labels.add(x_tex)

            self.play(
                *[Write(objeto)
                for objeto in [
                        self.y_axis,
                        self.x_axis,
                        self.x_axis_labels,
                        func,var
                    ]
                ],
                run_time=3
            )


            

            graph = self.get_graph(lambda x: np.sin(x)*(4+4*np.cos(x)),
                                x_min = 0,
                                x_max = PI/2,
                                color = GREEN)
        
            graph_lab = TexMobject("A(\\theta)=\sin{(\\theta)}+(4+4\cos{(\\theta)})")
            graph_lab.scale(0.6).next_to(graph, UP*0.7).set_color(GREEN)

        #ADDING TANGENT TO NUMBER PLANE#

            input_tracker_p1 = ValueTracker(PI/2)
            input_tracker_p2 = ValueTracker(0.01)

            def get_x_value(input_tracker):
                return input_tracker.get_value()

            def get_y_value(input_tracker):
                return graph.underlying_function(get_x_value(input_tracker))

            def get_graph_point(input_tracker):
                return self.coords_to_point(get_x_value(input_tracker),get_y_value(input_tracker))

            def get_x_point(input_tracker):
                return self.coords_to_point(get_x_value(input_tracker),0)

            def get_y_point(input_tracker):
                return self.coords_to_point(0,get_y_value(input_tracker))

            def get_v_line(input_tracker):
                return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=4)

            def get_h_line(input_tracker):
                return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=4)

            #Adding Tangent1 Updater

            tandot1 = Dot()
            tandot1.move_to(get_graph_point(input_tracker_p1))
            def update_tandot1(mob, alpha):
                td1 = mob
                td1.move_to(get_graph_point(input_tracker_p1)).alpha=0.1

            tangent_group = always_redraw(lambda:

                                      self.get_secant_slope_group(input_tracker_p1.get_value(),
                                                                  graph, 0.01,
                                                                  secant_line_color=YELLOW,
                                                                  secant_line_length=2)
                                      )

            #ADDING VERT AND HORIZ LINES#

            v_line_p1 = get_v_line(input_tracker_p1)
            def update_v_line_p1(mob, alpha):
                v1 = mob
                v1.become(get_v_line(input_tracker_p1)).alpha=0.1

            h_line_p1 = get_h_line(input_tracker_p1)
            def update_h_line_p1(mob, alpha):
                h1 = mob
                h1.become(get_h_line(input_tracker_p1)).alpha=0.1
 

            #Defining the Lines

            theta = ValueTracker(PI/2.001)
            phi = ValueTracker(PI/2.001)

            groundline = Line((-6,-2,0),(-2,-2,0))
            groundline.set_color(WHITE).stroke_width=4

            base = Line((-5,-2,0),(-3,-2,0)).set_color(RED)
            base.stroke_width=6
            adjust1 = Line((-5,-2,0),(-5,0,0)).set_color(RED)
            adjust1.stroke_width=6
            adjust2 = Line((-3,-2,0),(-3,0,0)).set_color(RED)
            adjust2.stroke_width=6

            adjust1.rotate(theta.get_value(),about_point=(-5,-2,0))

            adjust1.add_updater(
                lambda a : a.set_angle(
                    theta.get_value()
                    )
                )

            adjust2.rotate(theta.get_value(),about_point=(-3,-2,0))

            adjust2.add_updater(
                lambda a : a.set_angle(
                    phi.get_value()
                    )
                )

            top = Line()
            top.put_start_and_end_on(adjust1.get_end(),
                                     adjust2.get_end()
                                     )
            top.set_color(GREY)
            top.stroke_width=6

            top.add_updater(
                lambda t : t.put_start_and_end_on(
                    adjust1.get_end(),
                    adjust2.get_end()
                    )
                )

            trap = Polygon(base.get_start(),
                                base.get_end(),
                                adjust2.get_end(), adjust1.get_end()
                                )
            
            trap.set_fill(ORANGE, opacity=0.4).stroke_color=RED
            
            trap.add_updater(lambda t : t.become(Polygon(
                base.get_start(), base.get_end(),
                adjust2.get_end(), adjust1.get_end()
                ).set_fill(ORANGE, opacity=0.4)
                                                 )
                             )
                                 
                                                
            
            arc = Arc(
                radius = 0.5,
                start_angle = groundline.get_angle(),
                angle = adjust2.get_angle(),
                arc_center = LEFT*3+DOWN*2,
                color = GREEN,
                )

            arc.add_updater(
                lambda a : a.become(
                    Arc(radius=0.5, start_angle=groundline.get_angle(),
                        angle = adjust2.get_angle(),
                        arc_center = LEFT*3+DOWN*2,
                        color = GREEN
                        ))
                )

            #ADDING THETA TEX & GRAPH TRACKERS

            theta1 = TexMobject("\\theta=").scale(0.7).set_color(GREEN)
            theta1.next_to(arc, UP*0.1+RIGHT*0.1)
            theta1.add_updater(lambda t : t.next_to(arc, UP*0.1+RIGHT*0.1))
            
            tritrack = RegularPolygon(n=3, start_angle=PI/2).set_fill(WHITE)
            tritrack.next_to(v_line_p1, DOWN, buff=0).scale(0.1).set_stroke(WHITE)
            tritrack.add_updater(lambda t : t.next_to(v_line_p1, DOWN, buff=0))
            
            theta2 = TexMobject("\\theta").scale(0.7).set_color(GREEN)
            theta2.next_to(tritrack, DOWN*0.4)
            theta2.add_updater(lambda t : t.next_to(tritrack, DOWN*0.2))

            theta1num = DecimalNumber(
                0, num_decimal_places=2,
                include_sign=False)
            theta1num.scale(0.4).set_color(GREEN).next_to(theta1, RIGHT*0.1)
            theta1num.add_updater(lambda t : t.next_to(theta1, RIGHT*0.1))
            theta1num.add_updater(lambda t : t.set_value(
                get_x_value(input_tracker_p1))
                                  )

            mes1 = TexMobject("2m").scale(0.6).set_color(BLUE)
            mes1.next_to(base,DOWN*0.4)
            mes2 = TexMobject("2m").scale(0.6).set_color(BLUE)
            mes2.next_to(adjust1, LEFT*0.2)
            mes2.add_updater(lambda m : m.next_to(adjust1, LEFT*0.2))
            mes3 = TexMobject("2m").scale(0.6).set_color(BLUE)
            mes3.next_to(adjust2, RIGHT*0.2)
            mes3.add_updater(lambda m : m.next_to(adjust2, RIGHT*0.2))

            areatext = TextMobject("Area=").scale(0.5).next_to(top, UP*0.4).set_color(ORANGE)
            areatext.add_updater(lambda a : a.next_to(top, UP*0.4))
            areanum = DecimalNumber(
                0, num_decimal_places = 2,
                include_sign=False)
            areanum.scale(0.5).set_color(ORANGE).next_to(areatext, RIGHT*0.1)
            areanum.add_updater(lambda a : a.next_to(areatext, RIGHT*0.1))
            areanum.add_updater(lambda a : a.set_value(
                get_y_value(input_tracker_p1)
                ))


            


            #PLAYING THE ANIMATION
                                   

            self.play(ShowCreation(graph), Write(graph_lab))
            self.add(tandot1, v_line_p1, h_line_p1, tritrack,
                     base, top, adjust1, adjust2, groundline, trap)
            
            self.play(DrawBorderThenFill(trap))
            
            self.play(ShowCreation(arc))
            self.play(Write(mes1),Write(mes2),Write(mes3))
            self.wait()
    
            
            self.add(theta2, theta1, theta1num, areatext, areanum)
            self.wait()
            self.play(theta.increment_value,PI/6,
                      phi.increment_value,-PI/6,
                      input_tracker_p1.set_value, PI/3,
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      run_time=5, rate_func=linear)
            self.add(tangent_group)
            self.wait(2)
            self.play(FadeOut(tangent_group))
            self.play(theta.increment_value, PI/3.001,
                      phi.increment_value,-PI/3.001,
                      input_tracker_p1.set_value, input_tracker_p2.get_value(),
                      UpdateFromAlphaFunc(tandot1, update_tandot1),
                      UpdateFromAlphaFunc(v_line_p1, update_v_line_p1),
                      UpdateFromAlphaFunc(h_line_p1, update_h_line_p1),
                      FadeOut(mes1),FadeOut(mes2),FadeOut(mes3),
                      run_time=5, rate_func=linear)
            self.wait()


class InitialFarm(Scene):
    def construct(self):

        rule = TextMobject("100m fence, maximum area?")
        rule.scale(1.2).shift(UP*3.2+LEFT*2)
        und = Underline(rule)

         #ADDING RECTANGLES AS A VGROUP CALLED RECTANGLES#

        rect1 = Polygon((-4, 3.33,0), (-4, -3.33,0), (-4,-3.33,0), (-4,3.33,0))

        rect2 = Polygon((-4.33,3,0), (-4.33,-3,0), (-3.67,-3,0), (-3.67,3,0))

        rect3 = Polygon((-4.67,2.66,0), (-4.67,-2.67,0), (-3.33,-2.67,0), (-3.33,2.67,0))

        rect4 = Polygon((-5,2.33,0), (-5,-2.33,0), (-3,-2.33,0), (-3,2.33,0))

        rect5 = Polygon((-5.33,2,0), (-5.33,-2,0), (-2.67, -2, 0), (-2.67,2,0))

        rect6 = Polygon((-5.67,1.67,0),(-5.67,-1.67,0),(-2.33,-1.67,0),(-2.33,1.67,0))

        rect7 = Polygon((-6,1.33,0),(-6,-1.33,0),(-2,-1.33,0),(-2,1.33,0))

        rect8 = Polygon((-6.33,1,0),(-6.33,-1,0),(-1.67,-1,0),(-1.67,1,0))

        rect9 = Polygon((-6.67,0.67,0),(-6.67,-0.67,0),(-1.33,-0.67,0),(-1.33,0.67,0))

        rect10 = Polygon((-7,0.33,0),(-7,-0.33,0),(-1,-0.33,0),(-1,0.33,0))

        rect11 = Polygon((-7.33,0,0), (-7.33,0,0),(-0.67,0,0),(-0.67,0,0))


        rectangles = VGroup(
                rect1, rect2, rect3, rect4, rect5, rect6,
                rect7, rect8, rect9, rect10, rect11)
        rectangles.set_fill(GREEN,opacity=0.7).set_stroke(width=4)


            #ADDING AREA VALUE TRACKER#

        area = TextMobject("Area:??")
        area.scale(0.6).next_to(rect1)
        area.add_updater(lambda a : a.next_to(rect1, 0.5*UP))
    

            #ADDING ELEMENTS TO RECTANGLE#

        width = TextMobject("Width:??")
        width.scale(0.6).next_to(rect1, DOWN*0.5)
        width.add_updater(lambda w : w.next_to(rect1, DOWN*0.5))


        length = TextMobject("Length:??")
        length.scale(0.7).next_to(rect1, RIGHT*0.5)
        length.rotate(PI/2)
        length.add_updater(lambda l : l.next_to(rect1, RIGHT*0.5))


            #PLAYING THE ANIMATION#

        self.play(Write(rule), ShowCreation(und), run_time=2)
        self.play(rule.shift, DOWN*1.5+RIGHT*3.5, rule.scale,0.7,
                  und.shift, DOWN*1.5+RIGHT*3.5, und.scale, 0.7)

        self.play(DrawBorderThenFill(rect1),run_time=3)
        
        
        self.add(width, area, length)
        
        
        self.play(Transform(rect1,rect2),
                  run_time=2, rate_func=linear)
        
        self.play(Transform(rect1,rect3),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect4),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect5),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect6),
                      run_time=2, rate_func=linear)
                     
        self.play(Transform(rect1,rect7),
                  FadeOut(rule), FadeOut(und),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect8),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect9),
                      run_time=2, rate_func=linear)
            
        self.play(Transform(rect1,rect10),
                      run_time=2, rate_func=linear)

        self.play(Transform(rect1,rect11),
                      run_time=2, rate_func=linear)
        self.wait()


class InitialTrap(Scene):
    
    def construct(self):

        rule = TextMobject("What angle to maximise the area?")
        rule.scale(1.2).shift(UP*3.2+LEFT*2)
        und = Underline(rule)

        #Defining the Lines

        theta = ValueTracker(PI/2.001)
        phi = ValueTracker(PI/2.001)

        groundline = Line((-6,-2,0),(-2,-2,0))
        groundline.set_color(WHITE).stroke_width=4

        base = Line((-5,-2,0),(-3,-2,0)).set_color(RED)
        base.stroke_width=6
        adjust1 = Line((-5,-2,0),(-5,0,0)).set_color(RED)
        adjust1.stroke_width=6
        adjust2 = Line((-3,-2,0),(-3,0,0)).set_color(RED)
        adjust2.stroke_width=6

        adjust1.rotate(theta.get_value(),about_point=(-5,-2,0))

        adjust1.add_updater(
                lambda a : a.set_angle(
                    theta.get_value()
                    )
                )

        adjust2.rotate(theta.get_value(),about_point=(-3,-2,0))

        adjust2.add_updater(
                lambda a : a.set_angle(
                    phi.get_value()
                    )
                )

        top = Line()
        top.put_start_and_end_on(adjust1.get_end(),
                                     adjust2.get_end()
                                     )
        top.set_color(GREY)
        top.stroke_width=6

        top.add_updater(
                lambda t : t.put_start_and_end_on(
                    adjust1.get_end(),
                    adjust2.get_end()
                    )
                )

        trap = Polygon(base.get_start(),
                                base.get_end(),
                                adjust2.get_end(), adjust1.get_end()
                                )
            
        trap.set_fill(ORANGE, opacity=0.4).stroke_color=RED
            
        trap.add_updater(lambda t : t.become(Polygon(
                base.get_start(), base.get_end(),
                adjust2.get_end(), adjust1.get_end()
                ).set_fill(ORANGE, opacity=0.4)
                                                 )
                             )
                                 
                                                
            
        arc = Arc(
                radius = 0.5,
                start_angle = groundline.get_angle(),
                angle = adjust2.get_angle(),
                arc_center = LEFT*3+DOWN*2,
                color = GREEN,
                )

        arc.add_updater(
                lambda a : a.become(
                    Arc(radius=0.5, start_angle=groundline.get_angle(),
                        angle = adjust2.get_angle(),
                        arc_center = LEFT*3+DOWN*2,
                        color = GREEN
                        ))
                )

            #ADDING THETA TEX & GRAPH TRACKERS

        theta1 = TexMobject("\\theta=??").scale(0.7).set_color(GREEN)
        theta1.next_to(arc, UP*0.1+RIGHT*0.1)
        theta1.add_updater(lambda t : t.next_to(arc, UP*0.1+RIGHT*0.1))

        mes1 = TexMobject("2m").scale(0.6).set_color(BLUE)
        mes1.next_to(base,DOWN*0.4)
        mes2 = TexMobject("2m").scale(0.6).set_color(BLUE)
        mes2.next_to(adjust1, LEFT*0.2)
        mes2.add_updater(lambda m : m.next_to(adjust1, LEFT*0.2))
        mes3 = TexMobject("2m").scale(0.6).set_color(BLUE)
        mes3.next_to(adjust2, RIGHT*0.2)
        mes3.add_updater(lambda m : m.next_to(adjust2, RIGHT*0.2))

        areatext = TextMobject("Area=??").scale(0.5).next_to(top, UP*0.4).set_color(ORANGE)
        areatext.add_updater(lambda a : a.next_to(top, UP*0.4))


            


            #PLAYING THE ANIMATION
                                   
        self.add(base, top, adjust1, adjust2, groundline)
            
        self.play(DrawBorderThenFill(trap))
            
        self.play(ShowCreation(arc))
        self.play(Write(mes1),Write(mes2),Write(mes3))
        self.wait()

        self.add(theta1, areatext)

        self.play(Write(rule), ShowCreation(und), run_time=2)
        self.wait()
        self.play(rule.shift, DOWN*3.5+RIGHT*3.7, rule.scale,0.6,
                  und.shift, DOWN*3.5+RIGHT*3.7, und.scale, 0.6)    
            
        
        self.wait()
        self.play(theta.increment_value,PI/6,
                      phi.increment_value,-PI/6,
                      run_time=5, rate_func=linear)
        self.play(theta.increment_value, PI/3.001,
                      phi.increment_value,-PI/3.001,
                  FadeOut(rule), FadeOut(und),
                      run_time=7.5, rate_func=linear)
        self.wait()



class Misconception(Scene):
    
    def construct(self):

        #Defining the Lines

        theta = ValueTracker(PI/2.001)
        phi = ValueTracker(PI/2.001)

        groundline = Line((-6,-2,0),(-2,-2,0))
        groundline.set_color(WHITE).stroke_width=4

        base = Line((-5,-2,0),(-3,-2,0)).set_color(RED)
        base.stroke_width=6
        adjust1 = Line((-5,-2,0),(-5,0,0)).set_color(RED)
        adjust1.stroke_width=6
        adjust2 = Line((-3,-2,0),(-3,0,0)).set_color(RED)
        adjust2.stroke_width=6

        adjust1.rotate(theta.get_value(),about_point=(-5,-2,0))

        adjust1.add_updater(
                lambda a : a.set_angle(
                    theta.get_value()
                    )
                )

        adjust2.rotate(theta.get_value(),about_point=(-3,-2,0))

        adjust2.add_updater(
                lambda a : a.set_angle(
                    phi.get_value()
                    )
                )

        top = Line()
        top.put_start_and_end_on(adjust1.get_end(),
                                     adjust2.get_end()
                                     )
        top.set_color(GREY)
        top.stroke_width=6

        top.add_updater(
                lambda t : t.put_start_and_end_on(
                    adjust1.get_end(),
                    adjust2.get_end()
                    )
                )

        trap = Polygon(base.get_start(),
                                base.get_end(),
                                adjust2.get_end(), adjust1.get_end()
                                )
            
        trap.set_fill(ORANGE, opacity=0.4).stroke_color=RED
            
        trap.add_updater(lambda t : t.become(Polygon(
                base.get_start(), base.get_end(),
                adjust2.get_end(), adjust1.get_end()
                ).set_fill(ORANGE, opacity=0.4)
                                                 )
                             )
                                 
                                                
            
        arc = Arc(
                radius = 0.5,
                start_angle = groundline.get_angle(),
                angle = adjust2.get_angle(),
                arc_center = LEFT*3+DOWN*2,
                color = GREEN,
                )

        arc.add_updater(
                lambda a : a.become(
                    Arc(radius=0.5, start_angle=groundline.get_angle(),
                        angle = adjust2.get_angle(),
                        arc_center = LEFT*3+DOWN*2,
                        color = GREEN
                        ))
                )


            #ADDING THETA TEX & GRAPH TRACKERS

        theta1 = TexMobject("\\theta=??").scale(0.7).set_color(GREEN)
        theta1.next_to(arc, UP*0.1+RIGHT*0.1)
        theta1.add_updater(lambda t : t.next_to(arc, UP*0.1+RIGHT*0.1))

        symtheta = TexMobject("\\theta").scale(0.7).set_color(GREEN)
        symtheta.next_to(trap, LEFT).shift(DOWN*0.8+LEFT*0.6)




            


            #PLAYING THE ANIMATION
                                   
        self.add(base, top, adjust1, adjust2, groundline)
            
        self.play(DrawBorderThenFill(trap))
            
        self.play(ShowCreation(arc))
        self.wait()

        self.add(theta1)
        
        self.wait()
        self.play(theta.increment_value,PI/2.5,
                      phi.increment_value,-PI/12,
                      run_time=5, rate_func=linear)
        self.play(Transform(theta1.copy(), symtheta))
        self.add(symtheta)

        self.wait()

        

        

        
            

            
            
            
                


    
        
        

        

    

        


            


        

        
