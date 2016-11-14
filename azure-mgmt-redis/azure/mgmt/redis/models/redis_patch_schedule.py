# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RedisPatchSchedule(Model):
    """Response to put/get patch schedules for Redis cache.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location.
    :vartype location: str
    :param schedule_entries: List of patch schedules for a Redis cache.
    :type schedule_entries: list of :class:`ScheduleEntry
     <azure.mgmt.redis.models.ScheduleEntry>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'schedule_entries': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'schedule_entries': {'key': 'properties.scheduleEntries', 'type': '[ScheduleEntry]'},
    }

    def __init__(self, schedule_entries):
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.schedule_entries = schedule_entries
