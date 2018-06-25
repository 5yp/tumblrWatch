from tumblrWatch import get_client_connection

client = get_client_connection()

d = client.info()
print(d)

results = client.tagged(tag="pharmercy", before=1410000000, limit=20)
for result in results:
    print(result['id'], result['timestamp'], result['date'], result['blog_name'], result['tags'])
