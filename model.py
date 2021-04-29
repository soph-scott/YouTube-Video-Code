from big_ol_pile_of_manim_imports import *
import math

class Model(GraphScene):
    def construct(self):
        equation1 = TextMobject("Logistic Growth Model for Human Population:").scale(0.8).move_to(np.array([-2,3,0]))
        equation2 = TextMobject("$>$ 2018 is our $t=0$").scale(0.7).move_to(np.array([-2,2,0])).align_to(equation1,LEFT)
        equation3 = TextMobject("$>$ Measure population in billions").scale(0.7).move_to(np.array([-2,1,0])).align_to(equation1,LEFT)
        equation4 = TextMobject("$>$ $N_0=7.5$").scale(0.7).move_to(np.array([-2,0,0])).align_to(equation1,LEFT)

        equation5 = TextMobject("$>$ $K=12$").scale(0.7).move_to(np.array([-2,-1,0])).align_to(equation1,LEFT)

        dates1 = TextMobject("2018").scale(0.7).move_to(np.array([-3,0,0]))
        dates2 = TextMobject("2019").scale(0.7).move_to(np.array([-1.5,0,0]))
        dates3 = TextMobject("2020").scale(0.7).move_to(np.array([0,0,0]))
        dates4 = TextMobject("2021").scale(0.7).move_to(np.array([1.5,0,0]))
        dates5 = TextMobject("...").scale(0.7).move_to(np.array([3,0,0]))
        times1 = TextMobject("$t=0$").scale(0.7).next_to(dates1,DOWN)
        times2 = TextMobject("$t=1$").scale(0.7).next_to(dates2,DOWN)
        times3 = TextMobject("$t=2$").scale(0.7).next_to(dates3,DOWN)
        times4 = TextMobject("$t=3$").scale(0.7).next_to(dates4,DOWN)
        times5 = TextMobject("$t\\to\\infty$").scale(0.7).next_to(dates5,np.array([0,-1.5,0]))

        capacity = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/capacity.png").scale(3)
        capacity.move_to(np.array([4,-0.7,0]))

        equation6 = TextMobject("$N(t) = \\frac{KN_0e^{rt}}{K - N_0 + N_0e^{rt}}$").scale(0.9)
        equation7 = TextMobject("$N(2) = \\frac{12\\cdot7.5e^{2r}}{12 - 7.5 + 7.5e^{2r}}$").scale(0.9)
        equation8 = TextMobject("$7.8(4.5 + 7.5e^{2r}) = 90e^{2r}$").scale(0.9)
        equation9 = TextMobject("$e^{2r} = \\frac{39}{35}$").scale(0.9)
        equation10 = TextMobject("$r = \\frac{1}{2}\\text{ln}(\\frac{39}{35})$").scale(0.9)
        equation11 = TextMobject("$r \\approx 0.05$").scale(0.9).set_color(YELLOW)

        rectangle = Rectangle(height=6,width=5.6).move_to(np.array([4,-0.6,0]))

        equation6.move_to(np.array([4,2,0]))
        equation7.next_to(equation6,np.array([0,-2,0]))
        equation8.next_to(equation7,np.array([0,-2,0]))
        equation9.next_to(equation8,np.array([0,-2,0]))
        equation10.next_to(equation9,np.array([0,-2,0]))
        equation11.next_to(equation10,np.array([0,-2,0]))

        equation12 = TextMobject("$>$ $r=0.05$").scale(0.7).move_to(np.array([-2,-2,0])).align_to(equation1,LEFT)

        self.play(FadeIn(equation1))
        self.wait(2)
        self.play(FadeIn(equation2))
        self.play(FadeIn(dates1),FadeIn(times1),run_time=0.5)
        self.play(FadeIn(dates2),FadeIn(times2),run_time=0.5)
        self.play(FadeIn(dates3),FadeIn(times3),run_time=0.5)
        self.play(FadeIn(dates4),FadeIn(times4),run_time=0.5)
        self.play(FadeIn(dates5),FadeIn(times5),run_time=0.5)
        self.play(FadeOut(dates1),
        FadeOut(dates2),
        FadeOut(dates3),
        FadeOut(dates4),
        FadeOut(dates5),
        FadeOut(times1),
        FadeOut(times2),
        FadeOut(times3),
        FadeOut(times4),
        FadeOut(times5)
        )
        self.wait(2)
        self.play(FadeIn(equation3))
        self.wait(2)
        self.play(FadeIn(equation4))
        self.wait(2)
        self.play(FadeIn(capacity))
        self.wait(2)
        self.play(FadeIn(equation5))
        self.wait(2)
        self.play(FadeOut(capacity))
        self.wait(2)
        self.play(FadeIn(equation6),FadeIn(rectangle))
        self.wait(2)
        self.play(FadeIn(equation7))
        self.wait(1)
        self.play(FadeIn(equation8))
        self.wait(1)
        self.play(FadeIn(equation9))
        self.wait(1)
        self.play(FadeIn(equation10))
        self.wait(1)
        self.play(FadeIn(equation11))
        self.wait(1)
        self.play(FadeOut(equation6),
        FadeOut(equation7),
        FadeOut(equation8),
        FadeOut(equation9),
        FadeOut(equation10),
        FadeOut(rectangle),
        Transform(equation11,equation12)
        )
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Parameters(Scene):
    def construct(self):
        equation1 = TextMobject("Model Parameters:").scale(1).move_to(np.array([0,2,0]))
        equation2 = TextMobject("$>$ $N_0=7.5$").scale(0.9).move_to(np.array([-2,1,0])).align_to(equation1,LEFT)
        equation3 = TextMobject("$>$ $K=12$").scale(0.9).move_to(np.array([-2,0,0])).align_to(equation1,LEFT)
        equation4 = TextMobject("$>$ $r=0.05$").scale(0.9).move_to(np.array([-2,-1,0])).align_to(equation1,LEFT)
        equation5 = TextMobject("$>$ $N_0=3.75$").scale(0.9).move_to(np.array([-2,1,0])).align_to(equation1,LEFT).set_color(YELLOW)
        self.play(FadeIn(equation1),
        FadeIn(equation2),
        FadeIn(equation3),
        FadeIn(equation4)
        )
        self.wait(1)
        self.play(Transform(equation2,equation5))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
