from big_ol_pile_of_manim_imports import *
import math

class ThanosReasons(Scene):
    def construct(self):
        thanos = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanosthrone.png").scale(3).move_to(np.array([0,0,0]))
        path = Line(np.array([0,0,0]),np.array([-3,0,0]))
        power = TextMobject("Power?").scale(2).next_to(thanos,np.array([0.8,0,0]))

        self.play(
        FadeIn(thanos),
        run_time=2
        )
        self.play(
        MoveAlongPath(thanos,path),
        run_time=2
        )
        self.play(
        FadeIn(power),
        run_time=2
        )
        self.play(
        FadeOut(power),
        FadeOut(thanos),
        run_time=2
        )
