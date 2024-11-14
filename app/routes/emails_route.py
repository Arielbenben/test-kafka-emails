from flask import Blueprint, request, jsonify
from app.service.producers_service.emails_producer_service import produce_email


all_emails_blueprint = Blueprint('api', __name__)


@all_emails_blueprint.route('/email', methods=['POST'])
def get_all_sentences_route():
    json_email = request.get_json()
    if not json_email:
        return jsonify({'Error': 'Expected to get json'})
    try:
        produce_email(json_email)
        return jsonify({'message': 'Email inserted successfully'}), 200
    except Exception as e:
        print(f"Error inserting email: {e}")
        return jsonify({'error': 'Failed to insert email'}), 500
