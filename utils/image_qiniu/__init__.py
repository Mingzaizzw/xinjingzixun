# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'y8hAvcd29fiTJdEPFBSo98nDvrP9kBe6DLQuYT2_'
secret_key = 'edWBs5jLhCS88u4ax07y3gZLZR8roiHvlZp2eA2m'

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 要上传的空间
bucket_name = 'xinjingzixunwenyiming'

# 上传后保存的文件名
key = 'my-python-logo.png'

# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

# 要上传文件的本地路径
localfile = './bbb.png'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
