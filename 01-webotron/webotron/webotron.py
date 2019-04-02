#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
import click
from bucket import BucketManager
from domain import DomainManager
session = None
bucket_manager = None
domain_manager = None
#s3 = session.resource('s3')

# decorator
@click.group()
@click.option('--profile', default=None,
               help="Use a given AWS profile.")
def cli(profile):
    """Webotron deploys websites to AWS."""
    global session, bucket_manager, domain_manager
    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    #session = boto3.Session(profile_name='pythonAutomation')
    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)
    domain_manager = DomainManager(session)

@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an s3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)

    bucket_manager.set_policy(s3_bucket)

    bucket_manager.configure_website(s3_bucket)

@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')

def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    #s3_bucket = s3.Bucket(bucket)
    bucket_manager.sync(pathname, bucket)
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket)))

@cli.command('setup-domain')
#@cli.argument('domain')
@click.argument('bucket')
def setup_domain(domain, bucket):
    """Configure DOMAIN to point to BUCKET."""
    zone = domain_manager.find_hosted_zone(domain) \
        or domain_manager.create_hosted_zone(domain)
    print(zone)

if __name__ == '__main__':
    cli()
