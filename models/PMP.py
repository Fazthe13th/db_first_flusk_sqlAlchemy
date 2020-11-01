from db import Base, PMPS, db


class PmpModel(Base):

    __tablename__ = 'pmps'

    def __init__(
        self,
        pmp_id=None,
        pop_id=None,
        cell_id=None,
        latitude=None,
        longitude=None,
        division=None,
        district=None,
        thana=None,
        pmp_sectoral=None,
        tx_power=None,
        frequency=None,
        vendor=None,
        antenna_type=None,
        radio_name=None,
        pmp_azimuth=None,
        tower_height_meter=None,
        antenna_height_meter=None,
        created_at=None,
        updated_at=None,
        is_active=None

    ):
        self.pmp_id = pmp_id
        self.pop_id = pop_id
        self.cell_id = cell_id
        self.latitude = latitude
        self.longitude = longitude
        self.division = division
        self.district = district
        self.thana = thana
        self.pmp_sectoral = pmp_sectoral
        self.tx_power = tx_power
        self.frequency = frequency
        self.vendor = vendor
        self.antenna_type = antenna_type
        self.radio_name = radio_name
        self.pmp_azimuth = pmp_azimuth
        self.tower_height_meter = tower_height_meter
        self.antenna_height_meter = antenna_height_meter
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active

    def json(self, user_email, first_name, last_name):
        return {
            'user_email': user_email,
            'first_name': first_name,
            'last_name': last_name
        }

    def find_by_user_email(self, user_email):
        return db.session.query(Users).filter_by(user_email=user_email).first()

    def find_by_user_uuid(self, _user_uuid):
        return db.session.query(Users).filter_by(user_uuid=_user_uuid).first()

    def save_to_db(self):
        new_user = Users(
            user_uuid=self.user_uuid,
            user_email=self.user_email,
            user_password=self.user_password,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=self.is_active
        )
        db.session.add(new_user)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
