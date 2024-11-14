from flask import Blueprint, request, jsonify
from app.service.producers_service.emails_producer import produce_email
from app.service.sentences_service import check_type_sentences, get_all_suspicious_content


emails_blueprint = Blueprint('api', __name__)


@emails_blueprint.route('/email', methods=['POST'])
def get_all_sentences_route():
    json_email = request.get_json()
    if not json_email:
        return jsonify({'Error': 'Expected to get json'})
    try:
        produce_email(json_email)
        check_type_sentences(json_email)
        return jsonify({'message': 'Email inserted successfully'}), 200
    except Exception as e:
        print(f"Error inserting email: {e}")
        return jsonify({'error': 'Failed to insert email'}), 500


@emails_blueprint.route('/email/<string:email>', methods=['GET'])
def get_all_suspicious_content_route(email: str):
    try:
        suspicious_content = get_all_suspicious_content(email)
        return jsonify({'suspicious_content': suspicious_content})
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': f'Failed to get content for email: {email}'}), 500


# @emails_blueprint.route('/most_common', methods=['GET'])
# def get_most_common_word_route():
#     try:
#         word = get_most_common_word()
#         return jsonify({'message': f'The most common word is: {word}'}), 200
#     except Exception as e:
#         print(f'Failed to get the most common word. Error: {e}')
#         return jsonify({'Erorr': 'Failed to get the most common word'})