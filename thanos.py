from big_ol_pile_of_manim_imports import *
import math

class Thanos(ZoomedScene):
        CONFIG = {
                "zoom_factor": 0.5,
                "zoomed_display_height": 3,
                "zoomed_display_width": 4,
                "image_frame_stroke_width": 20,
                "zoomed_display_corner": UP + UP + LEFT,
                "zoomed_camera_config": {
                "default_frame_stroke_width": 3,
                },
                }

        def construct(self):
                avengers_and_thanos = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_and_avengers.png").scale(3)
                self.add(avengers_and_thanos)
                self.play(
                FadeIn(avengers_and_thanos)
                )

                self.wait()

                path = Line(np.array([0,0,0]),np.array([1,0,0]))

                self.play(MoveAlongPath(avengers_and_thanos, path))

                zoomed_camera = self.zoomed_camera
                zoomed_display = self.zoomed_display
                frame = zoomed_camera.frame
                zoomed_display_frame = zoomed_display.display_frame

                frame.move_to(np.array([1,2.25,0]))
                frame.set_color(PURPLE)

                zoomed_display_frame.set_color(RED)
                zoomed_display.shift(DOWN)

        # brackground zoomed_display
                zd_rect = BackgroundRectangle(
                zoomed_display,
                fill_opacity=0,
                buff=MED_SMALL_BUFF,
                )

                self.add_foreground_mobject(zd_rect)

                # animation of unfold camera
                unfold_camera = UpdateFromFunc(
                zd_rect,
                lambda rect: rect.replace(zoomed_display)
                )

                self.play(
                ShowCreation(frame)
                )

                # Activate zooming
                self.activate_zooming()

                self.play(
                # You have to add this line
                self.get_zoomed_display_pop_out_animation(),
                unfold_camera,
                )

                black_screen = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/black.png").scale(5)

                self.play(
                FadeIn(black_screen),
                FadeOut(zoomed_display_frame),
                FadeOut(frame)
                )

class ThanosPlan(Scene):
    def construct(self):
        group1 = Group()
        for x in range(-5, 0):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group1.add(image)
                self.add(image)
        group2 = Group()
        for x in range(0, 5):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group2.add(image)
                self.add(image)

        group1.shift(np.array([0.5,0,0]))
        group2.shift(np.array([0.5,0,0]))
        self.play(FadeIn(group1),FadeIn(group2))

        group3 = Group()
        for x in range(0, 5):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group3.add(image)
                self.add(image)

        group3.shift(np.array([0.5,0,0]))

        self.play(FadeIn(group3))

        self.wait()

        self.play(
        FadeOut(group2),
        FadeOut(group3)
        )

class ThanosPlan2(Scene):
    def construct(self):
        group1 = Group()
        for x in range(-5, 0):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group1.add(image)
                self.add(image)

        group1.shift(np.array([0.5,0,0]))

        path = Line(np.array([-2.5,0,0]),np.array([0,0,0]),)

        self.play(MoveAlongPath(group1,path))

        self.wait()

        self.play(
        FadeOut(group1)
        )

class ThanosPlan3(Scene):
    def construct(self):
        group1 = Group()
        group2 = Group()
        group3 = Group()
        group4 = Group()
        group5 = Group()
        group6 = Group()
        group7 = Group()
        group8 = Group()
        group9 = Group()
        group10 = Group()
        for x in range(-5,-4):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group1.add(image)
        for x in range(-4,-3):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group2.add(image)
        for x in range(-3,-2):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group3.add(image)
        for x in range(-2,-1):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group4.add(image)
        for x in range(-1,0):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group5.add(image)
        for x in range(0,1):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group6.add(image)
        for x in range(1,2):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group7.add(image)
        for x in range(2,3):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group8.add(image)
        for x in range(3,4):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group9.add(image)
        for x in range(4,5):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group10.add(image)


        group1.shift(np.array([0.5,0,0]))
        group2.shift(np.array([0.5,0,0]))
        group3.shift(np.array([0.5,0,0]))
        group4.shift(np.array([0.5,0,0]))
        group5.shift(np.array([0.5,0,0]))
        group6.shift(np.array([0.5,0,0]))
        group7.shift(np.array([0.5,0,0]))
        group8.shift(np.array([0.5,0,0]))
        group9.shift(np.array([0.5,0,0]))
        group10.shift(np.array([0.5,0,0]))

        self.play(FadeIn(group1),
        FadeIn(group2),
        FadeIn(group3),
        FadeIn(group4),
        FadeIn(group5),
        FadeIn(group6),
        FadeIn(group7),
        FadeIn(group8),
        FadeIn(group9),
        FadeIn(group10)
        )

        group11 = Group()
        group12 = Group()
        group13 = Group()
        group14 = Group()
        group15 = Group()
        group16 = Group()
        group17 = Group()
        group18 = Group()
        group19 = Group()
        group20 = Group()

        for x in range(-5,-4):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group11.add(image)
        for x in range(-4,-3):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group12.add(image)
        for x in range(-3,-2):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group13.add(image)
        for x in range(-2,-1):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group14.add(image)
        for x in range(-1,0):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group15.add(image)
        for x in range(0,1):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group16.add(image)
        for x in range(1,2):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group17.add(image)
        for x in range(2,3):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group18.add(image)
        for x in range(3,4):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group19.add(image)
        for x in range(4,5):
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/mini_thanos_red.png").scale(0.5).move_to(np.array([x,y,0]))
                group20.add(image)

        group11.shift(np.array([0.5,0,0]))
        group12.shift(np.array([0.5,0,0]))
        group13.shift(np.array([0.5,0,0]))
        group14.shift(np.array([0.5,0,0]))
        group15.shift(np.array([0.5,0,0]))
        group16.shift(np.array([0.5,0,0]))
        group17.shift(np.array([0.5,0,0]))
        group18.shift(np.array([0.5,0,0]))
        group19.shift(np.array([0.5,0,0]))
        group20.shift(np.array([0.5,0,0]))

        self.play(FadeIn(group20))

        self.play(FadeIn(group19),
        FadeOut(group20),
        FadeOut(group10))

        self.play(FadeIn(group18),
        FadeOut(group19),
        FadeOut(group9))

        self.play(FadeIn(group17),
        FadeOut(group18),
        FadeOut(group8))

        self.play(FadeIn(group16),
        FadeOut(group17),
        FadeOut(group7))

        self.play(FadeIn(group15),
        FadeOut(group16),
        FadeOut(group6))

        self.play(FadeIn(group14),
        FadeOut(group15),
        FadeOut(group5))

        self.play(FadeIn(group13),
        FadeOut(group14),
        FadeOut(group4))

        self.play(FadeIn(group12),
        FadeOut(group13),
        FadeOut(group3))

        self.play(FadeIn(group11),
        FadeOut(group12),
        FadeOut(group2))

        self.play(FadeOut(group11),
        FadeOut(group1))

class ThanosSnap(Scene):
        def construct(self):
                snap1 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/snaps.png").scale(3)
                snap2 = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/snaps2.png").scale(3)

                self.add(snap1)

                self.play(FadeIn(snap1))
                self.wait()
                self.remove(snap1)
                self.add(snap2)
                self.play(ShowCreation(snap2))
                self.play(FadeOut(snap2))
