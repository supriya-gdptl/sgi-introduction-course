import numpy as np
import polyscope as ps


# This function computes a trivial parameterization of a single triangle using the technique described above.
def trivial_parameterization(triangle):
    # Local basis origin is the first triangle vertex
    origin = triangle[0]

    # Get the normal of the plane defined by the triangle
    e1 = triangle[1] - origin
    e2 = triangle[2] - origin
    normal = np.cross(e1, e2)
    normal /= np.linalg.norm(normal)

    # We will use e1 as the first basis. Second basis will be cross between e1 and the normal
    basis1 = e1 / np.linalg.norm(e1)
    basis2 = np.cross(normal, basis1)
    basis2 /= np.linalg.norm(basis2)

    # First vertex is the origin. Project the other two vertices onto the local bases.
    uv0 = np.array([0,0])
    uv1 = np.array([np.dot(e1, basis1), np.dot(e1, basis2)])
    uv2 = np.array([np.dot(e2, basis1), np.dot(e2, basis2)])

    return np.array([uv0, uv1, uv2]), origin, basis1, basis2

# Define a triangle and compute its trivial parameterization
triangle = np.array([[5.1, 2.8, 9.9],
                     [-1, 8, 2.3],
                     [8, 4.4, 6.7]])

uvs, origin, basis1, basis2 = trivial_parameterization(triangle)

ps.init()
ps.remove_all_structures()
ps.register_surface_mesh("single tri", triangle, np.array([[0,1,2]]), edge_width=1, color = (0.1, 0.2, 1))
ps.register_curve_network("basis1", np.array([origin, origin + basis1]), np.array([[0,1]]), radius=0.01, color=(1, 0, 0))
ps.register_curve_network("basis2", np.array([origin, origin + basis2]), np.array([[0,1]]), radius=0.01, color=(0, 0, 1))
ps.register_surface_mesh("uv tri", uvs, np.array([[0,1,2]]), edge_width=1, color = (0.2, 1, 0.2))
ps.reset_camera_to_home_view()
ps.show()

