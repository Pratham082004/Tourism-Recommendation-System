"""
Application entry point for the Tourism Recommendation System.

Configures the Flask application, initializes extensions,
registers API blueprints, initializes the database,
and starts the development server.
"""

from flask import Flask
from flask_cors import CORS
import time

from config import Config
from database.connection import db

from services.database_initializer import Database_Initializer

from utils.logger import logger

from routes.health_routes import health_bp
from routes.package_routes import package_bp
from routes.recommendation_routes import recommendation_bp
from routes.attraction_routes import attraction_bp


def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(package_bp)
    app.register_blueprint(recommendation_bp)
    app.register_blueprint(attraction_bp)

    with app.app_context():
        max_retries = 10
        retry_delay = 3  

        for attempt in range(1, max_retries + 1):
            try:
                db.engine.connect()
                logger.info("Database connection successful.")

                Database_Initializer.initialize()
                logger.info("Database initialized successfully.")

                break

            except Exception:
                logger.warning(
                    f"Database connection failed "
                    f"(Attempt {attempt}/{max_retries}). "
                    f"Retrying in {retry_delay} seconds..."
                )

                if attempt == max_retries:
                    logger.error(
                        "Failed to connect to the database after "
                        f"{max_retries} attempts.",
                        exc_info=True,
                    )
                else:
                    time.sleep(retry_delay)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=True,
        use_reloader=False,
    )