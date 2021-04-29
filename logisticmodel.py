from big_ol_pile_of_manim_imports import *
import math

class Maths(Scene):
    def construct(self):
        text = TextMobject("Did Thanos get his").move_to(np.array([0,0.5,0]))
        text2 = TextMobject("maths right?").next_to(text,DOWN)
        self.play(
        FadeIn(text),
        FadeIn(text2),
        run_time=1.3
        )
        underline = Line(np.array([-1.5,-0.5,0]),np.array([0,-0.5,0]))
        self.play(
        FadeIn(underline),
        run_time=1
        )
        self.play(FadeOut(text),FadeOut(text2),FadeOut(underline))

class Maths2(Scene):
    def construct(self):
        person = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thinking.png").scale(3).move_to(np.array([0,-1,0]))
        text1 = TextMobject("Problems solved?").scale(0.5)
        text2 = TextMobject("How to explore further?").scale(0.5)
        text1.move_to(np.array([-2.5,1,0]))
        text2.move_to(np.array([2,1,0]))
        self.play(FadeIn(person))
        self.play(GrowFromPoint(text1,np.array([0,1,0])))
        self.wait(2)
        self.play(GrowFromPoint(text2,np.array([0,1,0])))
        self.wait(2)

        person2 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/idea.png").scale(3).move_to(np.array([0,-1,0]))
        text3 = TextMobject("We need a population model!").scale(1)
        text3.move_to(np.array([0,2,0]))

        self.play(
        FadeOut(person),
        FadeOut(text1),
        FadeOut(text2),
        FadeIn(person2))
        self.play(GrowFromPoint(text3,np.array([0,1,0])))
        self.play(FadeOut(person2),FadeOut(text3))

class Maths3(Scene):
    def construct(self):
        equation = TextMobject("$\\frac{dN}{dt} = rN \\big(1 - \\frac{N}{K}\\big)$").scale(2)
        equation.move_to(np.array([0,1,0]))
        self.play(FadeIn(equation))

        arrow1 = Arrow(np.array([-4,-1.5,0]),np.array([-3,0.27,0]))
        arrow2 = Arrow(np.array([-1,-1.5,0]),np.array([-1,0.57,0]))
        arrow3 = Arrow(np.array([4,-1.5,0]),np.array([2.75,0.27,0]))

        text1 = TextMobject("rate of").scale(0.8).move_to(np.array([-4,-1.6,0]))
        text2 = TextMobject("change").scale(0.8).next_to(text1,DOWN)
        text3 = TextMobject("growth").scale(0.8).move_to(np.array([-1,-1.6,0]))
        text4 = TextMobject("rate").scale(0.8).next_to(text3,DOWN)
        text5 = TextMobject("carrying").scale(0.8).move_to(np.array([4,-1.6,0]))
        text6 = TextMobject("capacity").scale(0.8).next_to(text5,DOWN)

        framebox1 = Rectangle(height=1.6,width=1.3).move_to(np.array([-3.15,1,0])).set_color(YELLOW)
        framebox2 = Rectangle(height=0.95,width=0.64).move_to(np.array([-0.97,1,0])).set_color(YELLOW)
        framebox3 = Rectangle(height=0.6,width=0.7).move_to(np.array([2.92,0.6,0])).set_color(YELLOW)

        self.play(FadeIn(framebox1))
        self.play(FadeIn(arrow1))
        self.wait(1)
        self.play(FadeIn(text1),FadeIn(text2))
        self.wait(1)
        self.remove(framebox1)
        self.play(Transform(framebox1,framebox2))
        self.remove(framebox1)
        self.add(framebox2)
        self.play(FadeIn(arrow2))
        self.wait(1)
        self.play(FadeIn(text3),FadeIn(text4))
        self.wait(1)
        self.play(Transform(framebox2,framebox3))
        self.play(FadeIn(arrow3))
        self.wait(1)
        self.play(FadeIn(text5),FadeIn(text6))
        self.wait(1)
        self.play(FadeOut(arrow1),
        FadeOut(arrow2),
        FadeOut(arrow3),
        FadeOut(text1),
        FadeOut(text2),
        FadeOut(text3),
        FadeOut(text4),
        FadeOut(text5),
        FadeOut(text6),
        FadeOut(framebox2)
        )

class Maths4(Scene):
    def construct(self):
        equation = TextMobject("$\\frac{dN}{dt} = rN \\big(1 - \\frac{N}{K}\\big)$").scale(2)
        equation.move_to(np.array([0,1,0]))
        self.add(equation)
        path = Line(np.array([0,1,0]),np.array([0,2,0]))
        solved = TextMobject("$N(t) = \\frac{KN_0e^{rt}}{K - N_0 + N_0e^{rt}}$").scale(2).move_to(np.array([0,-2,0]))
        arrow = Arrow(np.array([0,1,0]),np.array([0,-1,0]))
        self.play(MoveAlongPath(equation,path))
        self.play(FadeIn(arrow))
        self.play(FadeIn(solved))
        path2 = Line(np.array([0,-2,0]),np.array([0,0,0]))
        self.play(FadeOut(equation),FadeOut(arrow))
        self.play(MoveAlongPath(solved,path2))
        self.wait(4)
        self.play(FadeOut(solved))

class Maths5(GraphScene):

    CONFIG = {
        "y_max" : 25,
        "y_min" : 0,
        "x_max" : 45,
        "x_min" : 0,
        "x_tick_frequency" : 5,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$N(t)$",
        "graph_origin": 3 * DOWN + 4.5 * LEFT,
        "y_labeled_nums" : [],
        "x_labeled_nums" : [],
        }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (20*1*math.exp(0.2*x))/(20-1+1*math.exp(0.2*x)), color = GREEN)
        graph2 = self.get_graph(lambda x : 20, color = GREEN)
        label = TextMobject("$K$").move_to(np.array([-5,1.8,0]))
        self.play(ShowCreation(graph),run_time=4)
        line = DashedLine(self.input_to_graph_point(0,graph2),self.input_to_graph_point(45,graph2)).set_color(YELLOW)
        self.play(FadeIn(line),run_time=2)
        self.play(FadeIn(label))
        self.wait(4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Maths6(GraphScene):
    def construct(self):
        yeast = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/yeast.png").scale(1.5).move_to(np.array([-3.5,0,0]))
        sheep = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/sheep.png").scale(1.5).move_to(np.array([3.5,0,0]))
        human = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/humans.png").scale(2).move_to(np.array([0,0,0]))

        self.play(GrowFromCenter(yeast))
        self.play(GrowFromCenter(sheep))
        self.play(GrowFromCenter(human))
        self.wait(1)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Maths7(Scene):
    def construct(self):
        equation = TextMobject("$\\frac{dN}{dt} = rN \\big(1 - \\frac{N}{K}\\big)$").scale(2)
        equation.move_to(np.array([0,1,0]))
        self.play(FadeIn(equation))
        path = Line(np.array([0,1,0]),np.array([0,2,0]))
        solved = TextMobject("$N(t) = \\frac{KN_0e^{rt}}{K - N_0 + N_0e^{rt}}$").scale(2).move_to(np.array([0,-2,0]))
        arrow = Arrow(np.array([0,1,0]),np.array([0,-1,0]))
        self.play(MoveAlongPath(equation,path))
        self.play(FadeIn(arrow))
        self.play(FadeIn(solved))
        self.play(*[FadeOut(mob)for mob in self.mobjects])
