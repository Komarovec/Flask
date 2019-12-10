from .base import BaseResource
from ..models.section import SectionModel
from flask import request

class SectionResource(BaseResource):

    MODEL = SectionModel

    def _register_args(self):
        super()._register_args()

        if request.method == "POST":
            self.parser.add_argument("name", type=str, location="form")
            self.parser.add_argument("description", type=str, location="form")

        elif request.method == "GET":
            self.parser.add_argument("name", type=str, location="args")
