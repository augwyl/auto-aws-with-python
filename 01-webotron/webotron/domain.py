#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

"""Classes for Route53 domains."""
from pprint import pprint

class DomainManager:
    """Manage a Route53 domain."""
    def __init__(self, session):
        """Create DomainManager object."""
        self.session = session
        self.client = self.session.client('route53')

    def find_hosted_zone(self, domain_name):
        paginator = self.client.get_paginator('list_hosted_zones')
        for page in paginator.paginate():
            for zone in page['HostedZones']:
                if domain_name.endswith(zone['Name'][:-1]):
                    return zone

# domain_name = 'subdomain.autobot.augwyl.com'
# zone_name = 'augywl.com.'
    def create_hosted_zone(self, domain_name):
        zone_name = domain_name.split('.')[-2:] + '.'
        return self.client.create_hosted_zone(
            Name=zone_name,
            CallerReference=str(uuid.uuid4())
        )
