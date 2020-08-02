from flask import Flask, redirect, url_for, session
from flask_restful import Resource

class UserSignIn(Resource):
    def __init__(self, **kwargs):
        self.oauth = kwargs['oauth']

    def get(self):
        oauth = self.oauth
        google = oauth.create_client('google')  # create the google oauth client
        redirect_uri = url_for('userauthorize', _external=True)
        return google.authorize_redirect(redirect_uri)

class UserAuthorize(Resource):
    def __init__(self, **kwargs):
        self.oauth = kwargs['oauth']

    def get(self):
        oauth = self.oauth
        google = oauth.create_client('google')  # create the google oauth client
        token = google.authorize_access_token()  # Access token from google (needed to get user info)
        resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
        user_info = resp.json()
        user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
        # Here you use the profile/user data that you got and query your database find/register the user
        # and set ur own data in the session not the profile from google
        session['profile'] = user_info
        session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
        return redirect('/')