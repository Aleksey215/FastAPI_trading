"""
Models for creating tables in database
"""
from datetime import datetime, timezone

from sqlalchemy import MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey, JSON


metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
    schema='trading'
)

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registred_at", TIMESTAMP, default=datetime.now(tz=timezone.utc)),
    Column("role_id", Integer, ForeignKey("trading.role.id")),
    schema='trading'
)
