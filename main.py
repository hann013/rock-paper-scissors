#!/usr/bin/env python

import webapp2
import jinja2
import os
import random

win_counter = 0
loss_counter = 0 
tie_counter = 0
total_counter = 0

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render(template_values))

class PlayHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        global win_counter
        global loss_counter
        global tie_counter
        global total_counter

        player_choice = self.request.get('choice')
        if player_choice == "rock":
            template_values['player_choice'] = '<img src="/static/rock.png" alt="Rock">'
        elif player_choice == "paper":
            template_values['player_choice'] = '<img src="/static/paper.png" alt="Paper">'
        else:
            template_values['player_choice'] = '<img src="/static/scissors.png" alt="Scissors">'

        comp = random.randint(1, 3)
        if comp == 1:
            comp_choice = "rock"
            template_values['comp_choice'] = '<img src="/static/rock.png" alt="Rock">'
        elif comp == 2:
            comp_choice = "paper"
            template_values['comp_choice'] = '<img src="/static/paper.png" alt="Paper">'
        else:
            comp_choice = "scissors"
            template_values['comp_choice'] = '<img src="/static/scissors.png" alt="Scissors">'

        if comp_choice == player_choice:
            winner = "You tied!"
            tie_counter += 1
        elif (comp_choice == "rock" and player_choice == "scissors") or (comp_choice == "paper" and player_choice == "rock") or (comp_choice == "scissors" and player_choice == "paper"):
            winner = "You lost..."    
            loss_counter += 1  
        else:
            winner = "You won!"
            win_counter += 1

        template_values['ties'] = tie_counter
        template_values['losses'] = loss_counter 
        template_values['wins'] = win_counter

        total_counter += 1
        
        template_values['percentage'] = float(win_counter)/total_counter * 100
        template_values['winner'] = winner

        template = jinja_environment.get_template('play.html')
        self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

routes = [
    ('/', MainHandler),
    ('/play', PlayHandler), 
]

app = webapp2.WSGIApplication(routes, debug=True)
