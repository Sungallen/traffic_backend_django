from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from .models import flows

class flowsType(DjangoObjectType):
    class Meta:
        model = flows
        fields = ("id", "category", "flow", "time")

class Query(graphene.ObjectType):
    alldatas = graphene.List(flowsType)
    category_data = graphene.List(flowsType, category=graphene.String(required=True))

    def resolve_alldatas(root, info):
        return flows.objects.all()

    def resolve_category_data (root, info, category):
        try:
            return flows.objects.filter(category=category)
        except flows.DoesNotExist:
            return None

class FlowMutation(graphene.Mutation):
    
    class Arguments:
        category = graphene.String(required=True)
        location = graphene.String(required=True)
        flow = graphene.Int(required=True)
        time = graphene.DateTime(required=True)

    flow_data = graphene.Field(flowsType)

    @classmethod
    def mutate(cls, root, info, category, location, flow, time):
        flow_data = flows(category = category, location = location, flow = flow, time = time)
        flow_data.save()
        return FlowMutation(flow_data=flow_data)
    
class Mutation(graphene.ObjectType):
    insert_flow = FlowMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)