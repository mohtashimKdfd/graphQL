import graphene
import json

DATA=[
    {
        "name":"Mohtashim",
        "age" : "22"
    },
    {
        "name":"Kamran",
        "age" : "22"
    }
]

class User(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()



class Query(graphene.ObjectType):
    array = graphene.List(User)

    def resolve_array(self, info):
        return DATA

schema = graphene.Schema(query=Query)
print(schema)

# ++++++++++++++++++++ #
query = '''
    query myquery{
        array{
            myname : name
        }
    }
'''
result = schema.execute(query)

print(json.dumps(result.data))