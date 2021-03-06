# -*- coding: utf-8 -*-

__all__ = [ 
    'BASE',
    'LB',
    'TOPOLOGY_MAP'
]

BASE = {
    'INSTALL_PREFIX': '/opt/polaris',

    'SHARED_MEM_HOSTNAME': '127.0.0.1',
    'SHARED_MEM_GENERIC_STATE_KEY': 'polaris_health:generic_state',
    'SHARED_MEM_PPDNS_STATE_KEY': 'polaris_health:ppdns_state',
    'SHARED_MEM_HEARTBEAT_KEY': 'polaris_health:heartbeat',

    'NUM_PROBERS': 50,

    'LOG_LEVEL': 'info',
    'LOG_HANDLER': 'syslog',
    'LOG_HOSTNAME': '127.0.0.1',
    'LOG_PORT': 2222,
}

LB = {}

TOPOLOGY_MAP = {}

