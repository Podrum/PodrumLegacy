r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""


class login_status_type:
    success: int = 0
    failed_client: int = 1
    failed_server: int = 2
    spawn: int = 3
    failed_invalid_tenant: int = 4
    failed_vanilla_edu: int = 5
    failed_incompatible_version: int = 6
    failed_server_full: int = 7
