from manim import *

# manim profile-picture.py -qm ProfilePicture
class ProfilePicture(Scene):
    def construct(self):
        circle = Circle(radius=4, color="#FF1A1A").set_opacity(1)
        capital_a = Text("A", color="#240CFF", font="Futura").scale(3)

        self.add(circle, capital_a)
