# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import datetime
import time

from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction

from simple_supply_addressing import addresser

from simple_supply_protobuf import payload_pb2

from simple_supply_tp.payload import SimpleSupplyPayload
from simple_supply_tp.state import SimpleSupplyState


SYNC_TOLERANCE = 60 * 5
MAX_LAT = 90 * 1e6
MIN_LAT = -90 * 1e6
MAX_LNG = 180 * 1e6
MIN_LNG = -180 * 1e6


class SimpleSupplyHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespaces(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = SimpleSupplyPayload(transaction.payload)
        state = SimpleSupplyState(context)

        _validate_timestamp(payload.timestamp)

        if payload.action == payload_pb2.SimpleSupplyPayload.CREATE_AGENT:
            _create_agent(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        elif payload.action == payload_pb2.SimpleSupplyPayload.CREATE_RECORD:
            _create_record(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        elif payload.action == payload_pb2.SimpleSupplyPayload.TRANSFER_RECORD:
            _transfer_record(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        elif payload.action == payload_pb2.SimpleSupplyPayload.UPDATE_RECORD:
            _update_record(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        else:
            raise InvalidTransaction('Unhandled action')


def _create_agent(state, public_key, payload):
    #    Write code here


def _create_record(state, public_key, payload):
    #    Write code here


def _transfer_record(state, public_key, payload):
    #    Write code here


def _update_record(state, public_key, payload):
    #    Write code here


def _validate_record_owner(signer_public_key, record):
    """Validates that the public key of the signer is the latest (i.e.
    current) owner of the record
    """
    #    Write code here


def _validate_latlng(latitude, longitude):
    #    Write code here


def _validate_timestamp(timestamp):
    """Validates that the client submitted timestamp for a transaction is not
    greater than current time, within a tolerance defined by SYNC_TOLERANCE

    NOTE: Timestamp validation can be challenging since the machines that are
    submitting and validating transactions may have different system times
    """
    #    Write code here
