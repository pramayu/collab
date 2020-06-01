from graphene import ObjectType
from app.controller.services.users.user_signup import UserSignup

class UserServ(ObjectType):
	usersignup 			= UserSignup.Field()