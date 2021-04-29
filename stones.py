from big_ol_pile_of_manim_imports import *
import math

class Stones(Scene):
    def construct(self):
        gem1 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem1.png").scale(1.7).move_to(np.array([-5,0,0]))
        gem2 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem2.png").scale(1.7).move_to(np.array([-3,0,0]))
        gem3 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem3.png").scale(1.7).move_to(np.array([-1,0,0]))
        gem4 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem4.png").scale(1.7).move_to(np.array([1,0,0]))
        gem5 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem5.png").scale(1.7).move_to(np.array([3,0,0]))
        gem6 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/gem6.png").scale(1.7).move_to(np.array([5,0,0]))

        self.play(FadeIn(gem1))
        self.play(FadeIn(gem2))
        self.play(FadeIn(gem3))
        self.play(FadeIn(gem4))
        self.play(FadeIn(gem5))
        self.play(FadeIn(gem6))
        self.play(FadeOut(gem1),
        FadeOut(gem2),
        FadeOut(gem3),
        FadeOut(gem4),
        FadeOut(gem5),
        FadeOut(gem6)
        )
