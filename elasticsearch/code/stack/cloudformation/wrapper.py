# pylint: disable=no-member
import boto3

RESOURCE = boto3.resource('cloudformation')


class CloudFormationWrapper:
    def __init__(self, stack_name: str):
        self.stack_name = stack_name
        self.stack = RESOURCE.Stack(self.stack_name)

    def get_outputs(self):
        output_key = 'OutputKey'
        output_value_key = 'OutputValue'

        outputs = self.stack.outputs
        formatted_output = {}
        for item in outputs:
            formatted_output = {
                **{item[output_key]: item[output_value_key]},
                **formatted_output
            }

        return formatted_output
