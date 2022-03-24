from turtle import title
from flask import render_template
from flask_classful import FlaskView, route

class Router(FlaskView):
    @route('/')
    def index(self):
        return render_template('pages/index.html', title = 'Yadah Football Club')

    @route('/upcoming-match')
    def upcoming_match(self):
        return render_template('pages/upcoming-match.html', title = 'Upcoming Match')

    @route('/match-results')
    def match_results(self):
        return render_template('pages/match-results.html', title = 'Match Results')

    @route('/match-details')
    def match_details(self):
        return render_template('pages/match-details.html', title = 'Match Details')

    @route('/contact')
    def contact(self):
        return render_template('pages/contact.html', title = 'Contact US')