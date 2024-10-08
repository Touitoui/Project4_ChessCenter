from prompt_toolkit.validation import ValidationError
import string
from datetime import datetime


class InquirerValidation:
    def __init__(self):
        pass

    @classmethod
    def date_validation(cls, text):
        date_format = "%d-%m-%Y"
        try:
            if text != datetime.strptime(text, date_format).strftime(date_format):
                raise ValueError
            return True
        except ValueError:
            raise ValidationError(
                message="La date doit être entrée au format JJ-MM-AAAA"
            )

    @classmethod
    def datetime_validation(cls, text):  # TODO: Issue with format, not recognised
        date_format = "%H:%M %d-%m-%y"
        try:
            if text != datetime.strptime(text, date_format).strftime(date_format):
                raise ValueError
            return True
        except ValueError:
            raise ValidationError(
                message="La date doit être entrée au format HH:MM JJ-MM-AAAA"
            )

    @classmethod
    def time_validation(cls, text):
        date_format = "%H:%M"
        try:
            if text != datetime.strptime(text, date_format).strftime(date_format):
                raise ValueError
            return True
        except ValueError:
            raise ValidationError(
                message="L'heure doit être entrée au format HH:MM"
            )

    @classmethod
    def club_validation(cls, text):  # TODO: validator AB12345
        text = text.translate({ord(c): None for c in string.whitespace})
        if not (len(text) == 7 and text[:2].isalpha() and text[2:].isnumeric()):
            raise ValidationError(
                message="Le numéro de club doit être deux lettres suivit par 5 chiffres. (Ex: AB12345)",
            )
        return True




# if __name__ == '__main__':
#     InquirerTools.prompt_text("date:", InquirerValidation.timedate_validation)

