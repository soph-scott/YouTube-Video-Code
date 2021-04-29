from big_ol_pile_of_manim_imports import *
import math

class PlanChecklist(Scene):
    def construct(self):
        plan1 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/plan1.png").scale(4).move_to(np.array([0.008,0,0]))
        plan2 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/plan2.png").scale(4).move_to(np.array([0,0,0]))
        plan3 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/plan3.png").scale(4).move_to(np.array([0,0,0]))
        plan4 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/plan4.png").scale(4).move_to(np.array([0,0,0]))

        self.play(FadeIn(plan1))
        self.play(ShowCreation(plan2))
        self.play(ShowCreation(plan3))
        self.play(ShowCreation(plan4))

class PlanChecklist2(Scene):
    def construct(self):
        plan4 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/plan4.png").scale(4).move_to(np.array([0,0,0]))
        self.add(plan4)

        self.play(FadeOut(plan4))
