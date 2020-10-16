from mashumaro.serializer.base.metaprogramming import CodeBuilder

@dataclass
class Member:
    count: int


@dataclass
class MainClass:
    member: Member


builder = CodeBuilder(MainClass)
builder.add_from_dict()
