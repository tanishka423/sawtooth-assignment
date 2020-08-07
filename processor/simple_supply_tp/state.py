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

from simple_supply_addressing import addresser

from simple_supply_protobuf import agent_pb2
from simple_supply_protobuf import record_pb2


class SimpleSupplyState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def get_agent(self, public_key):
        """Gets the agent associated with the public_key

        Args:
            public_key (str): The public key of the agent

        Returns:
            agent_pb2.Agent: Agent with the provided public_key
        """
        #    Write code here


    def set_agent(self, public_key, name, timestamp):
        """Creates a new agent in state

        Args:
            public_key (str): The public key of the agent
            name (str): The human-readable name of the agent
            timestamp (int): Unix UTC timestamp of when the agent was created
        """
        #    Write code here
    

    def get_record(self, record_id):
        """Gets the record associated with the record_id

        Args:
            record_id (str): The id of the record

        Returns:
            record_pb2.Record: Record with the provided record_id
        """
        #    Write code here

    def set_record(self,
                   public_key,
                   latitude,
                   longitude,
                   record_id,
                   timestamp):
        """Creates a new record in state

        Args:
            public_key (str): The public key of the agent creating the record
            latitude (int): Initial latitude of the record
            longitude (int): Initial latitude of the record
            record_id (str): Unique ID of the record
            timestamp (int): Unix UTC timestamp of when the agent was created
        """
        #    Write code here


    def transfer_record(self, receiving_agent, record_id, timestamp):
        #    Write code here


    def update_record(self, latitude, longitude, record_id, timestamp):
        #    Write code here
