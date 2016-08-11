import datetime

import webapp2
from google.appengine.api import mail
from google.appengine.ext import ndb

from models import GameStatus
from utils import (
    get_all_users,
    get_user_games
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome to my api')


class SendEmailReminderHandler(webapp2.RequestHandler):
    @staticmethod
    def get_email_list():
        email_list = []

        timestamp = datetime.datetime.now() - datetime.timedelta(hours=24)

        users = get_all_users(100)

        for user in users:
            all_games = get_user_games(user.user_name)
            # filter for active games
            active_game_filter = ndb.query.FilterNode('game_status', '=', GameStatus.IN_SESSION.number)
            # filter for timestamp
            timestamp_filter = ndb.query.FilterNode('timestamp', '<', timestamp)
            # fetch filtered games of this user
            filtered_games = all_games.filter(active_game_filter, timestamp_filter).fetch()
            if filtered_games:
                email_list.append(user.email)

        return email_list

    @staticmethod
    def get():
        email_list = SendEmailReminderHandler.get_email_list()
        for email in email_list:
            mail.send_mail(sender="ahmed.elsayed.mahmoud3@gmail.com",
                           to=email,
                           subject="Make your move!",
                           body="""
                           Dear Player,
							
						   I hope you are fine. You have not made your move in past 24 hrs.
						   Login to your game account and guess a char.

                           Best regards,
                           Hangman Game Team
                           """)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/crons/send_email_reminders', SendEmailReminderHandler)
], debug=True)
