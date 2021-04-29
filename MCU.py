from big_ol_pile_of_manim_imports import *
import math

class MCU(Scene):
    def construct(self):
        mcu = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/MCU.png").scale(2)
        path = Line(np.array([0,-10,0]),np.array([0,0,0]))

        self.play(
        GrowFromCenter(mcu),
        run_time=7.5
        )

class MCUFade(Scene):
    def construct(self):
        mcu = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/MCU.png").scale(2)
        self.add(mcu)

        self.play(
        FadeOut(mcu)
        )
