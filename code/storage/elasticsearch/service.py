import logging
from stack.cloudformation.service import StackServiceProvider
from stack.cloudformation.cloudformation_keys import ElasticsearchStackKeys, MainStackKeys
from compute.security_group.wrapper import SecurityGroupWrapper
from compute.security_group.wrapper import IngressAlreadyExistsException


LOGGER = logging.getLogger(__name__)


class ElasticsearchService:

    DESCRIPTION = 'Nginx access to Elasticsearch Domain'

    def __init__(self, cloudformation_service: StackServiceProvider):
        # Setup Security Group Service
        self.elasticsearch_stack_output = cloudformation_service.elasticsearch_stack.get_outputs()
        self.main_stack_output = cloudformation_service.main_stack.get_outputs()
        self.security_group_id = self.elasticsearch_stack_output[ElasticsearchStackKeys.es_security_group_id_key]

    def add_elastic_search_ingress_rule(self, ingress_port, protocol):
        security_group_wrapper = SecurityGroupWrapper(security_group_id=self.security_group_id)
        user_id = self.main_stack_output[MainStackKeys.user_id]

        build_ip_permissions = security_group_wrapper.build_ip_permissions(
            from_port=ingress_port,
            to_port=ingress_port,
            ip_protocol=protocol,
            description=self.DESCRIPTION,
            security_group_id=self.security_group_id,
            user_id=user_id
        )
        try:
            security_group_wrapper.add_ingress(
                ip_permissions=build_ip_permissions
            )
        except IngressAlreadyExistsException as exc:
            LOGGER.debug(exc)
