from marshmallow import fields

from api.libs.schema.base import (BaseSchema, Timestamp)


class RoleSchema(BaseSchema):
    name = fields.String()
    description = fields.String()

    class Meta:
        strict = True


class UserSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(load_only=True)
    confirmed_at = Timestamp(dump_only=True)
    roles = fields.List(fields.Nested(RoleSchema))

    class Meta:
        strict = True
