import graphene
from app.schema.user.schema_user import User

class GetUsers(graphene.ObjectType):
	users 	= graphene.List(User)

	def resolve(root, info):
		pass