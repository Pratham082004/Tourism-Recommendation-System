"""
Service layer for package-related operations.

Exposes methods used by controllers to Retrieves domestic and international package
data from the repository layer and convert models to serializable dicts.
"""

from repositories.package_repository import PackageRepository
from utils.logger import logger


class PackageService:

    """Service layer for travel packages."""

    @staticmethod
    def get_all_domestic_packages():
        """Retrieves all domestic packages and return them as dicts."""
        logger.debug("PackageService: get_all_domestic_packages")
        packages = PackageRepository.get_all_domestic_packages()
        result = [package.to_dict() for package in packages]
        logger.info("PackageService: domestic packages=%s", len(result))
        return result


    @staticmethod
    def get_domestic_package_by_id(package_id):
        """ Retrieves a domestic package by its ID. """
        logger.debug("PackageService: get_domestic_package_by_id id=%s", package_id)
        package = PackageRepository.get_domestic_package_by_id(package_id)
        return package.to_dict() if package else None


    @staticmethod
    def get_all_international_packages():
        """Retrieves all international packages and return them as dicts."""
        logger.debug("PackageService: get_all_international_packages")
        packages = PackageRepository.get_all_international_packages()
        result = [package.to_dict() for package in packages]
        logger.info("PackageService: international packages=%s", len(result))
        return result


    @staticmethod
    def get_international_package_by_id(package_id):
        """Retrieves an international package by its ID."""
        logger.debug("PackageService: get_international_package_by_id id=%s", package_id)
        package = PackageRepository.get_international_package_by_id(package_id)
        return package.to_dict() if package else None


