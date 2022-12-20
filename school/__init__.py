import random
import json
import os

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import Model, SQLAlchemy
from flask_cors import CORS, cross_origin

# from models import setup_db


def create_app(test_config=None):
    """Create and configure API"""
    app = Flask(__name__)
    # setup_db(app)


    # @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    
    
    
    @app.after_request
    def after_request(response):
        """@TODO: Use the after_request decorator to set Access-Control-Allow"""

        response.headers.add('Access_Control_Allow_Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access_Control_Allow_Methods',
                             'GET, PATCH, POST, DELETE')
        return response

    @app.route("/")
    @cross_origin()
    def hello():
        """Return Hello"""
        return "Hello"


 
    @app.errorhandler(404)
    def not_found(error):   
        """
        Error handler for 404
        """
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        """
        Error handler for 422
        """
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        }), 422

    return app
