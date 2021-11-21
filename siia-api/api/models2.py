from sqlalchemy.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import CHAR, Date, Float
from sqlalchemy.types import Boolean, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Schools(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(100), nullable=False)

class Careers(db.Model): #Revisar nombre
    school = Column("school", ForeignKey(Schools.id),primary_key=True)
    career_id = Column("id",Integer,primary_key=True)
    name = Column("name",String(100), nullable=False)

class Groups(db.Model):
    school = Column("school", ForeignKey(Schools.id),primary_key=True)
    period = Column("period",Integer,nullable=False, primary_key=True)
    group = Column("group",Integer,nullable=False, primary_key=True)

class Curriculums(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(100), nullable=False)

class Students(db.Model):
    account_number = Column("account_number",String(8), primary_key=True)
    nip = Column("NIP",String(32), nullable=False)
    name = Column("name",String(100), nullable=False)
    sex = Column("sex",String(1), nullable=False)
    birthday = Column("birthday",Date, nullable=False)
    admission_date = Column("admission_date",Date, nullable=False)
    street = Column("street",String(50), nullable=False)
    suburb = Column("suburb",String(50), nullable=False)
    postal_code = Column("suburb",String(10), nullable=False)
    city = Column("city",String(50), nullable=False)
    phone = Column("phone",String(10), nullable=False)
    curp = Column("curp",String(18), nullable=False)
    nss = Column("nss",String(20), nullable=True)
    
    # Auth jwt
    jwt_auth_active = Column(Boolean())
    date_joined = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'User {self.account_number}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_nip(self, nip):
        self.nip = generate_password_hash(nip)

    def check_nip(self, nip):
        return check_password_hash(self.nip, nip)

    def update_nip(self, new_nip):
        self.nip = new_nip

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_account_number(cls, account_number):
        return cls.query.filter_by(account_number=account_number).first()

    def toDICT(self):
        return dict(_id=self.id, account_number=self.account_number)

    def toJSON(self):
        return self.toDICT()

class Tutors(db.Model):
    tutor_number = Column("tutor_number",String(8), primary_key=True)
    name = Column("name",String(100), nullable=False)
    street = Column("street",String(50), nullable=False)
    suburb = Column("suburb",String(50), nullable=False)
    postal_code = Column("postal_code",String(10), nullable=False)
    city = Column("city",String(50), nullable=False)
    phone = Column("phone",String(10), nullable=False)

class Validities(db.Model):
    id = Column("id",Integer,primary_key=True)
    validity = Column("validity",CHAR, nullable=False)

class Studies(db.Model): #Revisar nombre
    id = Column("id",Integer,primary_key=True)
    school = Column("school", ForeignKey(Schools.id))
    career = Column("career", ForeignKey(Careers.career_id))
    curriculum = Column("curriculum", ForeignKey(Curriculums.id))
    period = Column("period", ForeignKey(Groups.period))
    group = Column("group", ForeignKey(Groups.group))
    validity = Column("validity", ForeignKey(Validities.id))

class StudiesTypes:
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(25), nullable=False)

class AdmissionTest:
    id = Column("id",Integer,primary_key=True)

class StudentStudies(db.Model):
    id = Column("id",Integer, primary_key=True)
    studies = Column("studies", ForeignKey(Studies.id))
    type = Column("school", ForeignKey(StudiesTypes.id))
    admission_year =  Column("life_time", String(4),nullable=False)
    average = Column("average",Float,nullable=False) #Revisar nombre
    admission_test = Column("admission_test", ForeignKey(AdmissionTest.id))

class SchoolSubjects(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(100), nullable=False)
    curriculum = Column("curriculum", ForeignKey(Curriculums.id))

class TestTypes(db.Model):
    id = Column("id",Integer,primary_key=True)
    short_name = Column("name",String(3), nullable=False)
    name = Column("name",String(20), nullable=False)

class Grades(db.Model):
    school_subject = Column("school_subject", ForeignKey(SchoolSubjects.id))
    grade = Column("grade",Float, default=0, nullable=True) #Pone default 0
    test_type = Column("test_type", ForeignKey(TestTypes.id))
    
class Teachers(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(100), nullable=False)

class WeekDays(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(20), nullable=False)

class Schedules(db.Model):
    school_subject = Column("school_subject", ForeignKey(SchoolSubjects.id))
    school = Column("school_subject", ForeignKey(Schools.id))
    teacher = Column("teacher", ForeignKey(Teachers.id))
    day = Column("day", ForeignKey(WeekDays.id))
    start_hour = Column("hour",String("5"),nullable=False)
    end_hour = Column("hour",String("5"),nullable=False)

class Requests(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",Boolean, nullable=False)

class PaymentStatuses(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(10), nullable=False)

class TaxReceiptStatuses(db.Model):
    id = Column("id",Integer,primary_key=True)
    name = Column("name",String(10), nullable=False)

class Procedures(db.Model):
    id = Column("id",Integer,primary_key=True)
    procedure_date = Column("procedure_date",Date,nullable=False)
    expiration_date = Column("expiration_date",Date,nullable=False)
    requested = Column("requested", ForeignKey(Requests.id))
    rfc = Column("rfc", String(13), nullable=False)
    payment_status = Column("payment_status", ForeignKey(PaymentStatuses.id))
    tax_receipt_status = Column("payment_status", ForeignKey(TaxReceiptStatuses.id))
    amount = Column("amount",Float,nullable=False)

class JWTTokenBlocklist(db.Model):
    id = Column(Integer, primary_key=True)
    jwt_token = Column(String(), nullable=False)
    created_at = Column(DateTime(), nullable=False)

    def __repr__(self):
        return f'Expired Token: {self.jwt_token}'

    def save(self):
        db.session.add(self)
        db.session.commit()

if __name__ == '__main__':
    db.create_all()