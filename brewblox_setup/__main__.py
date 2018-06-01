"""
Setup wizard entry point
"""
import inquirer
from functools import reduce


def system_questions(all_answers: dict) -> dict:
    system_services = [
        'history',
        'events',
        'gateway'
    ]

    questions = [
        inquirer.List('architecture',
                      message='On what kind of computer are you installing BrewBlox?',
                      choices=['Raspberry', 'Desktop']),
        inquirer.Checkbox('system_services',
                          message='Which system services do you want?',
                          choices=system_services,
                          default=system_services)
    ]
    answers = inquirer.prompt(questions)
    return answers


def device_questions(all_answers: dict) -> dict:
    devices = [
        'spark',
        'tilt'
    ]


def main():
    question_funcs = [
        system_questions
    ]

    all = reduce(
        lambda val, func: func(val),
        question_funcs,
        dict()
    )
    print(all)


if __name__ == '__main__':
    main()
