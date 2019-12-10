from flask_restful import Resource
from flask_restful import reqparse
from ..models.base import db
from sqlalchemy import desc


class BaseResource(Resource):

    MODEL = None

    def __init__(self):
        super().__init__()
        self.parser = reqparse.RequestParser()
        self._register_args()


    def _register_args(self):
        pass


    def _get_filters(self):
        filters = self.parser.parse_args()
        return dict([(key, value) for (key, value) in filters.items() if value])

    def _get_sort(self):
        # TODO: Přidat řazení
        pass


    def get(self, id=None):
        if(id):
            item = self.MODEL.query.filter_by(id=id).first()
            if item:
                return item.to_dict()
            return {}

        filters = self._get_filters()

        query = self.MODEL.query
        if filters:
            query = query.filter_by(**filters)
        items = query.all()

        return [item.to_dict() for item in items]

    def post(self):
        args = self.parser.parse_args()

        item = self.MODEL(**args)
        db.session.add(item)
        db.session.commit()

        return {}
