# coding: utf-8

import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon auto group', PolicyName='Scale up')
as_client.execute_policy(AutoScalingGroupName='Notifon auto group', PolicyName='Scale down')
