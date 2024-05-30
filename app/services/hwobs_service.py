from flask import current_app
from obs import ObsClient
from obs import PutObjectHeader
import os
import traceback
from app.utils.file_upload import get_storage_path

ak = os.getenv("HW_Access_Key_ID")
sk = os.getenv("HW_Secret_Access_Key")
server = "https://obs.cn-north-4.myhuaweicloud.com"
obsClient = ObsClient(access_key_id=ak, secret_access_key=sk, server=server)

def upload_file(file,file_name):
  try:
      # 读取文件流
      content = open(file, 'rb')
      bucketName = "storage-bucket-2024"
      objectKey = get_storage_path(file_name)
      print('=====')
      print(objectKey)
      # 流式上传
      resp = obsClient.putContent(bucketName, objectKey, content)

      # 返回码为2xx时，接口调用成功，否则接口调用失败
      if resp.status < 300:
          print('Put Content Succeeded')
          print('requestId:', resp.requestId)
      else:
          print('Put Content Failed')
          print('requestId:', resp.requestId)
          print('errorCode:', resp.errorCode)
          print('errorMessage:', resp.errorMessage)
  except:
      print('Put Content Failed')
      print(traceback.format_exc())