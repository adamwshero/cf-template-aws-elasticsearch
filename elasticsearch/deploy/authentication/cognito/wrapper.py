import logging
import boto3

LOGGER = logging.getLogger(__name__)


class CognitoIdentityException(Exception):
    pass


class CognitoIdentityProviderWrapper:
    CLIENT = boto3.client('cognito-idp')

    def __init__(self, user_pool_id: str):
        self.user_pool_id = user_pool_id

    def add_domain(self, domain_url: str) -> dict:
        try:
            response = self.CLIENT.create_user_pool_domain(
                Domain=domain_url,
                UserPoolId=self.user_pool_id
            )
        except self.CLIENT.exceptions.InvalidParameterException as exc:
            msg = f'Unable to add Domain url for User Pool Id: {self.user_pool_id}. {exc}'
            LOGGER.error(msg)
            raise CognitoIdentityException(msg)


        return response

    def remove_domain(self, domain_url: str) -> dict:
        response_key = 'DomainDescription'
        user_pool_key = 'UserPoolId'

        response = self.CLIENT.describe_user_pool_domain(
            Domain=domain_url
        )

        if response_key not in response:
            msg = f'Unable to remove domain url from Cognito pool: {self.user_pool_id}'
            LOGGER.error(msg)
            raise CognitoIdentityException(msg)

        response = self.CLIENT.delete_user_pool_domain(
            Domain=domain_url,
            UserPoolId=response.get(response_key).get(user_pool_key)
        )

        return response


class CognitoUserPoolWrapper:
    CLIENT = boto3.client('cognito-identity')

    def __init__(self, identity_pool_id):
        self.identity_pool_id = identity_pool_id

    def add_roles(self, roles: dict):
        self.CLIENT.set_identity_pool_roles(
            IdentityPoolId=self.identity_pool_id,
            Roles=roles
        )

    def get_roles(self) -> dict:
        roles_key = 'Roles'
        response = self.CLIENT.get_identity_pool_roles(
            IdentityPoolId=self.identity_pool_id
        )

        return response[roles_key]
