# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand

# Configure application and db connection

db_conn = 'sqlite:///reference.db'
create_engine('sqlite:///reference.db?charset=utf8')
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

class cs50(db.Model):
  __tablename__ = 'cs50'
  names = db.Column(db.String(825), primary_key=True)
  synopsis = db.Column(db.String(825))
  description = db.Column(db.String(10000))
  return_value = db.Column(db.String(825))
  examples = db.Column(db.String(1000))
  
class cs50Schema(ma.ModelSchema):
  class Meta:
    model = cs50
    
    
    
class ctype(db.Model):
  __tablename__ = 'ctype'
  names = db.Column(db.String(825), primary_key=True)
  synopsis = db.Column(db.String(825))
  feature_test = db.Column(db.String(825))
  description = db.Column(db.String(10000))
  return_value = db.Column(db.String(825))
  conforming_to = db.Column(db.String(825))
  notes = db.Column(db.String(825))
  bugs = db.Column(db.String(825))
  see_also = db.Column(db.String(825))
  
class ctypeSchema(ma.ModelSchema):
  class Meta:
    model = ctype   
    
    
    
class stdio(db.Model):
  __tablename__ = 'stdio'
  name = db.Column(db.String(825), primary_key=True)
  synopsis = db.Column(db.String(825))
  feature_test = db.Column(db.String(825))
  errors = db.Column(db.String(825))
  description = db.Column(db.String(20000))
  return_value = db.Column(db.String(825))
  conforming_to = db.Column(db.String(825))
  notes = db.Column(db.String(825))
  bugs = db.Column(db.String(825))
  see_also = db.Column(db.String(825))
  
class stdioSchema(ma.ModelSchema):
  class Meta:
    model = stdio      
    

models = ['cs50', 'ctype', 'stdio']
      

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<library>/<function>")
def selection(library, function):
    #func_name = request.args.get("func");
    #lib_name = request.args.get("lib");
    #if not func_name:
     #   raise RuntimeError("missing func_name or lib_name")
    result = []
    schema = cs50Schema(many=True)
    #.with_entities(cs50.names)
    if library == 'cs50':
      result = cs50.query.filter(cs50.names.like("%"+function+"%")).all() 
      schema = cs50Schema(many=True)
      
    if library == 'ctype':
      result = ctype.query.filter(ctype.names.like("%"+function+"%")).all() 
      schema = ctypeSchema(many=True)
      
    if library == 'stdio':
      result = stdio.query.filter(stdio.name.like("%"+function+"%")).all() 
      schema = stdioSchema(many=True)  
      
      
    #var_schema = library + "Schema"
    #cs50_schema = cs50Schema(many=True)
    func_out = schema.dump(result).data
    return jsonify(func_out) 
 
  
if __name__=="__main__":
  app.run()
