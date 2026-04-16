
from sqlalchemy.orm import Session
from backend import models, schemas

class PolicyService:
    def create_policy(self, db: Session, policy: schemas.Policy):
        db_policy = models.Policy(
            customer_id=policy.customer.id,
            vehicle_id=policy.vehicle.id,
            base_premium=policy.base_premium,
            ncb_years=policy.ncb_years,
            ncb_discount_percentage=policy.ncb_discount_percentage,
            vehicle_multiplier=policy.vehicle_multiplier,
            final_premium=policy.final_premium,
        )
        db.add(db_policy)
        db.commit()
        db.refresh(db_policy)
        return db_policy
