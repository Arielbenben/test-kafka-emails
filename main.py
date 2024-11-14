from flask import Flask
from app.routes.emails_route import all_emails_blueprint
from app.service.init_kafka_topics_service import init_topics


app = Flask(__name__)

app.register_blueprint(all_emails_blueprint, url_prefix='/api')


if __name__ == '__main__':
    init_topics()
    app.run()