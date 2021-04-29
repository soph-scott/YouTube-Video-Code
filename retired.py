from big_ol_pile_of_manim_imports import *
import math

class Retired(Scene):
    def construct(self):
        gem1 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem1.png").scale(1.7).move_to(np.array([-5,0,0]))
        gem2 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem2.png").scale(1.7).move_to(np.array([-3,0,0]))
        gem3 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem3.png").scale(1.7).move_to(np.array([-1,0,0]))
        gem4 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem4.png").scale(1.7).move_to(np.array([1,0,0]))
        gem5 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem5.png").scale(1.7).move_to(np.array([3,0,0]))
        gem6 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem6.png").scale(1.7).move_to(np.array([5,0,0]))

        self.play(GrowFromPoint(gem1,ORIGIN),
        GrowFromPoint(gem2,ORIGIN),
        GrowFromPoint(gem3,ORIGIN),
        GrowFromPoint(gem4,ORIGIN),
        GrowFromPoint(gem5,ORIGIN),
        GrowFromPoint(gem6,ORIGIN)
        )

        self.play(FadeOut(gem1),
        FadeOut(gem2),
        FadeOut(gem3),
        FadeOut(gem4),
        FadeOut(gem5),
        FadeOut(gem6))

class Retired2(Scene):
    def construct(self):
        retired = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/retired.png").scale(3)
        self.play(FadeIn(retired))
        self.wait(2)
        self.play(FadeOut(retired))
