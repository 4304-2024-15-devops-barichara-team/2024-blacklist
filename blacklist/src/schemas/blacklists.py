from marshmallow import Schema, fields

from src.constants.constants import DATE_FORMAT


class BlacklistDto(Schema):
    id = fields.String(attribute="id")
    email = fields.String(attribute="email")
    client_id = fields.String(attribute="client_id")
    reason = fields.String(attribute="reason")
    ip_address = fields.String(attribute="ip_address")
    createdAt = fields.DateTime(format=DATE_FORMAT, attribute="created_at")
