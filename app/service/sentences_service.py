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
