import graphene
from graphene import ObjectType

class User(ObjectType):
	id 				= graphene.ID()
	username		= graphene.String()
	email			= graphene.String()

class UserSignupRes(ObjectType):
	path			= graphene.String()
	status			= graphene.Boolean()