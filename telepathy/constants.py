# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005 Collabora Limited
# Copyright (C) 2005 Nokia Corporation
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

CONN_MGR_PARAM_FLAG_REQUIRED = 1
CONN_MGR_PARAM_FLAG_REGISTER = 2

CONNECTION_ALIAS_FLAG_USER_SET = 1

CONNECTION_CAPABILITY_FLAG_CREATE = 1
CONNECTION_CAPABILITY_FLAG_INVITE = 2

CONNECTION_HANDLE_TYPE_NONE = 0
CONNECTION_HANDLE_TYPE_CONTACT = 1
CONNECTION_HANDLE_TYPE_ROOM = 2
CONNECTION_HANDLE_TYPE_LIST = 3

CONNECTION_PRESENCE_TYPE_UNSET = 0
CONNECTION_PRESENCE_TYPE_OFFLINE = 1
CONNECTION_PRESENCE_TYPE_AVAILABLE = 2
CONNECTION_PRESENCE_TYPE_AWAY = 3
CONNECTION_PRESENCE_TYPE_EXTENDED_AWAY = 4
CONNECTION_PRESENCE_TYPE_HIDDEN = 5

CONNECTION_STATUS_CONNECTED = 0
CONNECTION_STATUS_CONNECTING = 1
CONNECTION_STATUS_DISCONNECTED = 2

CONNECTION_STATUS_REASON_NONE_SPECIFIED = 0
CONNECTION_STATUS_REASON_REQUESTED = 1
CONNECTION_STATUS_REASON_NETWORK_ERROR = 2
CONNECTION_STATUS_REASON_AUTHENTICATION_FAILED = 3
CONNECTION_STATUS_REASON_ENCRYPTION_ERROR = 4
CONNECTION_STATUS_REASON_NAME_IN_USE = 5

CHANNEL_CONTACT_SEARCH_STATE_BEFORE = 0
CHANNEL_CONTACT_SEARCH_STATE_DURING = 1
CHANNEL_CONTACT_SEARCH_STATE_AFTER = 2

CHANNEL_TEXT_MESSAGE_FLAG_TRUNCATED = 1

CHANNEL_TEXT_MESSAGE_TYPE_NORMAL = 0
CHANNEL_TEXT_MESSAGE_TYPE_ACTION = 1
CHANNEL_TEXT_MESSAGE_TYPE_NOTICE = 2
CHANNEL_TEXT_MESSAGE_TYPE_AUTO_REPLY = 3

CHANNEL_TEXT_SEND_ERROR_UNKNOWN = 0
CHANNEL_TEXT_SEND_ERROR_OFFLINE = 1
CHANNEL_TEXT_SEND_ERROR_INVALID_CONTACT = 2
CHANNEL_TEXT_SEND_ERROR_PERMISSION_DENIED = 3
CHANNEL_TEXT_SEND_ERROR_TOO_LONG = 4

CHANNEL_GROUP_CHANGE_REASON_NONE = 0
CHANNEL_GROUP_CHANGE_REASON_OFFLINE = 1
CHANNEL_GROUP_CHANGE_REASON_KICKED = 2
CHANNEL_GROUP_CHANGE_REASON_BUSY = 3
CHANNEL_GROUP_CHANGE_REASON_NONE = 4

CHANNEL_GROUP_FLAG_CAN_ADD = 1
CHANNEL_GROUP_FLAG_CAN_REMOVE = 2
CHANNEL_GROUP_FLAG_CAN_RESCIND = 4
CHANNEL_GROUP_FLAG_MESSAGE_ADD = 8
CHANNEL_GROUP_FLAG_MESSAGE_REMOVE = 16
CHANNEL_GROUP_FLAG_MESSAGE_ACCEPT = 32
CHANNEL_GROUP_FLAG_MESSAGE_REJECT = 64
CHANNEL_GROUP_FLAG_MESSAGE_RESCIND = 128
CHANNEL_GROUP_FLAG_CHANNEL_SPECIFIC_HANDLES = 256

CHANNEL_HOLD_STATE_NONE = 0
CHANNEL_HOLD_STATE_SEND_ONLY = 1
CHANNEL_HOLD_STATE_RECV_ONLY = 2
CHANNEL_HOLD_STATE_BOTH = 3

CHANNEL_PASSWORD_FLAG_PROVIDE = 8

MEDIA_STREAM_TYPE_AUDIO = 0
MEDIA_STREAM_TYPE_VIDEO = 1

MEDIA_STREAM_DIRECTION_NONE = 0
MEDIA_STREAM_DIRECTION_SEND = 1
MEDIA_STREAM_DIRECTION_RECEIVE = 2
MEDIA_STREAM_DIRECTION_BIDIRECTIONAL = 3

MEDIA_STREAM_ERROR_UNKNOWN = 0
MEDIA_STREAM_ERROR_EOS = 1

MEDIA_STREAM_BASE_PROTO_UDP = 0
MEDIA_STREAM_BASE_PROTO_TCP = 1

MEDIA_STREAM_TRANSPORT_TYPE_LOCAL = 0
MEDIA_STREAM_TRANSPORT_TYPE_DERIVED = 1
MEDIA_STREAM_TRANSPORT_TYPE_RELAY = 2

MEDIA_STREAM_STATE_STOPPED =0
MEDIA_STREAM_STATE_PLAYING = 1
MEDIA_STREAM_STATE_CONNECTING = 2
MEDIA_STREAM_STATE_CONNECTED = 3

PROPERTY_FLAG_READ = 1
PROPERTY_FLAG_WRITE = 2

