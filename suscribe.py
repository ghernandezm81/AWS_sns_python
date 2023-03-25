from connection import sns_client

response = sns_client.subscribe(
    TopicArn="arn:aws:sns:us-east-2:809090633799:Publicidad",
    Protocol="email",
    Endpoint="sppug2@hotmail.com",
    ReturnSubscriptionArn=True
)

print(response)
