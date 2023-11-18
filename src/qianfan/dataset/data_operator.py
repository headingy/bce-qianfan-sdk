# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
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
"""
data operator for qianfan online
not available currently
"""

from typing import Any, Dict


class QianfanOperator:
    """Basic class for online ETL operator"""

    operator_name: str
    arg_dict: Dict[str, Any]


class ExceptionRegulator(QianfanOperator):
    """Exception class for online ETL operator"""

    pass


class Filter(QianfanOperator):
    """Filter class for online ETL operator"""

    pass


class Deduplicator(QianfanOperator):
    """Deduplicator class for online ETL operator"""

    pass


class SensitiveDataProcessor(QianfanOperator):
    """Sensitive data processor class for online ETL operator"""

    pass