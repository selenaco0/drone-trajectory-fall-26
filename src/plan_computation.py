import typing as T
import math

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import (
    compute_image_footprint_on_surface,
    compute_ground_sampling_distance,
)


def compute_distance_between_images(
    camera: Camera, dataset_spec: DatasetSpec
) -> tuple[float, float]:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        The horizontal and vertical distance between images (in meters).
    """
    footprintx, footprinty = compute_image_footprint_on_surface(camera, dataset_spec.height)

    distance_hori = (1 - dataset_spec.overlap) * footprintx
    distance_vert = (1 - dataset_spec.sidelap) * footprinty

    return distance_hori, distance_vert

def compute_speed_during_photo_capture(
    camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1
) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.
        allowed_movement_px: The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        The speed at which the drone should move during photo capture.
    """
    gsd = compute_ground_sampling_distance(camera, dataset_spec.height)
    ground_movement = gsd * allowed_movement_px
    time = dataset_spec.exposure_time_ms / 1000.0

    speed = ground_movement / time

    return speed


def generate_photo_plan_on_grid(
    camera: Camera, dataset_spec: DatasetSpec
) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        Scan plan as a list of waypoints.

    """
    distance_hori, distance_vert = compute_distance_between_images(camera, dataset_spec) # Part 1: Compute the maximum distance between two images.

    num_images_hori = math.ceil(dataset_spec.scan_dimension_x / distance_hori) # Part 2: Layer the images such that they cover the whole scan area.
    num_images_vert = math.ceil(dataset_spec.scan_dimension_y / distance_vert)

    spacing_hori = dataset_spec.scan_dimension_x / num_images_hori
    spacing_vert = dataset_spec.scan_dimension_y / num_images_vert

    positions_hori = []
    for i in range(num_images_hori):
        positions_hori.append((i + 0.5) * spacing_hori) # Center is (i * spacing_x + (i+1) * spacing_x) / 2
    positions_vert = []
    for j in range(num_images_vert):
        positions_vert.append((j + 0.5) * spacing_vert)

    speed = compute_speed_during_photo_capture(camera, dataset_spec) # Part 3: Assign the speed to each waypoint.

    waypoints = []
    for row_position in range(len(positions_vert)):
        y = positions_vert[row_position]
        if row_position % 2 == 0:
            row_hori = positions_hori
        else:
            row_hori = list(reversed(positions_hori))
        for x in row_hori:
            waypoints.append(Waypoint(x=x, y=y, z=dataset_spec.height, speed=speed))

    return waypoints
