class CognitoStackKeys:
    cognito_auth_role_key = 'CognitoAuthIamRole'
    cognito_domain_key = 'CognitoUserPoolArn'
    cognito_pool_id_key = 'CognitoIdentityPoolId'
    cognito_pool_name_key = 'CognitoIdentityPoolName'
    cognito_unauth_role_key = 'CognitoUnauthIamRole'
    cognito_user_pool_name_key = 'CognitoUserPool'
    cognito_user_pool_arn_key = 'CognitoUserPoolArn'
    cognito_user_pool_client_id_key = 'CognitoUserPoolClientId'


class NginxProxyStackKeys:
    nginx_code_deploy_app_key = 'NginxCodeDeployApplication'
    nginx_code_deploy_deployment_config_key = 'NginxCodeDeployDeploymentConfig'
    nginx_code_deploy_deployment_group_key = 'NginxCodeDeployDeploymentGroup'
    nginx_elastic_ip_key = 'NginxElasticIp'
    nginx_internal_ip_key = 'NginxInternalIp'
    nginx_proxy_dns_key = 'NginxProxyDNS'
    nginx_proxy_listener_key = 'NginxProxyListener'
    nginx_proxy_load_balancer_key = 'NginxProxyLoadBalancer'
    nginx_proxy_security_group_1_key = 'NginxProxySecurityGroup1'
    nginx_proxy_security_group_2_key = 'NginxProxySecurityGroup2'
    nginx_proxy_stack_name_key = 'NginxProxyStackName'
    nginx_proxy_target_group_key = 'NginxProxyTargetGroup'


class ElasticsearchStackKeys:
    es_domain_arn_key = 'ElasticsearchDomainArn'
    es_domain_endpoint_key = 'ElasticsearchDomainEndpoint'
    es_security_group_id_key = 'ElasticsearchSecurityGroupId'
    es_stack_name_key = 'ElasticsearchStackName'
    es_subnet_id_1_key = 'ElasticsearchSubnetId1'
    es_subnet_id_2_key = 'ElasticsearchSubnetId2'
    es_kibana_endpoint_key = 'KibanaEndpoint'


class MainStackKeys:
    env = 'Environment'
    user_id = 'UserId'
