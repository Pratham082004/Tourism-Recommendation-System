from flask import blueprint

from controller.health_controller import(
    home,
    is_healthy
)

health_bp = blueprint("health", __name__)

health_bp.route("/", methods=["GET"])(home)
health_bp.route("/health", methods=["GET"])(is_healthy)
