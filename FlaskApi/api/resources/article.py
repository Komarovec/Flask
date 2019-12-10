from .base import BaseResource
from ..models.article import ArticleModel


class ArticleResource(BaseResource):

    MODEL = ArticleModel

    def _register_args(self):
        super()._register_args()

        self.parser.add_argument("title", type=str, location="form")
        self.parser.add_argument("content", type=str, location="form")
        self.parser.add_argument("section_id", type=int, location="form")
