"""
Repository layer for package data access.

Provides methods to query domestic and international package records using the
SQLAlchemy models.
"""

from database.models import Domestic_Package, International_Package
from utils.logger import logger


class PackageRepository:

    """Data access layer for extracting travel packages from the database. """
    @staticmethod
    def get_all_domestic_packages():
        logger.debug("Repository: get_all_domestic_packages")
        return Domestic_Package.query.all()

    @staticmethod
    def get_domestic_package_by_id(package_id):
        logger.debug("Repository: get_domestic_package_by_id id=%s", package_id)
        return Domestic_Package.query.filter_by(package_id=package_id).first()

    @staticmethod
    def get_all_international_packages():
        logger.debug("Repository: get_all_international_packages")
        return International_Package.query.all()

    @staticmethod
    def get_international_package_by_id(package_id):
        logger.debug("Repository: get_international_package_by_id id=%s", package_id)
        return International_Package.query.filter_by(package_id=package_id).first()

    


