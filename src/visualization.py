"""Utility to visualize photo plans.
"""

import typing as T

import plotly.graph_objects as go

from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans: List of waypoints for the photo plan.

    Returns:
        Plotly figure object.
    """
    # Scatter plot with connecting lines
    x = [wp.x for wp in photo_plans]
    y = [wp.y for wp in photo_plans]
    speed = [wp.speed for wp in photo_plans]

    fig = go.Figure()

    # Flight path: connects waypoints in order, so the lawn-mower zigzag is visible
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            line=dict(color="lightgray", width=1),
            name="Flight path",
            hoverinfo="skip",
        )
    )

    # Waypoints: one marker per photo capture, colored by speed, numbered in order
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=dict(
                size=8,
                color=speed,
                colorscale="Viridis",
                colorbar=dict(title="Speed (m/s)"),
                showscale=True,
            ),
            text=[f"Waypoint {i}<br>Speed: {s:.2f} m/s" for i, s in enumerate(speed)],
            hoverinfo="text",
            name="Waypoints",
        )
    )

    fig.update_layout(
    title="Photo Plan",
    xaxis_title="X (m)",
    yaxis_title="Y (m)",
    yaxis=dict(scaleanchor="x", scaleratio=1),
    legend=dict(
        orientation="h",       
        yanchor="bottom",
        y=-0.2,               
        xanchor="center",
        x=0.5,
    ))

    return fig
