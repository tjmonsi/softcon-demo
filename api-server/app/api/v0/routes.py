#!/usr/bin/env python
#
# Copyright 2019 Senti TechLabs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from flask import request, jsonify, abort
from app.api.v0 import bp
from app.modules.randomizer.v0 import predict as random

@bp.route('/random', methods=['GET', 'POST'])
def analyze():
    data = {}
    data['random'] = random()
    return jsonify(success=True, data=data)
