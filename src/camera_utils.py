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
    X, Y, Z = world_point

    if Z <= 0:
        raise ValueError

    x = camera.fx * X / Z 
    y = camera.fy * Y / Z

    return (x, y)

def backproject_image_point_to_world(camera: Camera, image_point: tuple[float, float], distance: float) -> tuple[float, float, float]:
    """Backproject an image point to a 3D world point.

    Args:
        camera: the camera model
        image_point: the image point
        distance: the distance from the surface

    Returns:
        (X, Y, Z) world coordinates.
    """
    x, y = image_point

    if distance <= 0:
        raise ValueError

    Z = distance
    X = Z * x / camera.fx
    Y = Z * y / camera.fy

    return (X, Y, Z)

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
    if distance_from_surface <= 0:
        raise ValueError
    
    footprint_x = distance_from_surface * camera.num_pixels_x / camera.fx
    footprint_y = distance_from_surface * camera.num_pixels_y / camera.fy

    return (footprint_x, footprint_y)


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
    if distance_from_surface <= 0:
        raise ValueError

    footprint_x = distance_from_surface * camera.num_pixels_x / camera.fx
    footprint_y = distance_from_surface * camera.num_pixels_y / camera.fy

    gsd_x = footprint_x / camera.num_pixels_x
    gsd_y = footprint_y / camera.num_pixels_y

    return min(gsd_x, gsd_y)
