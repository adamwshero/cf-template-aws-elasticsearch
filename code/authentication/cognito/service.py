import logging
from authentication.cognito.wrapper import CognitoIdentityProviderWrapper, CognitoUserPoolWrapper, CognitoIdentityException
from stack.cloudformation.service import StackServiceProvider
from stack.cloudformation.cloudformation_keys import CognitoStackKeys, ElasticsearchStackKeys
from storage.elasticsearch.wrapper import ElasticsearchWrapper

LOGGER = logging.getLogger(__name__)


class IdentityPoolRoleException(Exception):
    pass


class CognitoService:
    def __init__(self, cloudformation_service: StackServiceProvider):
        # Wrapper Setup
        self.main_stack_output = cloudformation_service.main_stack.get_outputs()
        self.cognito_stack_output = cloudformation_service.cognito_stack.get_outputs()
        self.elasticsearch_output = cloudformation_service.elasticsearch_stack.get_outputs()

        # Get info from stacks
        self.identity_pool_id = self.cognito_stack_output[CognitoStackKeys.cognito_pool_id_key]
        self.user_pool_id = self.cognito_stack_output[CognitoStackKeys.cognito_user_pool_client_id_key]
        self.auth_role = self.cognito_stack_output[CognitoStackKeys.cognito_auth_role_key]
        self.unauth_role = self.cognito_stack_output[CognitoStackKeys.cognito_unauth_role_key]
        self.domain_arn = self.elasticsearch_output[ElasticsearchStackKeys.es_domain_arn_key]

        # Init Wrappers
        self.cognito_wrapper = CognitoIdentityProviderWrapper(user_pool_id=self.user_pool_id)
        self.cognito_user_pool_wrapper = CognitoUserPoolWrapper(identity_pool_id=self.identity_pool_id)
        self.elastic_search_wrapper = ElasticsearchWrapper(domain_name=self.get_domain_name(domain_arn=self.domain_arn))

    def add_cognito(self, domain_url: str, cognito_role_arn: str):
        # 1. Add the Domain to Cognito
        self.add_domain_url(domain_url=domain_url)

        # 2 Set the Cognito User Pool Roles
        self.set_user_pool_roles(auth_role=self.auth_role, un_auth_role=self.unauth_role)

        # 3 Connect Cognito to the Elasticsearch instance
        self.elastic_search_wrapper.add_cognito_pool(
            cognito_pool_id=self.user_pool_id,
            identity_pool_id=self.identity_pool_id,
            role_arn=cognito_role_arn
        )

    def add_domain_url(self, domain_url: str):
        try:
            msg = f'Adding Domain Url to Cognito'
            LOGGER.debug(msg)
            self.cognito_wrapper.add_domain(domain_url=domain_url)
        except CognitoIdentityException as exc:
            msg = f'Domain Url for Cognito already found. Removing and Adding again. {exc}'
            LOGGER.debug(msg)
            self.cognito_wrapper.remove_domain(domain_url=domain_url)
            self.cognito_wrapper.add_domain(domain_url=domain_url)

    def set_user_pool_roles(self, auth_role, un_auth_role) -> dict:
        roles = self.build_user_pool_roles(auth_role=auth_role, unauth_role=un_auth_role)
        self.cognito_user_pool_wrapper.add_roles(roles=roles)

        found_roles = self.cognito_user_pool_wrapper.get_roles()
        if found_roles != roles:
            msg = f'User Pool Roles were not setup properly for Pool Id: {self.identity_pool_id}'
            LOGGER.error(msg)
            raise IdentityPoolRoleException(msg)

        return found_roles

    @staticmethod
    def build_user_pool_roles(auth_role: str, unauth_role: str):
        return {
            'authenticated': auth_role,
            'unauthenticated': unauth_role
        }

    @staticmethod
    def get_domain_name(domain_arn: str) -> str:
        return domain_arn[domain_arn.find('/')+1:]
