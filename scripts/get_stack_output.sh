#!/bin/bash
#mkdir -p home/es-config/config #I think you can remove this, verify and then delete, please
aws cloudformation describe-stacks \
--stack-name dev-dhi-profile-acq-es \
--query "Stacks[0].Outputs[?OutputKey=='ElasticsearchDomainEndpoint' || OutputKey=='KibanaEndpoint' || OutputKey=='Environment']" \
--region us-east-1 \
> /home/es-config/es-stack-output.json