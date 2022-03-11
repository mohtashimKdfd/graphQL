import graphene

class Query(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()

    def resolve_name(self, info):
        return "Mohtashim"

    def resolve_age(self, info):
        return "22"

schema = graphene.Schema(query=Query)
print(schema)

# ++++++++++++++++++++ #
query = '''
    query myquery{
        name
        age
    }
'''
result = schema.execute(query)

print(result)