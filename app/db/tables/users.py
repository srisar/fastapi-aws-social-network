from app.db.client import get_dynamodb_resource


def create_users_table():
    """
    Creates a new users table in dynamodb.
    """

    try:

        dynamodb = get_dynamodb_resource()

        print(dynamodb)

        table = dynamodb.create_table(
            TableName="apaluma-users",
            KeySchema=[
                {
                    "AttributeName": "user_id",
                    "KeyType": "HASH",
                },
                {
                    "AttributeName": "username",
                    "KeyType": "RANGE",
                },
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "user_id",
                    "AttributeType": "S",
                },
                {
                    "AttributeName": "username",
                    "AttributeType": "S",
                },
                {
                    "AttributeName": "email",
                    "AttributeType": "S",
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "email-index",
                    "KeySchema": [
                        {
                            "AttributeName": "email",
                            "KeyType": "HASH",
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL",
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5,
                    },
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )

        table.meta.client.get_waiter("table_exists").wait(TableName="apaluma-users")

        print("Table created")

    except Exception as e:
        raise e


if __name__ == "__main__":
    create_users_table()
