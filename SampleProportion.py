from manim import *
import random
import scipy.stats as scipy_stats
import numpy as np

HOME = "C:\manim\Manim_7_July\Projects\\assets\Images"
HOME2 = "C:\manim\Manim_7_July\Projects\\assets\SVG_Images"

def get_data_1(self):
        w = 0.2
        h = 0.2
        t_row1 = VGroup(*[SVGMobject(f"{HOME2}\\green_tick.svg").set_height(h).set_width(w).set_color(GREEN_C)
        for i in range(10)]).arrange(RIGHT, buff=0.2).to_edge(UL, buff=0.25)
        t_row2 = VGroup(*[SVGMobject(f"{HOME2}\\green_tick.svg").set_height(h).set_width(w).set_color(GREEN_C)
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(t_row1, DOWN, buff=0.25)
        f_row1 = VGroup(*[SVGMobject(f"{HOME2}\\cross.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(t_row2, DOWN, buff=0.25)
        f_row2 = VGroup(*[SVGMobject(f"{HOME2}\\cross.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(f_row1, DOWN, buff=0.25)
        f_row3 = VGroup(*[SVGMobject(f"{HOME2}\\cross.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(f_row2, DOWN, buff=0.25)

        result = VGroup(*t_row1, *t_row2, *f_row1, *f_row2, *f_row3)

        return result

def get_data_2(self):
        w = 0.4
        h = 0.2
        t_row1 = VGroup(*[SVGMobject(f"{HOME2}\\person3.svg").set_height(h).set_width(w).set_color(GREEN_C)
        for i in range(10)]).arrange(RIGHT, buff=0.2).to_edge(UL, buff=0.25)
        t_row2 = VGroup(*[SVGMobject(f"{HOME2}\\person3.svg").set_height(h).set_width(w).set_color(GREEN_C)
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(t_row1, DOWN, buff=0.25)
        f_row1 = VGroup(*[SVGMobject(f"{HOME2}\\person3.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(t_row2, DOWN, buff=0.25)
        f_row2 = VGroup(*[SVGMobject(f"{HOME2}\\person3.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(f_row1, DOWN, buff=0.25)
        f_row3 = VGroup(*[SVGMobject(f"{HOME2}\\person3.svg").set_height(h).set_width(w).set_color(RED_B) 
        for i in range(10)]).arrange(RIGHT, buff=0.2).next_to(f_row2, DOWN, buff=0.25)

        result = VGroup(*t_row1, *t_row2, *f_row1, *f_row2, *f_row3)

        return result

class intro(Scene):
    def construct(self):

        data = get_data_2(self)

        thinking_monkey = SVGMobject(f"{HOME2}\\thinking_monkey.svg").set_height(2).to_edge(DR)
        think_bubble = SVGMobject(f"{HOME2}\\think_bubble.svg").set_height(4).next_to(thinking_monkey, UL, buff=0.2).flip()
        thought1 = Tex("Population size = 50").scale(0.6).move_to(think_bubble).shift(UP).set_color(BLACK)
        thought2 = Tex("20 / 50 go canteen").scale(0.6).next_to(thought1, DOWN, buff=0.2).set_color(BLACK)
        thought3 = Tex("Population proportion = 0.4").scale(0.6).next_to(thought2, DOWN, buff=0.2).set_color(BLACK)

        happy_monkey = SVGMobject(f"{HOME2}\\happy_monkey.svg").set_height(2).to_edge(DR)
        update_thought1 = Tex("Sample size = 10").scale(0.6).move_to(think_bubble).shift(UP).set_color(BLACK)
        update_thought2 = Tex("Sample Proportion = 0.3").scale(0.6).next_to(thought1, DOWN, buff=0.2).set_color(BLACK)
        update_thought3 = Tex("Sample proportions").scale(0.6).move_to(think_bubble).shift(UP).set_color(BLACK)
        update_thought4 = Tex("estimate the").scale(0.6).next_to(update_thought3, DOWN, buff=0.2).set_color(BLACK)
        update_thought5 = Tex("population proportion.").scale(0.6).next_to(update_thought4, DOWN, buff=0.2).set_color(BLACK)

        bored_monkey = SVGMobject(f"{HOME2}\\int_monkey.svg").set_height(2).to_edge(DL)
        think_bubble2 = SVGMobject(f"{HOME2}\\think_bubble.svg").set_height(3.5).next_to(bored_monkey, UR, buff=0.2)
        bored_thought = Tex("Why not just ask everyone?").scale(0.55).move_to(think_bubble2).set_color(BLACK)

        conversation_thought = Tex("This isn't always possible!").scale(0.55).move_to(think_bubble).set_color(BLACK)

        key_qs = VGroup()
        q1 = Tex("1. How accurate is a sample proportion?").scale(0.8).to_edge(UL)
        q2 = Tex("2. How might we improve the accuracy of the sample proportion?").scale(0.8).next_to(q1, DOWN, buff=0.2, aligned_edge=LEFT)
        key_qs.add(q1, q2)

        rects = VGroup()
        rect1 = SurroundingRectangle(data[6])
        rect2 = SurroundingRectangle(data[24])
        rect3 = SurroundingRectangle(data[47])
        rect4 = SurroundingRectangle(data[18])
        rect5 = SurroundingRectangle(data[22])
        rect6 = SurroundingRectangle(data[34])
        rect7 = SurroundingRectangle(data[39])
        rect8 = SurroundingRectangle(data[1])
        rect9 = SurroundingRectangle(data[41])
        rect10 = SurroundingRectangle(data[49])
        rects.add(rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10)

        self.play(Create(data))
        self.wait()
        self.play(DrawBorderThenFill(thinking_monkey), DrawBorderThenFill(think_bubble), run_time=2)
        self.play(Write(thought1), run_time=2)
        self.play(Write(thought2))
        self.play(Write(thought3))
        self.play(FadeOut(VGroup(thought1, thought2, thought3)), run_time=4)

        self.play(LaggedStart(Create(rects), Write(update_thought1), Write(update_thought2), run_time=5, lag_ratio=1))
        self.wait()
        self.play(LaggedStart(FadeOut(VGroup(update_thought1, update_thought2))), 
        Write(VGroup(update_thought3, update_thought4, update_thought5)), Transform(thinking_monkey, happy_monkey), run_time=4, lag_ratio=1)
        self.wait()

        self.play(FadeOut(VGroup(rects,data, update_thought3, update_thought4, update_thought5)))
        self.play(DrawBorderThenFill(bored_monkey), Create(think_bubble2), run_time=2)
        self.play(Write(bored_thought))
        self.wait()
        self.play(think_bubble.animate.set_height(3.5), Write(conversation_thought))
        self.wait()
        self.play(FadeOut(VGroup(think_bubble, think_bubble2, conversation_thought, bored_thought, bored_monkey, thinking_monkey)))
        self.play(Write(key_qs), run_time=3)

class SamplesOf5(Scene): 
    def construct(self):

        data = get_data_1(self)
        axes = Axes(
                x_range = [0, 1.2, 0.2], 
                y_range = [0, 2],
                x_length = 10,
                y_length = 4).to_edge(DL).shift(UP*0.2)

        x_axis_label = MathTex("\\hat{p}").scale(0.7).next_to(axes.x_axis, RIGHT, buff=0.1).shift(UP*0.2)

        x_axis_nums = VGroup()
        num1 = MathTex("\\frac{0}{5}").scale(0.6).next_to(axes.x_axis.n2p(0), DOWN, buff=0.1).shift(RIGHT*0.8)
        num2 = MathTex("\\frac{1}{5}").scale(0.6).next_to(axes.x_axis.n2p(0.2), DOWN, buff=0.1).shift(RIGHT*0.8)
        num3 = MathTex("\\frac{2}{5}").scale(0.6).next_to(axes.x_axis.n2p(0.4), DOWN, buff=0.1).shift(RIGHT*0.8)
        num4 = MathTex("\\frac{3}{5}").scale(0.6).next_to(axes.x_axis.n2p(0.6), DOWN, buff=0.1).shift(RIGHT*0.8)
        num5 = MathTex("\\frac{4}{5}").scale(0.6).next_to(axes.x_axis.n2p(0.8), DOWN, buff=0.1).shift(RIGHT*0.8)
        num6 = MathTex("\\frac{5}{5}").scale(0.6).next_to(axes.x_axis.n2p(1), DOWN, buff=0.1).shift(RIGHT*0.8)
        x_axis_nums.add(num1, num2, num3, num4, num5, num6)

        def func(x):
            return scipy_stats.norm.pdf(x, 0.5, (((0.4*0.6)/5))**0.5)

        graph = axes.get_graph(func, x_min = 0, x_max = 1, color = BLUE) 

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT*0.6)
        total_counter = Tex("Sum of Averages: ").scale(0.6).next_to(sample_counter, DOWN, aligned_edge = LEFT, buff=0.4)
        average_counter = MathTex("Average\\quad \\hat{p}:  ").scale(0.6).next_to(total_counter, DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Create(data), Write(VGroup(sample_counter, total_counter, average_counter)))
        self.wait()
        self.play(Create(axes), Write(x_axis_label))
        self.add(x_axis_nums)
        self.wait()

        result = get_data_1(self)
        sample_count = 5
        possible_outcomes = sample_count + 1
        counter_num = 0
        counter_number = Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        counter_number.add_updater(lambda m : m.set_value(counter_num))

        total_sum = 0
        total_number = DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        total_number.add_updater(lambda m : m.set_value(total_sum))

        average = 0
        average_num = DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        average_num.add_updater(lambda m : m.set_value(average))

        r = 0.27           
        start = 0
        sums = [start] * possible_outcomes
        for s in range(3):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP))

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0


            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.play(Write(prop))
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/5 + 0.1), UP, buff=0).set_width(1.55).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)))
            
            sums[tot] += r

        for s in range(37):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.add(boxes)
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP), run_time=0.1)

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0

            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.add(prop)
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/5 + 0.1), UP, buff=0).set_width(1.55).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)), run_time=0.1)
            
            sums[tot] += r
        self.play(Create(graph))

class SamplesOf10(Scene):
    def construct(self):

        data = get_data_1(self)
        axes = Axes(
                x_range = [0, 1.2, 0.1], 
                y_range = [0, 2.5],
                x_length = 10,
                y_length = 4).to_edge(DL).shift(UP*0.2)

        x_axis_label = MathTex("\\hat{p}").scale(0.7).next_to(axes.x_axis, RIGHT, buff=0.1).shift(UP*0.2)

        x_axis_nums = VGroup()
        num1 = MathTex("\\frac{0}{10}").scale(0.6).next_to(axes.x_axis.n2p(0), DOWN, buff=0.1).shift(RIGHT*0.4)
        num2 = MathTex("\\frac{1}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.1), DOWN, buff=0.1).shift(RIGHT*0.4)
        num3 = MathTex("\\frac{2}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.2), DOWN, buff=0.1).shift(RIGHT*0.4)
        num4 = MathTex("\\frac{3}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.3), DOWN, buff=0.1).shift(RIGHT*0.4)
        num5 = MathTex("\\frac{4}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.4), DOWN, buff=0.1).shift(RIGHT*0.4)
        num6 = MathTex("\\frac{5}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.5), DOWN, buff=0.1).shift(RIGHT*0.4)
        num7 = MathTex("\\frac{6}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.6), DOWN, buff=0.1).shift(RIGHT*0.4)
        num8 = MathTex("\\frac{7}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.7), DOWN, buff=0.1).shift(RIGHT*0.4)
        num9 = MathTex("\\frac{8}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.8), DOWN, buff=0.1).shift(RIGHT*0.4)
        num10 = MathTex("\\frac{9}{10}").scale(0.6).next_to(axes.x_axis.n2p(0.9), DOWN, buff=0.1).shift(RIGHT*0.4)
        num11 = MathTex("\\frac{10}{10}").scale(0.6).next_to(axes.x_axis.n2p(1), DOWN, buff=0.1).shift(RIGHT*0.4)
        x_axis_nums.add(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11)

        def func(x):
            return scipy_stats.norm.pdf(x, 0.45, (((0.4*0.6))/10)**0.5)

        graph = axes.get_graph(func, x_min = 0, x_max = 1, color = BLUE) 

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT*0.6)
        total_counter = Tex("Sum of Averages: ").scale(0.6).next_to(sample_counter, DOWN, aligned_edge = LEFT, buff=0.4)
        average_counter = MathTex("Average\\quad \\hat{p}:  ").scale(0.6).next_to(total_counter, DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Create(data), Write(VGroup(sample_counter, total_counter, average_counter)))
        self.wait()
        self.play(Create(axes), Write(x_axis_label))
        self.add(x_axis_nums)
        self.wait()

        result = get_data_1(self)
        sample_count = 10
        possible_outcomes = sample_count + 1
        counter_num = 0
        counter_number = Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        counter_number.add_updater(lambda m : m.set_value(counter_num))

        total_sum = 0
        total_number = DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        total_number.add_updater(lambda m : m.set_value(total_sum))

        average = 0
        average_num = DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        average_num.add_updater(lambda m : m.set_value(average))

        r = 0.12          
        start = 0
        sums = [start] * possible_outcomes
        for s in range(3):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP))

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0


            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.play(Write(prop))
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/10 + 0.05), UP, buff=-0.1).set_width(0.75).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)))
            
            sums[tot] += r

        for s in range(117):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.add(boxes)
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP), run_time=0.1)

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0

            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.add(prop)
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/10 + 0.05), UP, buff=-0.1).set_width(0.75).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)), run_time=0.1)
            
            sums[tot] += r
        self.play(Create(graph))

class SamplesOf20(Scene): 
    def construct(self):

        data = get_data_1(self)
        axes = Axes(
                x_range = [0, 1.05, 0.05], 
                y_range = [0, 4],
                x_length = 10,
                y_length = 4).to_edge(DL).shift(UP*0.2)

        x_axis_label = MathTex("\\hat{p}").scale(0.7).next_to(axes.x_axis, RIGHT, buff=0.1).shift(UP*0.2)

        x_axis_nums = VGroup()
        num1 = MathTex("\\frac{0}{20}").scale(0.4).next_to(axes.x_axis.n2p(0), DOWN, buff=0.1).shift(RIGHT*0.2)
        num2 = MathTex("\\frac{1}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.05), DOWN, buff=0.1).shift(RIGHT*0.2)
        num3 = MathTex("\\frac{2}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.1), DOWN, buff=0.1).shift(RIGHT*0.2)
        num4 = MathTex("\\frac{3}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.15), DOWN, buff=0.1).shift(RIGHT*0.2)
        num5 = MathTex("\\frac{4}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.2), DOWN, buff=0.1).shift(RIGHT*0.2)
        num6 = MathTex("\\frac{5}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.25), DOWN, buff=0.1).shift(RIGHT*0.2)
        num7 = MathTex("\\frac{6}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.3), DOWN, buff=0.1).shift(RIGHT*0.2)
        num8 = MathTex("\\frac{7}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.35), DOWN, buff=0.1).shift(RIGHT*0.2)
        num9 = MathTex("\\frac{8}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.4), DOWN, buff=0.1).shift(RIGHT*0.2)
        num10 = MathTex("\\frac{9}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.45), DOWN, buff=0.1).shift(RIGHT*0.2)
        num11 = MathTex("\\frac{10}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.5), DOWN, buff=0.1).shift(RIGHT*0.2)
        num12 = MathTex("\\frac{11}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.55), DOWN, buff=0.1).shift(RIGHT*0.2)
        num13 = MathTex("\\frac{12}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.6), DOWN, buff=0.1).shift(RIGHT*0.2)
        num14 = MathTex("\\frac{13}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.65), DOWN, buff=0.1).shift(RIGHT*0.2)
        num15 = MathTex("\\frac{14}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.7), DOWN, buff=0.1).shift(RIGHT*0.2)
        num16 = MathTex("\\frac{15}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.75), DOWN, buff=0.1).shift(RIGHT*0.2)
        num17 = MathTex("\\frac{16}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.8), DOWN, buff=0.1).shift(RIGHT*0.2)
        num18 = MathTex("\\frac{17}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.85), DOWN, buff=0.1).shift(RIGHT*0.2)
        num19 = MathTex("\\frac{18}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.9), DOWN, buff=0.1).shift(RIGHT*0.2)
        num20 = MathTex("\\frac{19}{20}").scale(0.4).next_to(axes.x_axis.n2p(0.95), DOWN, buff=0.1).shift(RIGHT*0.2)
        num21 = MathTex("\\frac{20}{20}").scale(0.4).next_to(axes.x_axis.n2p(1), DOWN, buff=0.1).shift(RIGHT*0.2)

        x_axis_nums.add(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12,
        num13, num14, num15, num16, num17, num18, num19, num20, num21)

        def func(x):
            return scipy_stats.norm.pdf(x, 0.425, (((0.4*0.6))/20)**0.5)

        graph = axes.get_graph(func, x_min = 0, x_max = 1, color = BLUE) 

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT*0.6)
        total_counter = Tex("Sum of Averages: ").scale(0.6).next_to(sample_counter, DOWN, aligned_edge = LEFT, buff=0.4)
        average_counter = MathTex("Average\\quad \\hat{p}:  ").scale(0.6).next_to(total_counter, DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Create(data), Write(VGroup(sample_counter, total_counter, average_counter)))
        self.wait()
        self.play(Create(axes), Write(x_axis_label))
        self.add(x_axis_nums)
        self.wait()

        result = get_data_1(self)
        sample_count = 20
        possible_outcomes = sample_count + 1
        counter_num = 0
        counter_number = Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        counter_number.add_updater(lambda m : m.set_value(counter_num))

        total_sum = 0
        total_number = DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        total_number.add_updater(lambda m : m.set_value(total_sum))

        average = 0
        average_num = DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        average_num.add_updater(lambda m : m.set_value(average))

        r = 0.05          
        start = 0
        sums = [start] * possible_outcomes
        for s in range(3):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP).set_width(4))

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0


            prop = DecimalNumber(num_decimal_places = 2)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.play(Write(prop))
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/20 + 0.025), UP, buff=-0.05).set_width(0.4).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)))
            
            sums[tot] += r

        for s in range(297):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.add(boxes)
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP).set_width(4), run_time=0.1)

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0

            prop = DecimalNumber(num_decimal_places = 2)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.add(prop)
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/20 + 0.025), UP, buff=-0.05).set_width(0.4).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)), run_time=0.1)
            
            sums[tot] += r
        self.play(Create(graph))

class SamplesOf3(Scene):
    def construct(self):

        data = get_data_1(self)
        axes = Axes(
                x_range = [0, 4/3, 1/3], 
                y_range = [0, 1.5, 0.5],
                x_length = 9,
                y_length = 4).to_edge(DL).shift(UP*0.2+RIGHT*4)

        x_axis_label = MathTex("\\hat{p}").scale(0.7).next_to(axes.x_axis, RIGHT, buff=0.1).shift(UP*0.2)

        x_axis_nums = VGroup()
        num1 = MathTex("\\frac{0}{3}").scale(0.6).next_to(axes.x_axis.n2p(0), DOWN, buff=0.1).shift(RIGHT*0.9)
        num2 = MathTex("\\frac{1}{3}").scale(0.6).next_to(axes.x_axis.n2p(0.333333), DOWN, buff=0.1).shift(RIGHT*0.9)
        num3 = MathTex("\\frac{2}{3}").scale(0.6).next_to(axes.x_axis.n2p(0.66666), DOWN, buff=0.1).shift(RIGHT*0.9)
        num4 = MathTex("\\frac{3}{3}").scale(0.6).next_to(axes.x_axis.n2p(1), DOWN, buff=0.1).shift(RIGHT*0.9)
        x_axis_nums.add(num1, num2, num3, num4)

        def func(x):
            return scipy_stats.norm.pdf(x, 0.4, (((0.4*0.6))/3)**0.5)

        graph = axes.get_graph(func, x_min = 0, x_max = 1, color = BLUE) 

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT*0.6)
        total_counter = Tex("Sum of Averages: ").scale(0.6).next_to(sample_counter, DOWN, aligned_edge = LEFT, buff=0.4)
        average_counter = MathTex("Average\\quad \\hat{p}:  ").scale(0.6).next_to(total_counter, DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Create(data), Write(VGroup(sample_counter, total_counter, average_counter)))
        self.wait()
        self.play(Create(axes), Write(x_axis_label))
        self.add(x_axis_nums)
        self.wait()

        result = get_data_1(self)
        sample_count = 3
        possible_outcomes = sample_count + 1
        counter_num = 0
        counter_number = Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        counter_number.add_updater(lambda m : m.set_value(counter_num))

        total_sum = 0
        total_number = DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        total_number.add_updater(lambda m : m.set_value(total_sum))

        average = 0
        average_num = DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        average_num.add_updater(lambda m : m.set_value(average))

        r = 0.4    
        start = 0
        sums = [start] * possible_outcomes
        for s in range(5):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP))

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0


            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.play(Write(prop))
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/3 + 0.33333/2), UP, buff=0).set_width(1.3).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)))
            
            sums[tot] += r

        for s in range(20):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.add(boxes)
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP), run_time=0.1)

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0

            prop = DecimalNumber(num_decimal_places = 1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.add(prop)
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/3 + 0.333333/2), UP, buff=0).set_width(1.3).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)), run_time=0.1)
            
            sums[tot] += r

        self.play(Create(graph))

class SamplesOf3CLT(MovingCameraScene):
    def construct(self):

        data = get_data_1(self)
        axes = Axes(
                x_range = [0, 4/3, 1/3], 
                y_range = [0, 1.5, 0.5],
                x_length = 9,
                y_length = 4).to_edge(DL).shift(UP*0.2+RIGHT*4)

        x_axis_label = MathTex("\\hat{p}").scale(0.7).next_to(axes.x_axis, RIGHT, buff=0.1).shift(UP*0.2)

        x_axis_nums = VGroup()
        num1 = MathTex("\\frac{0}{3}").scale(0.6).next_to(axes.x_axis.n2p(0), DOWN, buff=0.1).shift(RIGHT*0.9)
        num2 = MathTex("\\frac{1}{3}").scale(0.6).next_to(axes.x_axis.n2p(0.333333), DOWN, buff=0.1).shift(RIGHT*0.9)
        num3 = MathTex("\\frac{2}{3}").scale(0.6).next_to(axes.x_axis.n2p(0.66666), DOWN, buff=0.1).shift(RIGHT*0.9)
        num4 = MathTex("\\frac{3}{3}").scale(0.6).next_to(axes.x_axis.n2p(1), DOWN, buff=0.1).shift(RIGHT*0.9)
        x_axis_nums.add(num1, num2, num3, num4)

        def func(x):
            return scipy_stats.norm.pdf(x, 0.4, (((0.4*0.6))/3)**0.5)

        graph = axes.get_graph(func, x_min = 0, x_max = 1, color = BLUE) 

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT*0.6)
        total_counter = Tex("Sum of Averages: ").scale(0.6).next_to(sample_counter, DOWN, aligned_edge = LEFT, buff=0.4)
        average_counter = MathTex("Average\\quad \\hat{p}:  ").scale(0.6).next_to(total_counter, DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Create(data), Write(VGroup(sample_counter, total_counter, average_counter)))
        self.wait()
        self.play(Create(axes), Write(x_axis_label))
        self.add(x_axis_nums)
        self.wait()

        result = get_data_1(self)
        sample_count = 3
        possible_outcomes = sample_count + 1
        counter_num = 0
        counter_number = Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        counter_number.add_updater(lambda m : m.set_value(counter_num))

        total_sum = 0
        total_number = DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        total_number.add_updater(lambda m : m.set_value(total_sum))

        average = 0
        average_num = DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        average_num.add_updater(lambda m : m.set_value(average))

        r = 0.4    
        start = 0
        sums = [start] * possible_outcomes
        for s in range(5):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP))

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0


            prop = DecimalNumber(num_decimal_places = 2)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.play(Write(prop))
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/3 + 0.33333/2), UP, buff=0).set_width(1.3).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)))
            
            sums[tot] += r

        moved_text = VGroup(average_num, average_counter, sample_counter, counter_number, total_counter, total_number)

        self.play(self.camera.frame.animate.scale(3.5).shift(RIGHT*4+UP*7), moved_text.animate.shift(UP*4+RIGHT*4).scale(2.5), run_time=2)

        for s in range(120):
            #THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0,50), k=sample_count)

            #THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            for i, res in enumerate(a):
                res = result[a[i]]
                res_values.add(res)

            #THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            for i, box in enumerate(res_values):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            #THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            for i, res in enumerate(res_values):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.add(boxes)
            self.play(moved_result.animate.arrange(RIGHT*0.3,buff=0).to_edge(UP), run_time=0.1)

            #THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i,value in enumerate(a):
                if value < 20: 
                    a[i] = 1
                else: a[i] = 0

            prop = DecimalNumber(num_decimal_places = 2)
            tot = sum(a)
            prop.set_value(tot / sample_count).set_height(0.2)
            

            prop.next_to(moved_result, RIGHT, buff=0.1)
            self.add(prop)
            counter_num += 1
            self.add(counter_number)
            
            total_sum += tot / sample_count
            self.add(total_number)

            average = (total_sum) / (counter_num)
            self.add(average_num)

            self.play(moved_result.animate.next_to(axes.x_axis.n2p(tot/3 + 0.333333/2), UP, buff=0).set_width(1.3).shift(UP*sums[tot]),
            FadeOut(VGroup(boxes, prop)), run_time=0.1)
            
            sums[tot] += r