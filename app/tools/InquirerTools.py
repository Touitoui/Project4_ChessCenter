from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, NumberValidator
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice


class InquirerTools:
    @classmethod
    def ask_confirmation(cls, question):
        answer = inquirer.confirm(
            message=question,
        ).execute()
        return answer

    @classmethod
    def prompt_text(cls, question):
        answer = inquirer.text(
            message=question,
            validate=EmptyInputValidator("Le champs ne doit pas être vide")
        ).execute()
        return answer

    @classmethod
    # GESTION CHIFFRE InquirerPy à vérifier
    def prompt_int(cls, question, default_number):
        answer = inquirer.text(
            message=question,
            validate=NumberValidator("Entrez un nombre")
        ).execute()
        return answer

    @classmethod
    def sort_choices(cls, choices):
        choices.sort(key=lambda x: x.name)
        return choices
