#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
import click
from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')

@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass

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

if __name__ == '__main__':
    cli()
