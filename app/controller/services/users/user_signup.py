import graphene
from app.schema.user.schema_user import UserSignupRes


class UserSignup(graphene.Mutation):
	class Arguments:
		username		= graphene.String()

	Output	= UserSignupRes

	def mutate(self, info, **kwargs):
		pass