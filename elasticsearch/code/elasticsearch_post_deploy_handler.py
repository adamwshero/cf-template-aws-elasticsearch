import logging
import os
from shared.app_context import BaseContext
from stack.cloudformation.service import StackServiceProvider
from storage.elasticsearch.service import ElasticsearchService


class ElasticSearchContext(BaseContext):
    def configure_settings(self):
        self.es_stack_name = os.environ.get("MainStackName")
        self.es_elasticsearch_stack_name = os.environ.get('ElasticSearchStackName')
        self.cognito_stack_name = os.environ.get('CognitoStackName')
        self.nginx_stack_name = os.environ.get('NginxStackName')
        self.ingress_port = os.environ.get('IngressPort')
        self.protocol = os.environ.get('Protocol')

    def configure_services(self):
        # Cloudformation Stacks
        self.stack_service = StackServiceProvider(
            main_stack=self.es_stack_name,
            cognito_stack=self.cognito_stack_name,
            elasticsearch_stack=self.es_elasticsearch_stack_name,
            nginx_proxy_stack=self.nginx_stack_name
        )

        self.elasticsearch_service = ElasticsearchService(cloudformation_service=self.stack_service)


APP_CONTEXT = ElasticSearchContext()
LOGGER = logging.getLogger()
LOGGER.info("graph query lambda_invocation_handler app context: %s", APP_CONTEXT)


def config_cognito_for_elasticsearch(event, context):
    msg = f'No Lambda Inputs Required. Ignoring anything in event: {event}'
    LOGGER.debug(msg)
    APP_CONTEXT.elasticsearch_service.add_elastic_search_ingress_rule(
        ingress_port=APP_CONTEXT.ingress_port,
        protocol=APP_CONTEXT.protocol
    )

    return 'Success'
