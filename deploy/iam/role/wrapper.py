import boto3


class RoleWrapper:
    CLIENT = boto3.client('iam')

    def __init__(self, role_name):
        self.role_name = role_name

    def get_role_attribute(self, attribute):
        # Attributes should be based off the value of the role dict object that is
        # returned from the get_role function shown here:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_role
        role_key = 'Role'

        role = self.CLIENT.get_role(RoleName=self.role_name)

        return role.get(role_key).get(attribute)
