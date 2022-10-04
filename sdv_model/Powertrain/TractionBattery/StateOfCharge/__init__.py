#!/usr/bin/env python3

# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""StateOfCharge model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class StateOfCharge(Model):
    """StateOfCharge model.

    Attributes
    ----------
    Current: sensor
        Physical state of charge of the high voltage battery, relative to net capacity. This is not necessarily the state of charge being displayed to the customer.

        Value range: [0, 100.0]
        Unit: percent
    Displayed: sensor
        State of charge displayed to the customer.

        Value range: [0, 100.0]
        Unit: percent
    """

    def __init__(self, name, parent):
        """Create a new StateOfCharge model."""
        super().__init__(parent)
        self.name = name

        self.Current = DataPointFloat("Current", self)
        self.Displayed = DataPointFloat("Displayed", self)
