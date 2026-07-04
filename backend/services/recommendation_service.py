"""
Service layer for orchestracting recommendataion.

It acts as the core logic layer which evaluates user input parameters
and routes data to the appropriate specialised ml inference engine(Domestic or International).
"""

from pathlib import Path

from database.models import International_Package, Domestic_Package
from ml.domestic.recommend import Domestic_Recommendation_Engine
from ml.International.recommend import International_Recommendation_Engine
from utils.logger import logger


_PROJECT_ROOT = Path(__file__).resolve().parents[1]

class recommendation_service:
    """
    Recommendation service class used for managing and routing recommendation services.
    """

    domestic_engine = Domestic_Recommendation_Engine(str(_PROJECT_ROOT / "ml" / "domestic" / "models" / "domestic_model.pkl"))  # domestic model path

    international_engine = International_Recommendation_Engine(str(_PROJECT_ROOT / "ml" / "International" / "models" / "international_model.pkl"))  # international model path


    @staticmethod
    def recommend(user):
        """ Function used to generate package recommendation by routing the request to the correct ml engine. """
        destination_type = user.get("destination_type").lower()
        logger.info("Recommendation requested destination_type=%s", destination_type)


        if destination_type == "domestic":
            recommendations = recommendation_service.domestic_engine.recommend(user, top_k = 5)
            logger.debug("Domestic engine recommendations size=%s", len(recommendations) if recommendations else 0)
            if not recommendations:
                return[]
            
            ids = [item["package_id"]for item in recommendations]


            packages = Domestic_Package.query.filter(Domestic_Package.package_id.in_(ids)).all()

            package_map = {package.package_id: package for package in packages}
            
            ordered_package = []

            for item in recommendations:
                package = package_map.get(item["package_id"])
                if package:
                    data = package.to_dict()
                    data["score"] = float(item["score"])
                    ordered_package.append(data)
            logger.info("Domestic recommendation result size=%s", len(ordered_package))
            
            return ordered_package


        elif destination_type == "international":
            recommendations = recommendation_service.international_engine.recommend(user, top_k = 5)
            logger.debug("International engine recommendations size=%s", len(recommendations) if recommendations else 0)
            if not recommendations:
                return[]
            
            ids = [item["package_id"]for item in recommendations]


            packages = International_Package.query.filter(International_Package.package_id.in_(ids)).all()

            package_map = {package.package_id: package for package in packages}
            
            ordered_package = []

            for item in recommendations:
                package = package_map.get(item["package_id"])
                if package:
                    data = package.to_dict()
                    data["score"] = float(item["score"])
                    ordered_package.append(data)
            logger.info("International recommendation result size=%s", len(ordered_package))
            
            return ordered_package

        else:
            return []

            