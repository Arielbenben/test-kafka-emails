from collections import Counter

from toolz import pipe,partial

from app.db.db_psql.database import session_maker
from app.db.db_psql.models.person import Person
from app.db.db_psql.models.suspicious_hostage_content import SuspiciousHostageContent
from app.repository.psql_repository.messages_explosive_repository import get_suspicious_explosive_content_by_email, \
    get_all_explosive_sentences
from app.repository.psql_repository.messages_hostage_repository import get_suspicious_hostage_content_by_email, \
    get_all_hostage_sentences
from app.service.producers_service.messages_explosive_producer import produce_messages_explosive
from app.service.producers_service.messages_hostage_producer import produce_messages_hostage
import re


def check_type_sentences(email: dict):
    explosive_pattern = re.compile(r'\bexplos\w*', re.IGNORECASE)
    hostage_pattern = re.compile(r'\bhostage\w*', re.IGNORECASE)

    for sentence in email['sentences']:
        if explosive_pattern.search(sentence):
            email['sentences'] = add_suspicious_sentence_first(sentence, email['sentences'])
            produce_messages_explosive(email)
            break
        elif hostage_pattern.search(sentence):
            email['sentences'] = add_suspicious_sentence_first(sentence, email['sentences'])
            produce_messages_hostage(email)
            break
    return


def add_suspicious_sentence_first(suspicious_sentence, all_sentence):
    sentences = [suspicious_sentence]
    for sentence in all_sentence:
        if sentence not in sentences:
            sentences.append(sentence)
    return sentences


def get_all_suspicious_content(email: str):
    suspicious_hostage_content = get_suspicious_hostage_content_by_email(email)
    suspicious_explosive_content = get_suspicious_explosive_content_by_email(email)
    all_suspicious_content = suspicious_explosive_content + suspicious_hostage_content
    return all_suspicious_content


def get_most_common_word():
    explosive_sentences = [explosive.sentence for explosive in get_all_explosive_sentences()]
    hostage_sentences = [hostage.sentence for hostage in get_all_hostage_sentences()]
    return pipe(
        explosive_sentences + hostage_sentences,
        "".join,
        lambda sen: sen.replace(".", " "),
        lambda sen: sen.replace(",", " "),
        lambda sen: sen.split(),
        partial(map, str.lower),
        list,
        lambda words: Counter(words).most_common(1)[0]
    )

