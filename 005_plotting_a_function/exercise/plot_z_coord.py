import gpytoolbox as gpy, polyscope as ps, numpy as np


def plot_z_coord(V,F):
    """This method plots the z-cordinate on the input mesh V,F
    """
    f = V[:,2]
    ps.init()
    ps_spot = ps.register_surface_mesh("spot_zcoord", V, F)
    ps_spot.add_scalar_quantity("zcoord", f, enabled=True)
    ps.show()


V, F = gpy.read_mesh("../data/spot.obj")
plot_z_coord(V, F)
