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

"""Seating model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointUint16, Model


class Seating(Model):
    """Seating model.

    Attributes
    ----------
    Length: actuator
        Length adjustment of seating. 0 = Adjustable part of seating in rearmost position (Shortest length of seating).

        Value range: [0, ]
        Unit: mm
    """

    def __init__(self, name, parent):
        """Create a new Seating model."""
        super().__init__(parent)
        self.name = name

        self.Length = DataPointUint16("Length", self)
