from datetime import datetime

import json

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
db = SQLAlchemy()
    

class JWTTokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jwt_token = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"

    def save(self):
        db.session.add(self)
        db.session.commit()

class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    db.UniqueConstraint(name)


class Career(db.Model):
    __tablename__ = 'careers'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    db.UniqueConstraint(name)
    
    # many to one db.relationship with School
    school_id = db.Column(db.Integer, ForeignKey(School.id))
    school = db.relationship('School')
    
    # one to many db.relationship with Group
    group = db.relationship('Group', back_populates='career')


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column('id', db.Integer, primary_key=True)
    grade = db.Column('grade', db.Integer, nullable=False)
    group = db.Column('group', db.Integer, nullable=False)
    
    # one to many db.relationship with Career
    career_id = db.Column(db.Integer, ForeignKey(Career.id))
    career = db.relationship(Career, back_populates='group')


class Curriculum(db.Model):
    __tablename__ = 'curriculums'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    db.UniqueConstraint(name)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column("id", db.Integer, primary_key=True)
    account_number = db.Column("account_number", db.String(8), nullable=False)
    nip = db.Column("nip", db.String(6), nullable=False)
    first_name = db.Column("first_name", db.String, nullable=False)
    last_name = db.Column("last_name", db.String, nullable=False)
    sex = db.Column("sex", db.String, nullable=False)
    birthday = db.Column("birthday", db.Date, nullable=False)
    admission_date = db.Column("admission_date", db.Date, nullable=False)
    street = db.Column("street", db.String, nullable=False)
    suburb = db.Column("suburb", db.String, nullable=False)
    postal_code = db.Column("postal_code", db.String, nullable=False)
    city = db.Column("city", db.String, nullable=False)
    phone_number = db.Column("phone_number", db.String(10), nullable=False)
    curp = db.Column("curp", db.String(18), nullable=False)
    nss = db.Column("nss", db.String(20), nullable=False)
    db.UniqueConstraint(account_number)
    
    jwt_auth_active = db.Column(db.Boolean())
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"User {self.account_number}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_nip(self, nip):
        self.nip = generate_password_hash(nip)

    def check_nip(self, _account_number, _nip):
        q_param = {'account': _account_number, 'nip': _nip}
        for i in db.session.execute('select * from students where account_number = :account and nip = :nip', params=q_param):
            a = i
        return True if a else False

    def update_nip(self, _new_nip):
        self.nip = _new_nip

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    def folio_query(self, _account_number):
        def json(i):
            return {
                'school_subject': i.school_subject,
                'status_group': i.status_group,
                'status_period': i.status_period,
                'test_type': i.test_type,
                'test_date': i.test_date.strftime('%Y/%m/%d')
            }
        q_param = {'account': _account_number}
        return [json(data) for data in db.session.execute("SELECT * FROM ConsultaFolios(:account)", params=q_param)][0]
    
    def academic_record(self, _account_number):
        def json(i):
            print(i)
            return {
                'school_subject': i.school_subject,
                'grade': i.grade,
                'test_type': i.test_type,
                'test_date': i.test_date.strftime('%Y/%m/%d')
            }
        q_param = {'account': _account_number}
        return [json(data) for data in db.session.execute("SELECT * FROM HistorialAcademico(:account)", params=q_param)][0]
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_account_number(cls, _account_number):
        return cls.query.filter_by(account_number=_account_number).first()

    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['account_number'] = self.account_number

        return cls_dict

    def toJSON(self):

        return self.toDICT()


class Tutor(db.Model):
    __tablename__ = "tutors"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, nullable=False)
    phone_number = db.Column("phone_number", db.String(10), nullable=False)
    street = db.Column("street", db.String, nullable=False)
    suburb = db.Column("suburb", db.String, nullable=False)
    postal_code = db.Column("postal_code", db.String, nullable=False)
    city = db.Column("city", db.String, nullable=False)
    
    # one to many db.relationship with Student
    # NOTE: Tutor de padre? o tutor tutorias
    student_account_number = db.Column(db.String(8), ForeignKey(Student.account_number))
    student = db.relationship(Student)
    

class Validity(db.Model):
    __tablename__ = 'validities'
    id = db.Column('id', db.Integer, primary_key=True)
    validity = db.Column('validity', db.String(1), nullable=False)
    

class Study(db.Model):
    __tablename__ = 'studies'
    id = db.Column('id', db.Integer, primary_key=True)
    
    school_id = db.Column(db.Integer, ForeignKey(School.id))
    school = db.relationship(School)
    career_id = db.Column(db.Integer, ForeignKey(Career.id))
    career = db.relationship(Career)
    curriculum_id = db.Column(db.Integer, ForeignKey(Curriculum.id))
    curriculum = db.relationship(Curriculum)
    group_id = db.Column(db.Integer, ForeignKey(Group.id))
    group = db.relationship(Group)
    validity_id = db.Column(db.Integer, ForeignKey(Validity.id))
    validity = db.relationship(Validity)
    

class StudyType(db.Model):
    __tablename__ = 'studies_types'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)


class AdmissionTest(db.Model):
    __tablename__ = 'admission_tests'
    id = db.Column("id", db.Integer, primary_key=True)
    

class StudenStudy(db.Model):
    __tablename__ = 'student_studies'
    id = db.Column('id', db.Integer, primary_key=True)
    admission_year = db.Column('life_time', db.String(4), nullable=False)
    average = db.Column('average', db.Float, nullable=False)
    
    studies_id = db.Column(db.Integer, ForeignKey(Study.id))
    studies = db.relationship(Study)
    study_type_id = db.Column(db.Integer, ForeignKey(StudyType.id))
    study_type = db.relationship(StudyType)
    admission_test_id = db.Column(db.Integer, ForeignKey(AdmissionTest.id))
    admission_test = db.relationship(AdmissionTest)
        

class SchoolSubject(db.Model):
    __tablename__ = 'school_subjects'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    
    curriculum_id = db.Column(db.Integer, ForeignKey(Curriculum.id))
    curriculum = db.relationship(Curriculum)
    

class TestType(db.Model):
    __tablename__ = 'test_types'
    id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name", db.String(20), nullable=False) 
    

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column("id", db.Integer, primary_key=True)
    grade = db.Column("grade", db.Integer, nullable=False, default=0)
    test_date = db.Column("test_date", db.Date, nullable=False)
    
    school_subject_id = db.Column(db.Integer, ForeignKey(SchoolSubject.id))
    school_subject = db.relationship(SchoolSubject)
    student_id = db.Column(db.Integer, ForeignKey(Student.id))
    student = db.relationship(Student)
    test_type_id = db.Column(db.Integer, ForeignKey(TestType.id))
    test_type = db.relationship(TestType)
    

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String, nullable=False)
    last_name = db.Column('last_name', db.String, nullable=False)
    
    
class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column('id', db.Integer, primary_key=True)
    day = db.Column('day', db.String, nullable=False)
    
    school_subject_id = db.Column(db.Integer, ForeignKey(SchoolSubject.id))
    school_subject = db.relationship(SchoolSubject)
    teacher_id = db.Column(db.Integer, ForeignKey(Teacher.id))
    teacher = db.relationship(Teacher)
    

class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)


class PaymentStatus(db.Model):
    __tablename__ = 'payment_statuses'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)    
    

class TaxReceiptStatus(db.Model):
    __tablename__ = 'tax_receipt_statuses'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    

class Procedure(db.Model):
    __tablename__ = 'procedures'
    id = db.Column('id', db.Integer, primary_key=True)
    procedure_date = db.Column('procedure_date', db.Date, nullable=False)
    expiration_date = db.Column('expiration_date', db.Date, nullable=False)
    rfc = db.Column('rfc', db.String(13), nullable=False)
    amount = db.Column('amount', db.Float, nullable=False)
    
    request_id = db.Column(db.Integer, ForeignKey(Request.id))
    request = db.relationship(Request)
    payment_status_id = db.Column(db.Integer, ForeignKey(PaymentStatus.id))
    payment_status = db.relationship(PaymentStatus)
    tax_receipt_Status_id = db.Column(db.Integer, ForeignKey(TaxReceiptStatus.id))
    tax_receipt_status = db.relationship(TaxReceiptStatus)
    