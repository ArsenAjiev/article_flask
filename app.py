from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource, fields
from flask_cors import CORS

import datetime

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(version='1.0', title='Flask API',
          description='swagger for Flask',
          )
api.init_app(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


# model for swagger
model = api.model('article_models', {
    'title': fields.String('Enter title'),
    'body': fields.String('Enter body'),
})


@api.route('/get')
class getdata(Resource):
    def get(self):
        data = Articles.query.all()
        return jsonify(articles_schema.dump(data))



@api.route('/get/<int:id>')
class getdata(Resource):
    def get(self, id):
        data = Articles.query.get(id)
        return jsonify(article_schema.dump(data))



@api.route('/post')
class postdata(Resource):
    @api.expect(model)
    def post(self):
        article = Articles(title=request.json['title'], body=request.json['body'])
        db.session.add(article)
        db.session.commit()
        return {'message': 'data added to database'}


@api.route('/put/<int:id>')
class putdata(Resource):
    @api.expect(model)
    def put(self, id):
        article = Articles.query.get(id)
        article.title = request.json['title']
        article.body = request.json['body']
        db.session.commit()
        return {'message': 'data updated'}


@api.route('/delete/<int:id>')
class deletedata(Resource):
    def delete(self, id):
        article = Articles.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return {'message': 'data deleted successfully'}


if __name__ == '__main__':
    app.run(debug=True)

