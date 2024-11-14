from app.db_mongo.database import all_emails_collection




def insert_email_to_db(email: dict):
    if not isinstance(email, dict):
        raise ValueError("Expected 'email' to be a dictionary.")
    try:
        all_emails_collection.insert_one(email)
        print('Email inserted successfully')
    except Exception as e:
        print(f'Error inserting email: {e}')
    return



