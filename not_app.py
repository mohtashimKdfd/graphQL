from dataclasses import Field
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


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    ok = graphene.Boolean()
    user = graphene.Field(User)

    def mutate(self, info, name):
        user = User(name=name)
        ok = True
        return CreateUser(user=user, ok=ok)

class MyMutation(graphene.ObjectType):
    createuser = CreateUser.Field()



class Query(graphene.ObjectType):
    user = graphene.Field(User)
    # array = graphene.List(User)

    # def resolve_array(self, info):
    #     return DATA

schema = graphene.Schema(query=Query,mutation=MyMutation)
print(schema)

# ++++++++++++++++++++ #
query = '''
    mutation MyMutation{
        createuser(name:"Mohtashim"){
            user {
                name
            }
            ok
        }
    }
'''
result = schema.execute(query)

print(json.dumps(result.data))     