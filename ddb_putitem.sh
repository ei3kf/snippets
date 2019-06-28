aws --region us-east-1 dynamodb get-item --table-name AAAA --key '{ "Wload": {"S": "00-X"} }'
aws --region us-east-1 dynamodb put-item --table-name AAAA --item '{"Wload": {"S": "00-X"}, "Profile": {"S": "Large"}}'
aws --region us-east-1 dynamodb get-item --table-name AAAA --key '{ "Wkload": {"S": "00-X"} }'
