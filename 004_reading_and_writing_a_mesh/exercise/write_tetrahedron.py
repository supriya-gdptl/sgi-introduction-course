import numpy as np, gpytoolbox as gpy
import polyscope as ps

def write_tetrahedron():
    """
    Writes a tetrahedron to the file "tetrahedron.obj"
    """
    V = np.array([[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    F = np.array([[1, 0, 2], [0, 1, 3], [1, 2, 3], [2, 0, 3]])
    gpy.write_mesh("tetrahedron.obj", V, F)
    print("saved tetrahedron")

def read_tetrahedron():
    V,F = gpy.read_mesh("tetrahedron.obj")
    ps.init()
    ps.register_surface_mesh("saved_tet", V, F)
    ps.show()

write_tetrahedron()
read_tetrahedron()
