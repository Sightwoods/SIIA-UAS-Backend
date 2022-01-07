from datetime import datetime, timezone, timedelta

from functools import wraps

from flask import request
from flask.json import jsonify
from flask_restx import Api, Resource, fields

import jwt
import json
import sys

from .models import db, Student, JWTTokenBlocklist
from .config import BaseConfig

rest_api = Api(version="2.0", title="SIIA API")

login_model = rest_api.model(
    'LoginModel',
    {
        "account_number": fields.String(required=True, min_length=4, max_length=64),
        "nip": fields.String(required=True, min_length=4, max_length=16)
    }
)

user_edit_model = rest_api.model(
    'UserEditModel',
    {
        "new_nip": fields.String(required=True, min_length=4, max_length=64)
    }
)

# Middlewares para la protección de rutas
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if "authorization" in request.headers:
            token = request.headers["authorization"].split()[0]

        if not token:
            return {"success": False, "msg": "Valid JWT token is missing"}, 401

        try:
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            current_user: Student = Student.get_by_account_number(data["account_number"])

            if not current_user:
                return {"success": False,
                        "msg": "Sorry. Wrong auth token. This user does not exist."}, 401

            token_expired = db.session.query(JWTTokenBlocklist.id).filter_by(jwt_token=token).scalar()

            if token_expired is not None:
                return {"success": False, "msg": "Token revoked."}, 401

            if not current_user.check_jwt_auth_active():
                return {"success": False, "msg": "Token expired."}, 401

        except:
            return {"success": False, "msg": "Token is invalid"}, 401

        return f(current_user, *args, **kwargs)

    return decorator

# Auth routes
# Verifica las credenciales del usuario, retornando un token si todo esta en orden
@rest_api.route('/api/users/login')
class Login(Resource):
    @rest_api.expect(login_model, validate=True)
    def post(self):

        req_data = request.get_json()

        _account_number = req_data.get("account_number")
        _nip = req_data.get("nip")

        user_exists: Student = Student.get_by_account_number(_account_number)

        if not user_exists:
            return {"success": False,
                    "msg": "This account number does not exist."}, 400

        if not user_exists.check_nip(_account_number, _nip):
            return {"success": False,
                    "msg": "Wrong credentials."}, 400

        # create access token uwing JWT
        payload = {
            'account_number': _account_number,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        token: jwt = jwt.encode(payload, BaseConfig.SECRET_KEY)

        user_exists.set_jwt_auth_active(True)
        user_exists.save()

        return {
            "success": True,
            "token": token,
            "user": user_exists.toJSON()
        },

# Permite editar el NIP del usuario
@rest_api.route('/api/users/edit_nip')
class EditUser(Resource):
    @rest_api.expect(user_edit_model)
    @token_required
    def post(self, current_user):
        req_data = request.get_json()
        _new_nip = req_data.get("new_nip")

        if _new_nip:
           self.update_nip(_new_nip)

        self.save()

        return {"success": True}, 200

# Verifica si el token aun sigue en vigencia
@rest_api.route('/api/users/auth_check')
class CheckAuth(Resource):
    @token_required
    def get(self, current_user):
        token = request.headers["authorization"].split()[0]
        data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
        user: Student = Student.get_by_account_number(data["account_number"])

        return {"success": True, "user": user.toJSON()}, 200

# Manda al token actual del usuario a una lista negra
@rest_api.route('/api/users/logout')
class LogoutUser(Resource):
    @token_required
    def post(self, current_user):

        _jwt_token = request.headers["authorization"]

        jwt_block = JWTTokenBlocklist(jwt_token=_jwt_token, created_at=datetime.now(timezone.utc))
        jwt_block.save()

        self.set_jwt_auth_active(False)
        self.save()

        return {"success": True}, 200

# Student Data routes
# Retorna los folios
@rest_api.route('/api/users/folio_query') 
class FolioQuery(Resource):
    @token_required
    def get(self, current_user):
        token = request.headers["authorization"].split()[0]
        data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
        account = data["account_number"]

        return {"success": True, "user": user.toJSON()}, 200

# Retorna las materias del alumno
@rest_api.route('/api/users/subjects')
class Subjects(Resource):
    @token_required
    def get(self, current_user):
        try:
            token = request.headers["authorization"].split()[0]
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            account = data["account_number"]
            response = Student.subjects(account)
            # print(len(response), file=sys.stdout)
            if len(response) > 0:
                return {"success": True, "data": response}, 200
            else:
                return {"success": False, "msg": "No hay datos"}, 200
        except:
            return {"success": False, "msg": "Error interno"}, 500

# Retorna el historial acádemico
@rest_api.route('/api/users/academic_record')
class AcademicRecords(Resource):
    @token_required
    def get(self, current_user):
        try:
            token = request.headers["authorization"].split()[0]
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            account = data["account_number"]
            response = Student.academic_record(account)
            # print(len(response), file=sys.stdout)
            if len(response) > 0:
                return {"success": True, "data": response}, 200
            else:
                return {"success": False, "msg": "No hay datos"}, 200
        except:
            return {"success": False, "msg": "Error interno"}, 500

# Retorna el horario de clases
@rest_api.route('/api/users/schedule') 
class Schedule(Resource):
    @token_required
    def get(self, current_user):
        try:
            token = request.headers["authorization"].split()[0]
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            account = data["account_number"]
            response = Student.schedule(account)
            if len(response) > 0:
                return {"success": True, "data": response}, 200
            else:
                return {"success": False, "msg": "No hay datos"}, 200
        except:
            return {"success": False, "msg": "Error interno"}, 500

# Retorna el datos generales del alumno
@rest_api.route('/api/users/student') 
class StudentData(Resource):
    @token_required
    def get(self, current_user):
        try:
            token = request.headers["authorization"].split()[0]
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            account = data["account_number"]
            response = Student.student_data(account)
            if len(response) > 0:
                return {"success": True, "data": response[0]}, 200
            else:
                return {"success": False, "msg": "No hay datos"}, 200
        except:
            return {"success": False, "msg": "Error interno"}, 500

# Retorna el datos generales del tutor
@rest_api.route('/api/users/parents') 
class ParentData(Resource):
    @token_required
    def get(self, current_user):
        try:
            token = request.headers["authorization"].split()[0]
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=["HS256"])
            account = data["account_number"]
            response = Student.parent_data(account)
            if len(response) > 0:
                return {"success": True, "data": response[0]}, 200
            else:
                return {"success": False, "msg": "No hay datos"}, 200
        except:
            return {"success": False, "msg": "Error interno"}, 500