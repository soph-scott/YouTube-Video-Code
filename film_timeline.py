from big_ol_pile_of_manim_imports import *
import math
import os

class FilmTimeline(MovingCameraScene):
    def construct(self):
        films = ["filma","filmb","filmc","filmd","filme","filmf","filmg","filmh","filmi","filmj","filmk","filml","filmm","filmn","filmo","filmp","filmq","filmr","films","filmt","filmu","filmv","filmw"]
        film_group = Group()
        place = 0

        for x in range(0,23):
            if x==18:
                infinity_war = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[x])).scale(2.5).move_to(np.array([place,0,0]))
                film_group.add(infinity_war)
                self.add(infinity_war)
            if x==21:
                end_game = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[x])).scale(2.5).move_to(np.array([place,0,0]))
                film_group.add(end_game)
                self.add(end_game)
            else:
                image = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[x])).scale(2.5).move_to(np.array([place,0,0]))
                film_group.add(image)
                self.add(image)
            place = place + 5

        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_width,1.5,
            self.camera_frame.move_to,infinity_war
        )
        self.wait()

        self.play(Restore(self.camera_frame))
