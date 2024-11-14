from flask import Flask
from app.db.db_psql.database import init_db
from app.routes.emails_route import emails_blueprint
from app.service.init_kafka_topics_service import init_topics


app = Flask(__name__)

app.register_blueprint(emails_blueprint, url_prefix='/api')


if __name__ == '__main__':
    init_topics()
    init_db()
    app.run()