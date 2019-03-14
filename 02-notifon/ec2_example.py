# coding: utf-8
get_ipython().run_line_magic('history', '')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key_name = 'python_autom_key'
key_name = 'python_auto_key'
key = ec2.create_key_pair(KeyName=key_name)
key_name = 'python_automation_key1'
key = ec2.create_key_pair(KeyName=key_name)
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key1.pem')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', '-ltr')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-ltr')
img
inst
ec2.images.filter(Owners=['amazon'])
img = ec2.Image('ami-922914f7')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-922914f7')
img_apse2.name
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20180508-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
img.id
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img = ec2.Image('ami-423bec20')
img
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst
inst.public_dns_name
inst.wait_until_running
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
# Look up the security group
# Authorize incoming connections from our public IP address, on port 22 (the port SSH uses)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '121.200.26.109/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
