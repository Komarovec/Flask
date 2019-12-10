from .article import ArticleResource
from .section import SectionResource

URLS = (
    ((ArticleResource, "/v1/articles"), "articles_list"),
    ((ArticleResource, "/v1/articles/<int:id>"), "articles_detail"),
    ((SectionResource, "/v1/sections"), "sections_list"),
    ((SectionResource, "/v1/sections/<int:id>"), "sections_detail"),
)
