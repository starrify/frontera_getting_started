#coding: utf8

from frontera.contrib.backends.sqlalchemy import Page, SQLAlchemyBackend
from sqlalchemy import Column, Integer
from frontera.core.models import Request, Response


class ScoredPage(Page):
    score = Column(Integer, nullable=False)


class ScoredBackend(SQLAlchemyBackend):
    component_name = 'SQLAlchemy Scored Backend'

    @property
    def page_model(self):
        return self.models['ScoredPage']

    def _get_order_by(self, query):
        return query.order_by(
            self.page_model.score.desc(), self.page_model.created_at)

    def _create_page(self, obj):
        db_page = super(ScoredBackend, self)._create_page(obj)
        if isinstance(obj, Request):
            db_page.score = obj.meta['scrapy_meta'].get('score', 0)
        elif isinstance(obj, Response):
            db_page.score = obj.request.meta['scrapy_meta'].get('score', 0)
        return db_page
