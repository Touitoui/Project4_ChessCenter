from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice
from app.tools.inquirer_validation import InquirerValidation


class InquirerTools:
    @classmethod
    def ask_confirmation(cls, question):
        answer = inquirer.confirm(
            message=question,
        ).execute()
        return answer

    @classmethod
    def prompt_text(cls, question, validate=EmptyInputValidator("Le champs ne doit pas être vide")):
        answer = inquirer.text(
            message=question,
            validate=validate
        ).execute()
        return answer

    @classmethod
    def prompt_date(cls, question, format_type="date"):
        validator = None
        match format_type:
            case "date":
                validator = InquirerValidation.date_validation
            case "datetime":
                validator = InquirerValidation.datetime_validation
            case "time":
                validator = InquirerValidation.time_validation

        answer = inquirer.text(
            message=question,
            validate=validator
        ).execute()
        print(answer)
        return answer

    @classmethod
    def prompt_int(cls, question, default_number=None):
        answer = inquirer.number(
            message=question,
            min_allowed=1,
            default=default_number,
            validate=NumberValidator("Entrez un nombre")
        ).execute()
        return answer

    @classmethod
    def prompt_club(cls, question):
        answer = inquirer.text(
            message=question,
            validate=InquirerValidation.club_validation
        ).execute()
        return answer

    @classmethod
    def sort_choices(cls, choices):
        choices.sort(key=lambda x: x.name)
        return choices
