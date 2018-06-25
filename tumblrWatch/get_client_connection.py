import pytumblr

'''
OAuth Consumer Key:
EUMJV900zfGqpXFxFDHgSjosWTCr7VjJNMSImoDJ4Mre6iMwVj

Secret Key:
OtqkjJGrlGBpK9hfge2UYVxPLVxTzHflpdI3MmSQLIONUwRyWc
'''

def get_client() :
    # Authenticate via OAuth
    client = pytumblr.TumblrRestClient(
      consumer_key='EUMJV900zfGqpXFxFDHgSjosWTCr7VjJNMSImoDJ4Mre6iMwVj',
      consumer_secret='OtqkjJGrlGBpK9hfge2UYVxPLVxTzHflpdI3MmSQLIONUwRyWc',
      oauth_token='lmhy82Isfn3JNBAF71h5yRHecnqK8gywu1NRfEA8dhkTlQ0Zl0',
      oauth_secret='ksikeI2VwJv27hYL1JyEl4vlLCe6OpZhmGDSEqiRfkQZD5pZSt'
    )
    return client
