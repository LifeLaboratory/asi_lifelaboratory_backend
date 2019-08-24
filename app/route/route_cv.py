# coding=utf-8
from app.api.base import base_name as names
from app.api.src.cv import *
from app.api.base.base_router import BaseRouter


class Cv(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL, names.TITLE, names.TYPE]

    def get(self):
        answer = get_cv()
        return answer or {}

    def post(self):
        self._read_args()
        answer = update_cv(self.data)
        return answer or {}


class GetCv(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_user_cv(args)
        return answer or {}
