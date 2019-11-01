from typing import Mapping

from mashumaro.serializer.base.metaprogramming import CodeBuilder


class DataClassDictMixin:
    # def __init_subclass__(cls, **kwargs):
    #   build_types()

    # call this in post_init...
    @classmethod
    def build_types(cls):

        try:
            # don't do it twice...
            return cls.__is_mashu_built__

        except AttributeError:

            builder = CodeBuilder(cls)

            # we like it so much, we call it twice!!
            # copy-paste error, or partial side effect?
            exc = None
            try:
                builder.add_from_dict()
            except Exception as e:
                exc = e
            if exc:
                raise exc

            # done
            cls.__is_mashu_built__ = True

        return cls.__is_mashu_built__

    def to_dict(
            self,
            use_bytes: bool = False,
            use_enum: bool = False,
            use_datetime: bool = False) -> dict:
        pass

    @classmethod
    def from_dict(
            cls,
            d: Mapping,
            use_bytes: bool = False,
            use_enum: bool = False,
            use_datetime: bool = False) -> 'DataClassDictMixin':
        pass


__all__ = [
    'DataClassDictMixin'
]
