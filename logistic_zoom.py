from big_ol_pile_of_manim_imports import *
import math

class PopulationModel(GraphScene,MovingCameraScene):

    CONFIG = {
        "y_max" : 15,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "x_tick_frequency" : 20,
        "y_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$N(t)$",
        "graph_origin": 3 * DOWN + 4.5 * LEFT,
        "y_labeled_nums" : [12],
        "x_labeled_nums" : [0,20,40,60,80,100,120],
        }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.camera_frame.save_state()
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (12*7.5*math.exp(0.05*x))/(12-7.5+7.5*math.exp(0.05*x)), color = GREEN)

        graph2 = self.get_graph(lambda x : 12, color = GREEN)
        line = DashedLine(self.input_to_graph_point(0,graph2),self.input_to_graph_point(110,graph2)).set_color(YELLOW)

        vert_line = self.get_vertical_line_to_graph(110,graph,DashedLine,color=YELLOW)

        dot_at_start_graph=Dot().move_to(graph.points[0])

        self.play(
            ShowCreation(graph),
            run_time = 4
        )
        self.wait()

        self.play(
            self.camera_frame.scale,.5,
            self.camera_frame.move_to,dot_at_start_graph,
        )

        self.wait(2)

        self.play(Restore(self.camera_frame))

        self.play(FadeIn(line),FadeIn(vert_line),run_time=2)

        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

class PopulationModel2(GraphScene,MovingCameraScene):

    CONFIG = {
        "y_max" : 15,
        "y_min" : 0,
        "x_max" : 160,
        "x_min" : 0,
        "x_tick_frequency" : 20,
        "y_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$N(t)$",
        "graph_origin": 3 * DOWN + 4.5 * LEFT,
        "y_labeled_nums" : [12],
        "x_labeled_nums" : [0,20,40,60,80,100,120,140,160],
        }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.camera_frame.save_state()
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (12*7.5*math.exp(0.05*x))/(12-7.5+7.5*math.exp(0.05*x)), color = GREEN)
        graph2 = self.get_graph(lambda x : (12*3.75*math.exp(0.05*(x)))/(12-3.75+3.75*math.exp(0.05*(x))), color = RED)

        self.play(
            FadeIn(graph)
        )
        self.wait()
        self.play(
            ShowCreation(graph2),
            run_time = 4
        )

        self.wait()

        graph3 = self.get_graph(lambda x : 12, color = GREEN)

        line = DashedLine(self.input_to_graph_point(0,graph3),self.input_to_graph_point(150,graph3)).set_color(YELLOW)

        vert_line1 = self.get_vertical_line_to_graph(110,graph,DashedLine,color=YELLOW)
        vert_line2 = self.get_vertical_line_to_graph(150,graph,DashedLine,color=YELLOW)

        self.play(FadeIn(line),FadeIn(vert_line1),FadeIn(vert_line2),run_time=2)

        dot_in_graph=Dot().move_to(self.coords_to_point(130,(12*7.5*math.exp(0.05*130))/(12-7.5+7.5*math.exp(0.05*130))))

        self.play(
            self.camera_frame.scale,.25,
            self.camera_frame.move_to,dot_in_graph,
        )
        self.wait(1)
        self.play(
            Restore(self.camera_frame)
        )
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class PopulationModel3(GraphScene):

    CONFIG = {
        "y_max" : 15,
        "y_min" : 0,
        "x_max" : 350,
        "x_min" : 0,
        "x_tick_frequency" : 50,
        "y_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$N(t)$",
        "graph_origin": 3 * DOWN + 4.5 * LEFT,
        "y_labeled_nums" : [12],
        "x_labeled_nums" : [0,50,100,150,200,250,300,350],
        }

    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (12*7.5*math.exp(0.05*x))/(12-7.5+7.5*math.exp(0.05*x)), color = GREEN,x_min=0,x_max=110)
        graph2 = self.get_graph(lambda x : (12*6*math.exp(0.05*(x-110)))/(12-6+6*math.exp(0.05*(x-110))), color = RED,x_min=110,x_max=230)
        graph3 = self.get_graph(lambda x : (12*6*math.exp(0.05*(x-230)))/(12-6+6*math.exp(0.05*(x-230))), color = BLUE,x_min=230,x_max=350)

        vert_line1 = self.get_vertical_line_to_graph(110,graph,DashedLine,color=YELLOW)
        vert_line2 = self.get_vertical_line_to_graph(230,graph,DashedLine,color=YELLOW)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.play(FadeIn(vert_line1))
        self.play(
            ShowCreation(graph2),
            run_time = 2
        )
        self.play(FadeIn(vert_line2))
        self.play(
            ShowCreation(graph3),
            run_time = 2
        )

        self.play(*[FadeOut(mob)for mob in self.mobjects])
