from big_ol_pile_of_manim_imports import *
import math
import os

class FilmTimeline(MovingCameraScene):
        def construct(self):
            films = ["filma","filmb","filmc","filmd","filme","filmf","filmg","filmh","filmi","filmj","filmk","filml","filmm","filmn","filmo","filmp","filmq","filmr","films","filmt","filmu","filmv","filmw"]
            image_1 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[0])).scale(0.8).move_to(np.array([-6,3,0]))
            self.add(image_1)
            text_1 = TextMobject("2008").scale(0.4)
            text_1.next_to(image_1,np.array([0,-0.2,0]))
            self.add(text_1)
            self.camera_frame.save_state()
            self.play(
                self.camera_frame.set_width,image_1.get_width()*3.5,
                self.camera_frame.move_to,image_1,
                FadeIn(image_1),
                FadeIn(text_1)
                )
            self.wait()

            self.play(
                Restore(self.camera_frame),
            )
            self.wait()

class FilmTimeline2(Scene):
        def construct(self):
            films = ["filma","filmb","filmc","filmd","filme","filmf","filmg","filmh","filmi","filmj","filmk","filml","filmm","filmn","filmo","filmp","filmq","filmr","films","filmt","filmu","filmv","filmw"]
            image_1 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[0])).scale(0.8).move_to(np.array([-6,3,0]))
            group = Group()
            group.add(image_1)
            text_1 = TextMobject("2008").scale(0.4)
            self.add(image_1)
            text_1.next_to(image_1,np.array([0,-0.2,0]))
            self.add(text_1)
            image_2 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[1])).scale(0.8).move_to(np.array([-4,3,0]))
            image_3 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[2])).scale(0.8).move_to(np.array([-2,3,0]))
            image_4 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[3])).scale(0.8).move_to(np.array([0,3,0]))
            image_5 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[4])).scale(0.8).move_to(np.array([2,3,0]))
            image_6 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[5])).scale(0.8).move_to(np.array([4,3,0]))
            image_7 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[6])).scale(0.8).move_to(np.array([6,3,0]))
            image_8 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[7])).scale(0.8).move_to(np.array([-6,1,0]))
            image_9 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[8])).scale(0.8).move_to(np.array([-4,1,0]))
            image_10 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[9])).scale(0.8).move_to(np.array([-2,1,0]))
            image_11 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[10])).scale(0.8).move_to(np.array([0,1,0]))
            image_12 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[11])).scale(0.8).move_to(np.array([2,1,0]))
            image_13 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[12])).scale(0.8).move_to(np.array([4,1,0]))
            image_14 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[13])).scale(0.8).move_to(np.array([6,1,0]))
            image_15 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[14])).scale(0.8).move_to(np.array([-6,-1,0]))
            image_16 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[15])).scale(0.8).move_to(np.array([-4,-1,0]))
            image_17 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[16])).scale(0.8).move_to(np.array([-2,-1,0]))
            image_18 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[17])).scale(0.8).move_to(np.array([0,-1,0]))
            infinity_war = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[18])).scale(0.8).move_to(np.array([2,-1,0]))
            image_20 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[19])).scale(0.8).move_to(np.array([4,-1,0]))
            image_21 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[20])).scale(0.8).move_to(np.array([6,-1,0]))
            end_game = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[21])).scale(0.8).move_to(np.array([-1,-3,0]))
            image_23 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[22])).scale(0.8).move_to(np.array([1,-3,0]))

            images = [image_1,image_2,image_3,image_4,image_5,image_6,
                    image_7,image_8,image_9,image_10,image_11,image_12,
                    image_13,image_14,image_15,image_16,image_17,image_18,
                    infinity_war,image_20,image_21,end_game,image_23]

            text_2 = TextMobject("2008").scale(0.4)
            text_3 = TextMobject("2010").scale(0.4)
            text_4 = TextMobject("2011").scale(0.4)
            text_5 = TextMobject("2011").scale(0.4)
            text_6 = TextMobject("2012").scale(0.4)
            text_7 = TextMobject("2013").scale(0.4)
            text_8 = TextMobject("2013").scale(0.4)
            text_9 = TextMobject("2014").scale(0.4)
            text_10 = TextMobject("2014").scale(0.4)
            text_11 = TextMobject("2015").scale(0.4)
            text_12 = TextMobject("2015").scale(0.4)
            text_13 = TextMobject("2016").scale(0.4)
            text_14 = TextMobject("2016").scale(0.4)
            text_15 = TextMobject("2017").scale(0.4)
            text_16 = TextMobject("2017").scale(0.4)
            text_17 = TextMobject("2017").scale(0.4)
            text_18 = TextMobject("2018").scale(0.4)
            text_19 = TextMobject("2018").scale(0.4)
            text_20 = TextMobject("2018").scale(0.4)
            text_21 = TextMobject("2019").scale(0.4)
            text_22 = TextMobject("2019").scale(0.4)
            text_23 = TextMobject("2019").scale(0.4)

            text_2.next_to(image_2,np.array([0,-0.2,0]))
            text_3.next_to(image_3,np.array([0,-0.2,0]))
            text_4.next_to(image_4,np.array([0,-0.2,0]))
            text_5.next_to(image_5,np.array([0,-0.2,0]))
            text_6.next_to(image_6,np.array([0,-0.2,0]))
            text_7.next_to(image_7,np.array([0,-0.2,0]))
            text_8.next_to(image_8,np.array([0,-0.2,0]))
            text_9.next_to(image_9,np.array([0,-0.2,0]))
            text_10.next_to(image_10,np.array([0,-0.2,0]))
            text_11.next_to(image_11,np.array([0,-0.2,0]))
            text_12.next_to(image_12,np.array([0,-0.2,0]))
            text_13.next_to(image_13,np.array([0,-0.2,0]))
            text_14.next_to(image_14,np.array([0,-0.2,0]))
            text_15.next_to(image_15,np.array([0,-0.2,0]))
            text_16.next_to(image_16,np.array([0,-0.2,0]))
            text_17.next_to(image_17,np.array([0,-0.2,0]))
            text_18.next_to(image_18,np.array([0,-0.2,0]))
            text_19.next_to(infinity_war,np.array([0,-0.2,0]))
            text_20.next_to(image_20,np.array([0,-0.2,0]))
            text_21.next_to(image_21,np.array([0,-0.2,0]))
            text_22.next_to(end_game,np.array([0,-0.2,0]))
            text_23.next_to(image_23,np.array([0,-0.2,0]))


            text = [text_1,text_2,text_3,text_4,text_5,text_6,
                    text_7,text_8,text_9,text_10,text_11,text_12,
                    text_13,text_14,text_15,text_16,text_17,text_18,
                    text_19,text_20,text_21,text_22,text_23]

            for count in range(1,23):
                    group.add(images[count])
                    group.add(text[count])


            group.remove(infinity_war)
            group.remove(end_game)
            group.add(image_1)

            for count in range(1,23):
                self.play(FadeIn(images[count]),FadeIn(text[count]),run_time=0.2)

class FilmTimeline3(Scene):
        def construct(self):
                films = ["filma","filmb","filmc","filmd","filme","filmf","filmg","filmh","filmi","filmj","filmk","filml","filmm","filmn","filmo","filmp","filmq","filmr","films","filmt","filmu","filmv","filmw"]
                image_1 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[0])).scale(0.8).move_to(np.array([-6,3,0]))
                text_1 = TextMobject("2008").scale(0.4)
                text_1.next_to(image_1,np.array([0,-0.2,0]))
                image_2 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[1])).scale(0.8).move_to(np.array([-4,3,0]))
                image_3 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[2])).scale(0.8).move_to(np.array([-2,3,0]))
                image_4 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[3])).scale(0.8).move_to(np.array([0,3,0]))
                image_5 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[4])).scale(0.8).move_to(np.array([2,3,0]))
                image_6 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[5])).scale(0.8).move_to(np.array([4,3,0]))
                image_7 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[6])).scale(0.8).move_to(np.array([6,3,0]))
                image_8 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[7])).scale(0.8).move_to(np.array([-6,1,0]))
                image_9 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[8])).scale(0.8).move_to(np.array([-4,1,0]))
                image_10 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[9])).scale(0.8).move_to(np.array([-2,1,0]))
                image_11 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[10])).scale(0.8).move_to(np.array([0,1,0]))
                image_12 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[11])).scale(0.8).move_to(np.array([2,1,0]))
                image_13 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[12])).scale(0.8).move_to(np.array([4,1,0]))
                image_14 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[13])).scale(0.8).move_to(np.array([6,1,0]))
                image_15 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[14])).scale(0.8).move_to(np.array([-6,-1,0]))
                image_16 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[15])).scale(0.8).move_to(np.array([-4,-1,0]))
                image_17 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[16])).scale(0.8).move_to(np.array([-2,-1,0]))
                image_18 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[17])).scale(0.8).move_to(np.array([0,-1,0]))
                infinity_war = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[18])).scale(0.8).move_to(np.array([2,-1,0]))
                image_20 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[19])).scale(0.8).move_to(np.array([4,-1,0]))
                image_21 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[20])).scale(0.8).move_to(np.array([6,-1,0]))
                end_game = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[21])).scale(0.8).move_to(np.array([-1,-3,0]))
                image_23 = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[22])).scale(0.8).move_to(np.array([1,-3,0]))

                images = [image_1,image_2,image_3,image_4,image_5,image_6,
                        image_7,image_8,image_9,image_10,image_11,image_12,
                        image_13,image_14,image_15,image_16,image_17,image_18,
                        infinity_war,image_20,image_21,end_game,image_23]

                text_2 = TextMobject("2008").scale(0.4)
                text_3 = TextMobject("2010").scale(0.4)
                text_4 = TextMobject("2011").scale(0.4)
                text_5 = TextMobject("2011").scale(0.4)
                text_6 = TextMobject("2012").scale(0.4)
                text_7 = TextMobject("2013").scale(0.4)
                text_8 = TextMobject("2013").scale(0.4)
                text_9 = TextMobject("2014").scale(0.4)
                text_10 = TextMobject("2014").scale(0.4)
                text_11 = TextMobject("2015").scale(0.4)
                text_12 = TextMobject("2015").scale(0.4)
                text_13 = TextMobject("2016").scale(0.4)
                text_14 = TextMobject("2016").scale(0.4)
                text_15 = TextMobject("2017").scale(0.4)
                text_16 = TextMobject("2017").scale(0.4)
                text_17 = TextMobject("2017").scale(0.4)
                text_18 = TextMobject("2018").scale(0.4)
                text_19 = TextMobject("2018").scale(0.4)
                text_20 = TextMobject("2018").scale(0.4)
                text_21 = TextMobject("2019").scale(0.4)
                text_22 = TextMobject("2019").scale(0.4)
                text_23 = TextMobject("2019").scale(0.4)

                text_2.next_to(image_2,np.array([0,-0.2,0]))
                text_3.next_to(image_3,np.array([0,-0.2,0]))
                text_4.next_to(image_4,np.array([0,-0.2,0]))
                text_5.next_to(image_5,np.array([0,-0.2,0]))
                text_6.next_to(image_6,np.array([0,-0.2,0]))
                text_7.next_to(image_7,np.array([0,-0.2,0]))
                text_8.next_to(image_8,np.array([0,-0.2,0]))
                text_9.next_to(image_9,np.array([0,-0.2,0]))
                text_10.next_to(image_10,np.array([0,-0.2,0]))
                text_11.next_to(image_11,np.array([0,-0.2,0]))
                text_12.next_to(image_12,np.array([0,-0.2,0]))
                text_13.next_to(image_13,np.array([0,-0.2,0]))
                text_14.next_to(image_14,np.array([0,-0.2,0]))
                text_15.next_to(image_15,np.array([0,-0.2,0]))
                text_16.next_to(image_16,np.array([0,-0.2,0]))
                text_17.next_to(image_17,np.array([0,-0.2,0]))
                text_18.next_to(image_18,np.array([0,-0.2,0]))
                text_19.next_to(infinity_war,np.array([0,-0.2,0]))
                text_20.next_to(image_20,np.array([0,-0.2,0]))
                text_21.next_to(image_21,np.array([0,-0.2,0]))
                text_22.next_to(end_game,np.array([0,-0.2,0]))
                text_23.next_to(image_23,np.array([0,-0.2,0]))


                text = [text_1,text_2,text_3,text_4,text_5,text_6,
                        text_7,text_8,text_9,text_10,text_11,text_12,
                        text_13,text_14,text_15,text_16,text_17,text_18,
                        text_19,text_20,text_21,text_22,text_23]

                group = Group()

                for count in range(0,23):
                        group.add(images[count])
                        group.add(text[count])
                        self.add(images[count])
                        self.add(text[count])

                group.remove(infinity_war)
                group.remove(end_game)

                self.play(FadeOut(group))

                self.wait()


class FilmTimeline4(MovingCameraScene):
        def construct(self):
                infinity_war = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films/films.png").scale(0.8).move_to(np.array([2,-1,0]))
                end_game = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films/filmv.png").scale(0.8).move_to(np.array([-1,-3,0]))
                self.add(infinity_war)
                self.add(end_game)
                path_1 = Line(np.array([2,-1,0]),np.array([-1,0,0]))
                path_2 = Line(np.array([-1,-3,0]),np.array([1,0,0]))

                self.play(
                MoveAlongPath(infinity_war, path_1),
                MoveAlongPath(end_game, path_2),
                self.camera_frame.scale,0.4,
                self.camera_frame.move_to,ORIGIN
                )

class FilmTimeline5(MovingCameraScene):
        def construct(self):
                infinity_war = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films/films.png").scale(0.8).move_to(np.array([-1,0,0]))
                end_game = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films/filmv.png").scale(0.8).move_to(np.array([1,0,0]))
                self.add(infinity_war)
                self.add(end_game)

                text_1 = TextMobject("149 mins").next_to(infinity_war,np.array([0,-0.5,0])).scale(0.4)
                text_2 = TextMobject("181 mins").next_to(end_game,np.array([0,-0.5,0])).scale(0.4)

                self.play(
                self.camera_frame.scale,0.4,
                self.camera_frame.move_to,ORIGIN,
                )

                self.wait()

                self.play(Write(text_1))

                self.wait()

                self.play(Write(text_2))

                self.wait()

                self.play(
                FadeOut(infinity_war),
                FadeOut(end_game),
                FadeOut(text_1),
                FadeOut(text_2)
                )
