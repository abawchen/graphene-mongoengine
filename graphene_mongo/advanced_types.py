import graphene


__all__ = [
    'PointFieldType'
]


def _resolve_point_type_coordinates(self, info):
    return self['coordinates']


class PointFieldType(graphene.ObjectType):

    type = graphene.String()
    coordinates = graphene.List(
        graphene.Float, resolver=_resolve_point_type_coordinates)

    def resolve_type(self, info):
        return self['type']
