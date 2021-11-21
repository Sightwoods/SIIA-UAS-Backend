from flask import request
from flask_restx import Api, Resource, fields
from datetime import datetime, timezone, timedelta
from functools import wraps
import jwt

from .models import db, Users, JWTTokenBlocklist
from .config import BaseConfig

rest_api = Api(version='1.0', title='Siia API')

# Modelos de peticiones y respuestas de la api
signup_model = rest_api.model('SignUpModel', {'account_number': fields.String(required=True, min_length=8, max_length=8),
                                              'nip': fields.String(required=True, min_length=4, max_length=32)
                                              })

login_model = rest_api.model('LoginModel', {'account_number': fields.String(required=True, min_length=8, max_length=8),
                                            'nip': fields.String(required=True, min_length=4, max_length=32)
                                            })

user_edit_model = rest_api.model('UserEditModel', {'account_number': fields.String(required=True, min_length=8, max_length=8),
                                                  'nip': fields.String(required=True, min_length=4, max_length=32)
                                                  })


# funcion auxiliar para verificar el token para JWT
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return {'success': False, 'msg': 'Valid JWT token is missing'}, 400

        try:
            data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=['HS256'])
            current_user: Users = Users.get_by_account_number(data['account_number'])

            if not current_user:
                return {'success': False,
                        'msg': 'Sorry. Wrong auth token. This user does not exist.'}, 400

            token_expired = db.session.query(JWTTokenBlocklist.id).filter_by(jwt_token=token).scalar()

            if token_expired is not None:
                return {'success': False, 'msg': 'Token revoked.'}, 400

            if not current_user.check_jwt_auth_active:
                return {'success': False, 'msg': 'Token expired.'}, 400

        except:
            return {'success': False, 'msg': 'Token is invalid'}, 400

        return f(current_user, *args, **kwargs)

    return decorator


@rest_api.route('/api/users/register')
class Register(Resource):
    ''' Creates a new user by taking 'signup_model' input '''
    @rest_api.expect(signup_model, validate=True)
    def post(self):
        req_data = request.get_json()

        _account_number = req_data.get('account_number')
        _nip = req_data.get('nip')

        user_exists = Users.get_by_account_number(_account_number)
        if user_exists:
            return {'success': False,
                    'msg': 'Account number already taken'}, 400

        new_user = Users(account_number=_account_number, nip=_nip)

        new_user.set_nip(_nip)
        new_user.save()

        return {'success': True,
                'account_number': new_user.account_number,
                'msg': 'The user was successfully registered'}, 200


@rest_api.route('/api/users/login')
class Login(Resource):
    @rest_api.expect(login_model, validate=True)
    def post(self):
        req_data = request.get_json()

        _account_number = req_data.get('account_number')
        _nip = req_data.get('nip')

        user_exists: Users = Users.get_by_account_number(_account_number,)

        if not user_exists:
            return {'success': False,
                    'msg': 'This account does not exist.'}, 400

        if not user_exists.check_nip(_nip):
            return {'success': False,
                    'msg': 'Wrong credentials.'}, 400

        # create access token using JWT
        token = jwt.encode({'account_number': _account_number, 'exp': datetime.utcnow() + timedelta(minutes=30)}, BaseConfig.SECRET_KEY)

        user_exists.set_jwt_auth_active(True)
        user_exists.save()

        return {'success': True,
                'token': token,
                'user': user_exists.toJSON()}, 200


@rest_api.route('/api/users/edit')
class EditUser(Resource):
    @rest_api.expect(user_edit_model)
    @token_required
    def post(self: Users):
        req_data = request.get_json()

        _new_nip = req_data.get('nip')

        if _new_nip:
            self.update_nip(_new_nip)

        self.save()

        return {'success': True}, 200


@rest_api.route('/api/users/logout')
class LogoutUser(Resource):
    @token_required
    def post(self: Users):
        _jwt_token = request.headers['authorization']

        jwt_block = JWTTokenBlocklist(jwt_token=_jwt_token, created_at=datetime.now(timezone.utc))
        jwt_block.save()

        self.set_jwt_auth_active(False)
        self.save()

        return {'success': True}, 200