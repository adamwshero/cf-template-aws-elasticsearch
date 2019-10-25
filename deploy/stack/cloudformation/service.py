from stack.cloudformation.wrapper import CloudFormationWrapper


class StackServiceProvider:
    def __init__(
            self,
            main_stack: 'str',
            elasticsearch_stack: 'str',
            cognito_stack: 'str',
            nginx_proxy_stack: 'str'
    ):
        self.main_stack = CloudFormationWrapper(stack_name=main_stack)
        self.elasticsearch_stack = CloudFormationWrapper(stack_name=elasticsearch_stack)
        self.cognito_stack = CloudFormationWrapper(stack_name=cognito_stack)
        self.nginx_proxy_stack = CloudFormationWrapper(stack_name=nginx_proxy_stack)
