from manim import *

# manim profile-picture.py -qm ProfilePicture
class ProfilePicture(Scene):
    def construct(self):
        circle_with_a = VGroup(Circle(radius=2, color="#FF1A1A").set_opacity(1), Text("A", color="#240CFF", font="Futura").scale(3.5)).move_to([-1,1.5,0]).scale(0.5)

        lex = Text("lex", color="#240CFF", font="Futura").scale(2).next_to(circle_with_a, RIGHT, buff=0.15)

        the = Text("the", color=ORANGE, font="Futura").scale(1.5).next_to(VGroup(circle_with_a, lex), DOWN).shift(0.4*RIGHT+0.2*UP)

        man = Text("MAN", color=YELLOW, font="Futura").scale(2).next_to(the, DOWN).shift(0.2*LEFT+0.1*DOWN)

        self.add(
            # NumberPlane(axis_config={"include_numbers":True}), 
            circle_with_a, 
            lex, 
            the, 
            man)
