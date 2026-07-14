"""Utility functions for the camera model.
"""

from src.data_model import Camera


def project_world_point_to_image(camera: Camera, world_point: tuple[float, float, float]) -> tuple[float, float]:
    """Project a 3D world point into the image coordinates.

    Args:
        camera: the camera model
        world_point: the 3D world point

    Returns:
        (x, y) image coordinates on the film corresponding to world_point (in pixels).
    """
    raise NotImplementedError()

def backproject_image_point_to_world(camera: Camera, image_point: tuple[float, float], distance: float) -> tuple[float, float, float]:
    """Backproject an image point to a 3D world point.

    Args:
        camera: the camera model
        image_point: the image point
        distance: the distance from the surface

    Returns:
        (X, Y, Z) world coordinates.
    """
    raise NotImplementedError()

def compute_image_footprint_on_surface(
    camera: Camera, distance_from_surface: float
) -> tuple[float, float]:
    """Compute the footprint of the image captured by the camera at a given distance from the surface.

    Args:
        camera: the camera model.
        distance_from_surface: distance from the surface (in m).

    Returns:
        (footprint_x, footprint_y) in meters.
    """
    raise NotImplementedError()


def compute_ground_sampling_distance(
    camera: Camera, distance_from_surface: float
) -> float:
    """Compute the ground sampling distance (GSD) at a given distance from the surface.

    Args:
        camera: the camera model.
        distance_from_surface: distance from the surface (in m).

    Returns:
        The GSD in meters (smaller among x and y directions).
    """
    raise NotImplementedError()
    
