from datetime import datetime
from elasticsearch import Elasticsearch
from cement import Controller, ex


es = Elasticsearch()


class Items(Controller):
    class Meta:
        label = "items"
        stacked_type = "embedded"
        stacked_on = "base"

    @ex(help="list items")
    def list(self):
        output = es.get(index="test-my-index", doc_type="my-test-type", id=1)
        print(output["_source"])

    @ex(help="create new item")
    def create(self):
        from .services import addIndex

        query = addIndex()
        es.index(index="test-my-index", doc_type="my-test-type", id=1, body=query)
        print("Index is created.")

    @ex(help="update an existing item")
    def update(self):
        from .services import updateIndex

        query = updateIndex()
        es.update(index="test-my-index", doc_type="my-test-type", id=1, body={"doc":query})
        print("Index is updated")

    @ex(help="delete an item")
    def delete(self):
        es.delete(index="test-my-index", id=1)
        print("Index deleted Successfuly")

    @ex(help="complete an item")
    def complete(self):
        print("Completed")
