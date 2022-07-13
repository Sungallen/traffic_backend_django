import graphene
from graphene_django import DjangoObjectType
from .models import flows, coordinates, category

class flowsType(DjangoObjectType):
    class Meta:
        model = flows
        fields = ("id", "category", "coordinates", "flow", "time")
class categoryType(DjangoObjectType):
    class Meta:
        model = category
        fields = ("id","category")
class coordinates(DjangoObjectType):
    class Meta:
        model = coordinates
        fields = ("id","coordinates")

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
        coordinates = graphene.String(required=True)
        flow = graphene.Int(required=True)
        time = graphene.DateTime(required=True)

    flow_data = graphene.Field(flowsType)

    @classmethod
    def mutate(cls, root, info, category, coordinates, flow, time):
        flow_data = flows(category = category, coordinates = coordinates, flow = flow, time = time)
        flow_data.save()
        return FlowMutation(flow_data=flow_data)

# class InputType(graphene.ObjectType):
#     category = graphene.String(required=True)
#     coordinates = graphene.String(required=True)
#     flow = graphene.Int(required=True)
#     time = graphene.DateTime(required=True)

class FlowMultiMutations(graphene.Mutation):
    Is_Successed = graphene.Boolean()
    status = graphene.Int()
    class Arguments:
        category = graphene.List(graphene.String, required=True)
        coordinates = graphene.List(graphene.String, required=True)
        flow = graphene.List(graphene.Int, required=True)
        time = graphene.DateTime(required=True)
        affectedrows = graphene.Int(required=True)
    @classmethod
    def mutate(cls, root, info, category, coordinates, flow, time, affectedrows):
        

        for i in range(affectedrows):
            try:
                flows.objects.create(category=category[i], coordinates=coordinates[i], flow=flow[i], time=time)
            except:
                return FlowMultiMutations(Is_Successed=False, status=404)
        return FlowMultiMutations(Is_Successed=True, status=200)

class Mutation(graphene.ObjectType):
    insert_flow = FlowMutation.Field()
    multiinsert_flow = FlowMultiMutations.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)