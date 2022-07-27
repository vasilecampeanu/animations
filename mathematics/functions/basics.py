from manim import *

class AxesExample(Scene):
    def construct(self):
        axes = Axes(
            x_range  = [-5, 5],
            y_range  = [-5, 5],
            x_length = 6,
            y_length = 6
        ).add_coordinates()
        
        self.play(Write(axes))
        
        return super().construct()

class PlotFunctionByDots(Scene):
    def construct(self):
        axes = Axes(
            x_range     = [0, 10],
            y_range     = [0, 10],
            x_length    = 6, 
            y_length    = 6,
            axis_config = {"include_tip": False}
        )
        
        k = 25

        function_plot = axes.plot(
            lambda x: k / x,
            color = YELLOW_D,
            x_range = [k / 10, 10, 0.001],
            use_smoothing = False,
        )

        point01 = function_plot.get_point_from_function(2.5)
        dot01 = Dot(point01)
        lines_to_point01 = axes.get_lines_to_point(point01)

        point02 = function_plot.get_point_from_function(5)
        dot02 = Dot(point02)
        lines_to_point02 = axes.get_lines_to_point(point02)

        point03 = function_plot.get_point_from_function(7)
        dot03 = Dot(point03)
        lines_to_point03 = axes.get_lines_to_point(point03)

        point04 = function_plot.get_point_from_function(10)
        dot04 = Dot(point04)
        lines_to_point04 = axes.get_lines_to_point(point04)

        function_dots = VGroup(dot01, dot02, dot03, dot04)
        dots_lines = VGroup(lines_to_point01, lines_to_point02, lines_to_point03, lines_to_point04)

        self.play(Write(axes))
        self.wait()
        self.play(Write(function_dots))
        self.wait()
        self.play(Write(dots_lines))
        self.wait()
        self.play(Write(function_plot))
        self.wait()

        return super().construct()
