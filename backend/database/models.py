from database.connection import db

# Model for Domestic Packages

class Domestic_Package(db.Model):
    __tablename__ = 'domestic_packages'

    package_id = db.Column(db.String(20), primary_key=True)
    package_name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    cities_covered = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    hotel_category = db.Column(db.String(50))
    meals = db.Column(db.String(255))
    transportation = db.Column(db.String(255))
    major_attractions = db.Column(db.Text)
    activities = db.Column(db.Text)
    package_type = db.Column(db.String(100))
    best_for = db.Column(db.String(255))
    rating = db.Column(db.Numeric(2, 1))
    estimated_cost = db.Column(db.Numeric(10, 2))

    created_at = db.Column(
        db.DateTime, 
        server_default=db.func.current_timestamp(),
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_on_update=db.func.current_timestamp()
    )

    def to_dict(self):
        return {
            "package_id": self.package_id,
            "package_name": self.package_name,
            "country": self.country,
            "cities_covered": self.cities_covered,
            "duration": self.duration,
            "hotel_category": self.hotel_category,
            "meals": self.meals,
            "transportation": self.transportation,
            "major_attractions": self.major_attractions,
            "activities": self.activities,
            "package_type": self.package_type,
            "best_for": self.best_for,
            "rating": float(self.rating) if self.rating is not None else None,
            "estimated_cost": float(self.estimated_cost) if self.estimated_cost is not None else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# Model for International Packages

class International_Package(db.Model):
    __tablename__ = 'international_packages'

    package_id = db.Column(db.String(20), primary_key=True)
    package_name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    cities_covered = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    hotel_category = db.Column(db.String(50))
    meals = db.Column(db.String(255))
    transportation = db.Column(db.String(255))
    major_attractions = db.Column(db.Text)
    activities = db.Column(db.Text)
    package_type = db.Column(db.String(100))
    best_for = db.Column(db.String(255))
    rating = db.Column(db.Numeric(2, 1))
    estimated_cost = db.Column(db.Numeric(10, 2))

    created_at = db.Column(
        db.DateTime, 
        server_default=db.func.current_timestamp(),
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_on_update=db.func.current_timestamp()
    )

    def to_dict(self):
        return {
            "package_id": self.package_id,
            "package_name": self.package_name,
            "country": self.country,
            "cities_covered": self.cities_covered,
            "duration": self.duration,
            "hotel_category": self.hotel_category,
            "meals": self.meals,
            "transportation": self.transportation,
            "major_attractions": self.major_attractions,
            "activities": self.activities,
            "package_type": self.package_type,
            "best_for": self.best_for,
            "rating": float(self.rating) if self.rating is not None else None,
            "estimated_cost": float(self.estimated_cost) if self.estimated_cost is not None else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

