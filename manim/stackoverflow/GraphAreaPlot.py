from manim import *

# https://stackoverflow.com/questions/71209521/plotting-area-betwwn-implicit-curves

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 4], y_range=[-1.5, 1.5])

        curve_1 = ax.plot_implicit_curve(lambda x, y: y**2-x+1, color=BLUE)
        curve_2 = ax.plot_implicit_curve(lambda x, y: y**2+x-3,  color=GREEN)

        area = ax.get_area(curve_2, (1, 3), bounded_graph=curve_1, color=GREY, opacity=0.5)
        dA = ax.get_riemann_rectangles(
             curve_1, bounded_graph=curve_2, y_range=[-1, 1], dy=0.2, color=RED, fill_opacity=0.5)

        self.add(ax, curve_1, curve_2, area, dA)