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


class TopicCreateOrUpdateParameters(Model):
    """Parameters supplied to the Create Or Update Topic operation.

    :param name: Topic name.
    :type name: str
    :param location: Location of the resource.
    :type location: str
    :param accessed_at: Last time the message was sent, or a request was
     received, for this topic.
    :type accessed_at: datetime
    :param auto_delete_on_idle: TimeSpan idle interval after which the topic
     is automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: str
    :param entity_availability_status: Entity availability status for the
     topic. Possible values include: 'Available', 'Limited', 'Renaming',
     'Restoring', 'Unknown'
    :type entity_availability_status: str or :class:`EntityAvailabilityStatus
     <azure.mgmt.servicebus.models.EntityAvailabilityStatus>`
    :param created_at: Exact time the message was created.
    :type created_at: datetime
    :param count_details:
    :type count_details: :class:`MessageCountDetails
     <azure.mgmt.servicebus.models.MessageCountDetails>`
    :param default_message_time_to_live: Default message time to live value.
     This is the duration after which the message expires, starting from when
     the message is sent to Service Bus. This is the default value used when
     TimeToLive is not set on a message itself.
    :type default_message_time_to_live: str
    :param duplicate_detection_history_time_window: TimeSpan structure that
     defines the duration of the duplicate detection history. The default
     value is 10 minutes.
    :type duplicate_detection_history_time_window: str
    :param enable_batched_operations: Value that indicates whether
     server-side batched operations are enabled.
    :type enable_batched_operations: bool
    :param enable_express: Value that indicates whether Express Entities are
     enabled. An express topic holds a message in memory temporarily before
     writing it to persistent storage.
    :type enable_express: bool
    :param enable_partitioning: Value that indicates whether the topic to be
     partitioned across multiple message brokers is enabled.
    :type enable_partitioning: bool
    :param enable_subscription_partitioning: Value that indicates whether
     partitioning is enabled or disabled.
    :type enable_subscription_partitioning: bool
    :param filtering_messages_before_publishing: Whether messages should be
     filtered before publishing.
    :type filtering_messages_before_publishing: bool
    :param is_anonymous_accessible: Value that indicates whether the message
     is accessible anonymously.
    :type is_anonymous_accessible: bool
    :param is_express:
    :type is_express: bool
    :param max_size_in_megabytes: Maximum size of the topic in megabytes,
     which is the size of the memory allocated for the topic.
    :type max_size_in_megabytes: long
    :param requires_duplicate_detection: Value indicating if this topic
     requires duplicate detection.
    :type requires_duplicate_detection: bool
    :param size_in_bytes: Size of the topic, in bytes.
    :type size_in_bytes: long
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Creating',
     'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring',
     'SendDisabled', 'Unknown'
    :type status: str or :class:`EntityStatus
     <azure.mgmt.servicebus.models.EntityStatus>`
    :param subscription_count: Number of subscriptions.
    :type subscription_count: int
    :param support_ordering: Value that indicates whether the topic supports
     ordering.
    :type support_ordering: bool
    :param updated_at: The exact time the message was updated.
    :type updated_at: datetime
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'str'},
        'entity_availability_status': {'key': 'properties.entityAvailabilityStatus ', 'type': 'EntityAvailabilityStatus'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'str'},
        'duplicate_detection_history_time_window': {'key': 'properties.duplicateDetectionHistoryTimeWindow ', 'type': 'str'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'enable_express': {'key': 'properties.enableExpress', 'type': 'bool'},
        'enable_partitioning': {'key': 'properties.enablePartitioning', 'type': 'bool'},
        'enable_subscription_partitioning': {'key': 'properties.enableSubscriptionPartitioning', 'type': 'bool'},
        'filtering_messages_before_publishing': {'key': 'properties.filteringMessagesBeforePublishing', 'type': 'bool'},
        'is_anonymous_accessible': {'key': 'properties.isAnonymousAccessible', 'type': 'bool'},
        'is_express': {'key': 'properties.isExpress', 'type': 'bool'},
        'max_size_in_megabytes': {'key': 'properties.maxSizeInMegabytes', 'type': 'long'},
        'requires_duplicate_detection': {'key': 'properties.requiresDuplicateDetection', 'type': 'bool'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'subscription_count': {'key': 'properties.subscriptionCount', 'type': 'int'},
        'support_ordering': {'key': 'properties.supportOrdering', 'type': 'bool'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
    }

    def __init__(self, location, name=None, accessed_at=None, auto_delete_on_idle=None, entity_availability_status=None, created_at=None, count_details=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_express=None, enable_partitioning=None, enable_subscription_partitioning=None, filtering_messages_before_publishing=None, is_anonymous_accessible=None, is_express=None, max_size_in_megabytes=None, requires_duplicate_detection=None, size_in_bytes=None, status=None, subscription_count=None, support_ordering=None, updated_at=None):
        self.name = name
        self.location = location
        self.accessed_at = accessed_at
        self.auto_delete_on_idle = auto_delete_on_idle
        self.entity_availability_status = entity_availability_status
        self.created_at = created_at
        self.count_details = count_details
        self.default_message_time_to_live = default_message_time_to_live
        self.duplicate_detection_history_time_window = duplicate_detection_history_time_window
        self.enable_batched_operations = enable_batched_operations
        self.enable_express = enable_express
        self.enable_partitioning = enable_partitioning
        self.enable_subscription_partitioning = enable_subscription_partitioning
        self.filtering_messages_before_publishing = filtering_messages_before_publishing
        self.is_anonymous_accessible = is_anonymous_accessible
        self.is_express = is_express
        self.max_size_in_megabytes = max_size_in_megabytes
        self.requires_duplicate_detection = requires_duplicate_detection
        self.size_in_bytes = size_in_bytes
        self.status = status
        self.subscription_count = subscription_count
        self.support_ordering = support_ordering
        self.updated_at = updated_at
