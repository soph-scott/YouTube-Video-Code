from big_ol_pile_of_manim_imports import *
import math

class PopulationModel(GraphScene):

    CONFIG = {
        "y_max" : 15,
        "y_min" : 0,
        "x_max" : 100,
        "x_min" : 0,
        "x_tick_frequency" : 20,
        "y_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$N(t)$",
        "graph_origin": 3 * DOWN + 4.5 * LEFT,
        "y_labeled_nums" : [8,12],
        "x_labeled_nums" : [0,20,40,60,80,100],
        }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (12*7.9*math.exp(0.05*x))/(12-7.9+7.9*math.exp(0.05*x)), color = GREEN)
        vert_line = self.get_vertical_line_to_graph(80,graph,color=YELLOW)

        self.play(
            ShowCreation(graph),
            run_time = 4
        )
        self.wait()
        self.play(ShowCreation(vert_line))
