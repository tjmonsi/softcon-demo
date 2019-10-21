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

from flask import jsonify, request
from pprint import pprint
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):

    # for logging purposes
    pprint(vars(error), indent=2)
    pprint(vars(request), indent=2)

    return jsonify(
        success=False,
        code=404,
    error=error.description
    ), 404

@bp.app_errorhandler(400)
def not_found_error(error):

    # for logging purposes
    pprint(vars(error), indent=2)
    pprint(vars(request), indent=2)

    return jsonify(
        success=False,
        code=400,
    error=error.description
    ), 400

@bp.app_errorhandler(500)
def internal_error(error):

    # for logging purposes
    pprint(vars(error), indent=2)
    pprint(vars(request), indent=2)

    return jsonify(
        success=False,
        code=500,
    error=error.description
    ), 500
