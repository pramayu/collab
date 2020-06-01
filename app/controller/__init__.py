from graphene import ObjectType, Schema

from app.controller.queries.users.get_users import GetUsers
from app.controller.services.users import UserServ

class Query(GetUsers, ObjectType):
	pass

class Service(UserServ, ObjectType):
	pass

schema = Schema(query=Query, mutation=Service)