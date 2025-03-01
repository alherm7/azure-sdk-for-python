# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar code: Required. The error code.
    :vartype code: str
    :ivar message: Required. The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.phonenumbers.models.CommunicationError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.phonenumbers.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innererror', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code: Required. The error code.
        :paramtype code: str
        :keyword message: Required. The error message.
        :paramtype message: str
        """
        super(CommunicationError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = None
        self.details = None
        self.inner_error = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :ivar error: Required. The Communication Services error.
    :vartype error: ~azure.communication.phonenumbers.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword error: Required. The Communication Services error.
        :paramtype error: ~azure.communication.phonenumbers.models.CommunicationError
        """
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = kwargs['error']


class PhoneNumberCapabilities(msrest.serialization.Model):
    """Capabilities of a phone number.

    All required parameters must be populated in order to send to Azure.

    :ivar calling: Required. Capability value for calling. Possible values include: "none",
     "inbound", "outbound", "inbound+outbound".
    :vartype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    :ivar sms: Required. Capability value for SMS. Possible values include: "none", "inbound",
     "outbound", "inbound+outbound".
    :vartype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    """

    _validation = {
        'calling': {'required': True},
        'sms': {'required': True},
    }

    _attribute_map = {
        'calling': {'key': 'calling', 'type': 'str'},
        'sms': {'key': 'sms', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword calling: Required. Capability value for calling. Possible values include: "none",
         "inbound", "outbound", "inbound+outbound".
        :paramtype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        :keyword sms: Required. Capability value for SMS. Possible values include: "none", "inbound",
         "outbound", "inbound+outbound".
        :paramtype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        """
        super(PhoneNumberCapabilities, self).__init__(**kwargs)
        self.calling = kwargs['calling']
        self.sms = kwargs['sms']


class PhoneNumberCapabilitiesRequest(msrest.serialization.Model):
    """Capabilities of a phone number.

    :ivar calling: Capability value for calling. Possible values include: "none", "inbound",
     "outbound", "inbound+outbound".
    :vartype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    :ivar sms: Capability value for SMS. Possible values include: "none", "inbound", "outbound",
     "inbound+outbound".
    :vartype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    """

    _attribute_map = {
        'calling': {'key': 'calling', 'type': 'str'},
        'sms': {'key': 'sms', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword calling: Capability value for calling. Possible values include: "none", "inbound",
         "outbound", "inbound+outbound".
        :paramtype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        :keyword sms: Capability value for SMS. Possible values include: "none", "inbound", "outbound",
         "inbound+outbound".
        :paramtype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        """
        super(PhoneNumberCapabilitiesRequest, self).__init__(**kwargs)
        self.calling = kwargs.get('calling', None)
        self.sms = kwargs.get('sms', None)


class PhoneNumberCost(msrest.serialization.Model):
    """The incurred cost for a single phone number.

    All required parameters must be populated in order to send to Azure.

    :ivar amount: Required. The cost amount.
    :vartype amount: float
    :ivar currency_code: Required. The ISO 4217 currency code for the cost amount, e.g. USD.
    :vartype currency_code: str
    :ivar billing_frequency: Required. The frequency with which the cost gets billed. Possible
     values include: "monthly".
    :vartype billing_frequency: str or ~azure.communication.phonenumbers.models.BillingFrequency
    """

    _validation = {
        'amount': {'required': True},
        'currency_code': {'required': True},
        'billing_frequency': {'required': True},
    }

    _attribute_map = {
        'amount': {'key': 'amount', 'type': 'float'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'billing_frequency': {'key': 'billingFrequency', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword amount: Required. The cost amount.
        :paramtype amount: float
        :keyword currency_code: Required. The ISO 4217 currency code for the cost amount, e.g. USD.
        :paramtype currency_code: str
        :keyword billing_frequency: Required. The frequency with which the cost gets billed. Possible
         values include: "monthly".
        :paramtype billing_frequency: str or ~azure.communication.phonenumbers.models.BillingFrequency
        """
        super(PhoneNumberCost, self).__init__(**kwargs)
        self.amount = kwargs['amount']
        self.currency_code = kwargs['currency_code']
        self.billing_frequency = kwargs['billing_frequency']


class PhoneNumberOperation(msrest.serialization.Model):
    """Long running operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar status: Required. Status of operation. Possible values include: "notStarted", "running",
     "succeeded", "failed".
    :vartype status: str or ~azure.communication.phonenumbers.models.PhoneNumberOperationStatus
    :ivar resource_location: URL for retrieving the result of the operation, if any.
    :vartype resource_location: str
    :ivar created_date_time: Required. The date that the operation was created.
    :vartype created_date_time: ~datetime.datetime
    :ivar error: The Communication Services error.
    :vartype error: ~azure.communication.phonenumbers.models.CommunicationError
    :ivar id: Required. Id of operation.
    :vartype id: str
    :ivar operation_type: Required. The type of operation, e.g. Search. Possible values include:
     "purchase", "releasePhoneNumber", "search", "updatePhoneNumberCapabilities".
    :vartype operation_type: str or
     ~azure.communication.phonenumbers.models.PhoneNumberOperationType
    :ivar last_action_date_time: The most recent date that the operation was changed.
    :vartype last_action_date_time: ~datetime.datetime
    """

    _validation = {
        'status': {'required': True},
        'created_date_time': {'required': True},
        'id': {'required': True},
        'operation_type': {'required': True},
        'last_action_date_time': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'CommunicationError'},
        'id': {'key': 'id', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword status: Required. Status of operation. Possible values include: "notStarted",
         "running", "succeeded", "failed".
        :paramtype status: str or ~azure.communication.phonenumbers.models.PhoneNumberOperationStatus
        :keyword resource_location: URL for retrieving the result of the operation, if any.
        :paramtype resource_location: str
        :keyword created_date_time: Required. The date that the operation was created.
        :paramtype created_date_time: ~datetime.datetime
        :keyword error: The Communication Services error.
        :paramtype error: ~azure.communication.phonenumbers.models.CommunicationError
        :keyword id: Required. Id of operation.
        :paramtype id: str
        :keyword operation_type: Required. The type of operation, e.g. Search. Possible values include:
         "purchase", "releasePhoneNumber", "search", "updatePhoneNumberCapabilities".
        :paramtype operation_type: str or
         ~azure.communication.phonenumbers.models.PhoneNumberOperationType
        """
        super(PhoneNumberOperation, self).__init__(**kwargs)
        self.status = kwargs['status']
        self.resource_location = kwargs.get('resource_location', None)
        self.created_date_time = kwargs['created_date_time']
        self.error = kwargs.get('error', None)
        self.id = kwargs['id']
        self.operation_type = kwargs['operation_type']
        self.last_action_date_time = None


class PhoneNumberPurchaseRequest(msrest.serialization.Model):
    """The phone number search purchase request.

    :ivar search_id: The search id.
    :vartype search_id: str
    """

    _attribute_map = {
        'search_id': {'key': 'searchId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword search_id: The search id.
        :paramtype search_id: str
        """
        super(PhoneNumberPurchaseRequest, self).__init__(**kwargs)
        self.search_id = kwargs.get('search_id', None)


class PhoneNumberSearchRequest(msrest.serialization.Model):
    """Represents a phone number search request to find phone numbers. Found phone numbers are temporarily held for a following purchase.

    All required parameters must be populated in order to send to Azure.

    :ivar phone_number_type: Required. The type of phone numbers to search for, e.g. geographic, or
     tollFree. Possible values include: "geographic", "tollFree".
    :vartype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
    :ivar assignment_type: Required. The assignment type of the phone numbers to search for. A
     phone number can be assigned to a person, or to an application. Possible values include:
     "person", "application".
    :vartype assignment_type: str or
     ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
    :ivar capabilities: Required. Capabilities of a phone number.
    :vartype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
    :ivar area_code: The area code of the desired phone number, e.g. 425.
    :vartype area_code: str
    :ivar quantity: The quantity of desired phone numbers. The default value is 1.
    :vartype quantity: int
    """

    _validation = {
        'phone_number_type': {'required': True},
        'assignment_type': {'required': True},
        'capabilities': {'required': True},
        'quantity': {'maximum': 2147483647, 'minimum': 1},
    }

    _attribute_map = {
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'area_code': {'key': 'areaCode', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword phone_number_type: Required. The type of phone numbers to search for, e.g. geographic,
         or tollFree. Possible values include: "geographic", "tollFree".
        :paramtype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
        :keyword assignment_type: Required. The assignment type of the phone numbers to search for. A
         phone number can be assigned to a person, or to an application. Possible values include:
         "person", "application".
        :paramtype assignment_type: str or
         ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
        :keyword capabilities: Required. Capabilities of a phone number.
        :paramtype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
        :keyword area_code: The area code of the desired phone number, e.g. 425.
        :paramtype area_code: str
        :keyword quantity: The quantity of desired phone numbers. The default value is 1.
        :paramtype quantity: int
        """
        super(PhoneNumberSearchRequest, self).__init__(**kwargs)
        self.phone_number_type = kwargs['phone_number_type']
        self.assignment_type = kwargs['assignment_type']
        self.capabilities = kwargs['capabilities']
        self.area_code = kwargs.get('area_code', None)
        self.quantity = kwargs.get('quantity', 1)


class PhoneNumberSearchResult(msrest.serialization.Model):
    """The result of a phone number search operation.

    All required parameters must be populated in order to send to Azure.

    :ivar search_id: Required. The search id.
    :vartype search_id: str
    :ivar phone_numbers: Required. The phone numbers that are available. Can be fewer than the
     desired search quantity.
    :vartype phone_numbers: list[str]
    :ivar phone_number_type: Required. The phone number's type, e.g. geographic, or tollFree.
     Possible values include: "geographic", "tollFree".
    :vartype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
    :ivar assignment_type: Required. Phone number's assignment type. Possible values include:
     "person", "application".
    :vartype assignment_type: str or
     ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
    :ivar capabilities: Required. Capabilities of a phone number.
    :vartype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
    :ivar cost: Required. The incurred cost for a single phone number.
    :vartype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
    :ivar search_expires_by: Required. The date that this search result expires and phone numbers
     are no longer on hold. A search result expires in less than 15min, e.g.
     2020-11-19T16:31:49.048Z.
    :vartype search_expires_by: ~datetime.datetime
    """

    _validation = {
        'search_id': {'required': True},
        'phone_numbers': {'required': True},
        'phone_number_type': {'required': True},
        'assignment_type': {'required': True},
        'capabilities': {'required': True},
        'cost': {'required': True},
        'search_expires_by': {'required': True},
    }

    _attribute_map = {
        'search_id': {'key': 'searchId', 'type': 'str'},
        'phone_numbers': {'key': 'phoneNumbers', 'type': '[str]'},
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'cost': {'key': 'cost', 'type': 'PhoneNumberCost'},
        'search_expires_by': {'key': 'searchExpiresBy', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword search_id: Required. The search id.
        :paramtype search_id: str
        :keyword phone_numbers: Required. The phone numbers that are available. Can be fewer than the
         desired search quantity.
        :paramtype phone_numbers: list[str]
        :keyword phone_number_type: Required. The phone number's type, e.g. geographic, or tollFree.
         Possible values include: "geographic", "tollFree".
        :paramtype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
        :keyword assignment_type: Required. Phone number's assignment type. Possible values include:
         "person", "application".
        :paramtype assignment_type: str or
         ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
        :keyword capabilities: Required. Capabilities of a phone number.
        :paramtype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
        :keyword cost: Required. The incurred cost for a single phone number.
        :paramtype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
        :keyword search_expires_by: Required. The date that this search result expires and phone
         numbers are no longer on hold. A search result expires in less than 15min, e.g.
         2020-11-19T16:31:49.048Z.
        :paramtype search_expires_by: ~datetime.datetime
        """
        super(PhoneNumberSearchResult, self).__init__(**kwargs)
        self.search_id = kwargs['search_id']
        self.phone_numbers = kwargs['phone_numbers']
        self.phone_number_type = kwargs['phone_number_type']
        self.assignment_type = kwargs['assignment_type']
        self.capabilities = kwargs['capabilities']
        self.cost = kwargs['cost']
        self.search_expires_by = kwargs['search_expires_by']


class PurchasedPhoneNumber(msrest.serialization.Model):
    """Represents a purchased phone number.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Required. The id of the phone number, e.g. 11234567890.
    :vartype id: str
    :ivar phone_number: Required. String of the E.164 format of the phone number, e.g.
     +11234567890.
    :vartype phone_number: str
    :ivar country_code: Required. The ISO 3166-2 code of the phone number's country, e.g. US.
    :vartype country_code: str
    :ivar phone_number_type: Required. The phone number's type, e.g. Geographic, TollFree. Possible
     values include: "geographic", "tollFree".
    :vartype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
    :ivar capabilities: Required. Capabilities of a phone number.
    :vartype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
    :ivar assignment_type: Required. The assignment type of the phone number. A phone number can be
     assigned to a person, or to an application. Possible values include: "person", "application".
    :vartype assignment_type: str or
     ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
    :ivar purchase_date: Required. The date and time that the phone number was purchased.
    :vartype purchase_date: ~datetime.datetime
    :ivar cost: Required. The incurred cost for a single phone number.
    :vartype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
    """

    _validation = {
        'id': {'required': True},
        'phone_number': {'required': True},
        'country_code': {'required': True},
        'phone_number_type': {'required': True},
        'capabilities': {'required': True},
        'assignment_type': {'required': True},
        'purchase_date': {'required': True},
        'cost': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'purchase_date': {'key': 'purchaseDate', 'type': 'iso-8601'},
        'cost': {'key': 'cost', 'type': 'PhoneNumberCost'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword id: Required. The id of the phone number, e.g. 11234567890.
        :paramtype id: str
        :keyword phone_number: Required. String of the E.164 format of the phone number, e.g.
         +11234567890.
        :paramtype phone_number: str
        :keyword country_code: Required. The ISO 3166-2 code of the phone number's country, e.g. US.
        :paramtype country_code: str
        :keyword phone_number_type: Required. The phone number's type, e.g. Geographic, TollFree.
         Possible values include: "geographic", "tollFree".
        :paramtype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
        :keyword capabilities: Required. Capabilities of a phone number.
        :paramtype capabilities: ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
        :keyword assignment_type: Required. The assignment type of the phone number. A phone number can
         be assigned to a person, or to an application. Possible values include: "person",
         "application".
        :paramtype assignment_type: str or
         ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
        :keyword purchase_date: Required. The date and time that the phone number was purchased.
        :paramtype purchase_date: ~datetime.datetime
        :keyword cost: Required. The incurred cost for a single phone number.
        :paramtype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
        """
        super(PurchasedPhoneNumber, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.phone_number = kwargs['phone_number']
        self.country_code = kwargs['country_code']
        self.phone_number_type = kwargs['phone_number_type']
        self.capabilities = kwargs['capabilities']
        self.assignment_type = kwargs['assignment_type']
        self.purchase_date = kwargs['purchase_date']
        self.cost = kwargs['cost']


class PurchasedPhoneNumbers(msrest.serialization.Model):
    """The list of purchased phone numbers.

    All required parameters must be populated in order to send to Azure.

    :ivar phone_numbers: Required. Represents a list of phone numbers.
    :vartype phone_numbers: list[~azure.communication.phonenumbers.models.PurchasedPhoneNumber]
    :ivar next_link: Represents the URL link to the next page of phone number results.
    :vartype next_link: str
    """

    _validation = {
        'phone_numbers': {'required': True},
    }

    _attribute_map = {
        'phone_numbers': {'key': 'phoneNumbers', 'type': '[PurchasedPhoneNumber]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword phone_numbers: Required. Represents a list of phone numbers.
        :paramtype phone_numbers: list[~azure.communication.phonenumbers.models.PurchasedPhoneNumber]
        :keyword next_link: Represents the URL link to the next page of phone number results.
        :paramtype next_link: str
        """
        super(PurchasedPhoneNumbers, self).__init__(**kwargs)
        self.phone_numbers = kwargs['phone_numbers']
        self.next_link = kwargs.get('next_link', None)
