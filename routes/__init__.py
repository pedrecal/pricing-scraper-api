import routes.user

def initialize_routes(api, args):
    api.add_resource(routes.user.UserSignIn, '/user', resource_class_kwargs=args)
    api.add_resource(routes.user.UserAuthorize, '/authorize', resource_class_kwargs=args)