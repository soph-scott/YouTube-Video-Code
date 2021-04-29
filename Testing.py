from big_ol_pile_of_manim_imports import *

class ImageTest(Scene):
    def construct(self):
        for x in range(-5, 5):
            group = Group()
            for y in range(-3, 4):
                image = ImageMobject("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/thanos_mini.png").scale(0.5).move_to(np.array([x,y,0]))
                group.add(image)
                self.add(image)
            self.play(FadeIn(group))
#Do for each group and then can play around with groups as can be named specifically (x in for loop replaced by group each time)

count = 1
for y in [3,1,-1,-3]:
    for x in [-6,-4,-2,0,2,4,6]:
        if x == -6 and y == 3:
            continue
        if x == 2 and y == -1:
            infinity_war = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[count])).scale(0.5).move_to(np.array([x,y,0]))
            self.play(infinity_war)
        if x == -6 and y == -3:
            end_game = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[count])).scale(0.5).move_to(np.array([x,y,0]))
            self.play(end_game)
        if x in [-2,0,2,4,6] and y == -3:
            break
        else:
            image = ImageMobject(os.path.join("/Users/sophiescott/Desktop/ManimInstall/manim_3feb/media/designs/raster_images/Films", films[count])).scale(0.5).move_to(np.array([x,y,0]))
            group.add(image)
            self.play(image)
        count = count + 1
