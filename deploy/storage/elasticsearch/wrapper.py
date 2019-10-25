
import logging
import boto3

LOGGER = logging.getLogger(__name__)


class ElasticsearchWrapper:
    CLIENT = boto3.client('es')

    def __init__(self, domain_name: str):
        self.domain_name = domain_name

    def add_cognito_pool(self, cognito_pool_id: str, identity_pool_id: str, role_arn: str):
        self.CLIENT.update_elasticsearch_domain_config(
            DomainName=self.domain_name,
            CognitoOptions={
                'Enabled': True,
                'UserPoolId': cognito_pool_id,
                'IdentityPoolId': identity_pool_id,
                'RoleArn': role_arn
            }
        )
