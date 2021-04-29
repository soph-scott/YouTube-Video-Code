from big_ol_pile_of_manim_imports import *
import math

class Intro(Scene):
    def construct(self):
        text1 = TextMobject("THANOS").scale(4).move_to(np.array([0,2.5,0]))
        text2 = TextMobject("WAS").scale(4).move_to(np.array([0,0,0]))
        text3 = TextMobject("WRONG?!").scale(4).move_to(np.array([0,-2.5,0]))

        self.add(text1)
        self.add(text2)
        self.add(text3)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Outro(Scene):
    def construct(self):
        badmath = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/badmath.png").scale(3)

        self.play(FadeIn(badmath),run_time=2)
        self.wait(2)
        self.play(FadeOut(badmath),run_time=2)

        predicting = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/predicting.png").scale(3).move_to(np.array([-1,-1,0]))
        predictionbubble = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/predictionbubble.png").scale(1).move_to(np.array([2,1.5,0]))

        self.play(FadeIn(predicting))
        self.play(GrowFromPoint(predictionbubble,np.array([-1,0.7,0])))
        self.wait(1)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Outro2(Scene):
    def construct(self):
        arrow1 = Arrow(np.array([0,0.5,0]),np.array([0,-1,0])).scale(2).move_to(np.array([-3,-0.5,0]))
        arrow2 = Arrow(np.array([0,0.5,0]),np.array([0,-1,0])).scale(2).move_to(np.array([0,-0.5,0]))
        arrow3 = Arrow(np.array([0,0.5,0]),np.array([0,-1,0])).scale(2).move_to(np.array([3,-0.5,0]))
        text = TextMobject("Link in description!").scale(2).next_to(arrow2,UP)

        self.play(FadeIn(arrow1),FadeIn(arrow2),FadeIn(arrow3),FadeIn(text))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Outro3(Scene):
    def construct(self):
        text = TextMobject("Thanks for watching!").scale(2.5)

        self.play(FadeIn(text))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
