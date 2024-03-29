from app.route.document.provider import Provider
from app.api.base import base_name as names


def get_lesson(args):
    """
    Метод для получения данных о конкретном уроке
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_lesson(args)
    return answer


def get_lessons():
    """
    Метод для получения данных о уроке
    :return:
    """
    provider = Provider()
    answer = provider.get_lessons()
    return answer


def get_documents(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    id_user = args.get(names.ID_USER)
    id_document = args.get(names.ID_DOCUMENT)
    id_project = args.get(names.ID_PROJECT)
    args = {
        names.ID_USER: 'and upd."id_user" = %s' % id_user if id_user else 'and true',
        names.ID_DOCUMENT: 'and upd."id_document" = %s' % id_document if id_document else 'and true',
        names.ID_PROJECT: 'and upd."id_project" = %s' % id_project if id_project else 'and true',
    }
    answer = provider.get_documents(args)
    return answer


def get_user_document(args):
    """
    Метод для получения списка документов пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_document(args)
    return answer


def update_document(args):
    """
    Метод для добавлени/обновления документа
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_DOCUMENT):
        answer = provider.update_document(args)
    else:
        answer = provider.insert_document(args)
    return answer
