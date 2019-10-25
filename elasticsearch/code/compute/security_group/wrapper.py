# pylint: disable=no-member
import logging
import boto3

LOGGER = logging.getLogger(__name__)


class IngressAlreadyExistsException(Exception):
    pass


class SecurityGroupWrapper:
    CLIENT = boto3.client('ec2')
    RESOURCE = boto3.resource('ec2')

    def __init__(self, security_group_id: str):
        self.security_group_id = security_group_id
        self.security_group = self.RESOURCE.SecurityGroup(self.security_group_id)

    def add_ingress(self, ip_permissions: dict):
        try:
            self.security_group.authorize_ingress(
                IpPermissions=ip_permissions
            )
        except self.CLIENT.exceptions.ClientError as exc:
            if 'already exists' in str(exc):
                msg = f'Unable to add security group ingress Id: {self.security_group_id}. {exc}'
                LOGGER.error(msg)
                raise IngressAlreadyExistsException(msg)

    @staticmethod
    def build_ip_permissions(
            description: str, from_port: int, to_port: int, ip_protocol: str, security_group_id: str, user_id: str
    ):
        return [
            {
                'FromPort': int(from_port),
                'IpProtocol': ip_protocol.lower(),
                'ToPort': int(to_port),
                'UserIdGroupPairs': [
                    {
                        'Description': description,
                        'GroupId': security_group_id,
                        'UserId': user_id
                    }
                ]
            }
        ]
