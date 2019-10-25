import logging
import os
from shared.app_context import BaseContext
from stack.cloudformation.service import StackServiceProvider
from authentication.cognito.service import CognitoService
from iam.role.wrapper import RoleWrapper


class ElasticSearchContext(BaseContext):
    def configure_settings(self):
        self.stack_name = os.environ.get("MainStackName")
        self.elasticsearch_stack_name = os.environ.get('ElasticSearchStackName')
        self.cognito_stack_name = os.environ.get('CognitoStackName')
        self.nginx_stack_name = os.environ.get('NginxStackName')
        self.kibana_domain = os.environ.get('KibanaDomain')
        self.role_name = os.environ.get('CognitoRoleName')

    def configure_services(self):
        # Cloudformation Stacks
        self.stack_service = StackServiceProvider(
            main_stack=self.stack_name,
            cognito_stack=self.cognito_stack_name,
            elasticsearch_stack=self.elasticsearch_stack_name,
            nginx_proxy_stack=self.nginx_stack_name
        )

        self.cognito_service = CognitoService(cloudformation_service=self.stack_service)
        self.role_wrapper = RoleWrapper(role_name=self.role_name)


APP_CONTEXT = ElasticSearchContext()
LOGGER = logging.getLogger()
LOGGER.info("graph query lambda_invocation_handler app context: %s", APP_CONTEXT)


def config_cognito_for_elasticsearch(event, context):
    msg = f'No Lambda Inputs Required. Ignoring anything in event: {event}'
    LOGGER.debug(msg)
    role_arn_key = 'Arn'
    cognito_role_arn = APP_CONTEXT.role_wrapper.get_role_attribute(attribute=role_arn_key)
    APP_CONTEXT.cognito_service.add_cognito(domain_url=APP_CONTEXT.kibana_domain, cognito_role_arn=cognito_role_arn)

    return 'Success'
