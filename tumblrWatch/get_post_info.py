from tumblrWatch import get_client_connection
import pprint

client = get_client_connection()

d = client.info()
pp = pprint.PrettyPrinter(indent=2)

posts = client.posts(blogname='5-y-p', reblog_info=True, notes_info=True)
pp.pprint(posts)

