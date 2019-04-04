from enum import Enum

from django.conf import settings
from django.http import HttpResponseForbidden

import graphene

from .helpers import make_foo

class Query(graphene.ObjectType):
  foo = graphene.String()

  def resolve_foo(self, info):
    return make_foo()

schema = graphene.Schema(query=Query)