# coding=utf-8
from app.api.base import base_name as names
from app.api.src.project import *
from app.api.base.base_router import BaseRouter


class Projects(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.ID_PROJECT, names.ID_CATEGORY]

    def post(self):
        self._read_args()
        answer = get_filter_project(self.data)
        return answer or {}

