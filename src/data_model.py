"""Data models for the camera and user specification."""

from dataclasses import dataclass


@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """

    overlap: float  # Overlap between consecutive images. Range: (0, 1)
    sidelap: float  # Overlap between images in consecutive rows. Range: (0, 1)
    height: float  # Height above ground, in meters.
    scan_dimension_x: float  # The dimension of scan area in x-direction (meters)
    scan_dimension_y: float  # The dimension of scan area in y-direction (meters)
    exposure_time_ms: float  # Exposure time in milliseconds


@dataclass
class Camera:
    """
    Data model for a simple pinhole camera.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """

    fx: float  # Focal length in the x-direction (pixels)
    fy: float  # Focal length in the y-direction (pixels)
    sensor_size_x_mm: float  # Size of the sensor in x-direction (mm)
    sensor_size_y_mm: float  # Size of the sensor in y-direction (mm)
    num_pixels_x: int  # Number of pixels in x-direction
    num_pixels_y: int  # Number of pixels in y-direction


@dataclass
class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """

    x: float  # x-coordinate of the waypoint
    y: float  # y-coordinate of the waypoint
    z: float  # z-coordinate of the waypoint
    speed: float  # speed of the drone at the waypoint
    
    # Optional: un-comment if bonus section of arbitraty gimbal angle done
    # gimbal_angle_x: float # gimbal angle along the x-axis in radians. 0 means looking straight down.
