from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from services.test import tests
from services.area import areas
from services.pregunta import preguntas
from services.respuesta import respuestas
from flask_sqlalchemy import SQLAlchemy
from services.predio import predios
from config import DATABASE_CONNECTION

from sqlalchemy import text  # ESTO

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)

db.init_app(app) 
app.register_blueprint(estudiantes)
app.register_blueprint(tests)
app.register_blueprint(areas)
app.register_blueprint(preguntas)
app.register_blueprint(respuestas)

with app.app_context():
    db.create_all


#################### PARA PROBAR SI HAY CONEXIÓN
@app.route('/check_db')
def check_db():
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
            return 'Database connection successful!', 200
    except Exception as e:
        return str(e), 500
##########################################

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)

    