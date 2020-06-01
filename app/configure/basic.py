class Config(object):
	DEBUG=False
	TESTING=False

class Development(Config):
	DEBUG=True
	TESTING=True

class Production(Config):
	pass