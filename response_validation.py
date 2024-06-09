import json 

resp = '''{
    'IsTruncated': True|False,
    'Marker': 'string',
    'NextMarker': 'string',
    'Contents': [
        {
            'Key': 'string',
            'LastModified': 2015-01-01T00:00:00,
            'ETag': 'string',
            'ChecksumAlgorithm': [
                'CRC32'|'CRC32C'|'SHA1'|'SHA256',
            ],
            'Size': 123,
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'OUTPOSTS'|'GLACIER_IR'|'SNOW',
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            },
            'RestoreStatus': {
                'IsRestoreInProgress': True|False,
                'RestoreExpiryDate': 2015-01-01T00:00:00
            }
        },
    ],
    'Name': 'string',
    'Prefix': 'string',
    'Delimiter': 'string',
    'MaxKeys': 123,
    'CommonPrefixes': [
        {
            'Prefix': 'string'
        },
    ],
    'EncodingType': 'url',
    'RequestCharged': 'requester'
}'''
resp_nw = resp.replace("\'", "\"")
print(resp_nw)
resp_dict = json.loads(resp_nw)
print(resp_dict["Contents"])
