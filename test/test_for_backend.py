from build123d import *
from ocp_vscode import *

set_port(3939)
set_defaults(reset_camera=Camera.KEEP, ortho=True)

with BuildPart() as p:
    Box(10, 10, 10)
    with Locations((5, 0, 0)):
        Box(10, 10, 5)
c = Circle(10).edge()
c.normal()
pass
# line = line.edges()[0]
# show(p, f1, f2)
