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

from .sub_resource import SubResource


class TrustedIdProvider(SubResource):
    """Data Lake Store firewall rule information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param id_provider: The URL of this trusted identity provider
    :type id_provider: str
    """ 

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'id_provider': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id_provider': {'key': 'properties.idProvider', 'type': 'str'},
    }

    def __init__(self, id_provider, name=None):
        super(TrustedIdProvider, self).__init__(name=name)
        self.id_provider = id_provider
