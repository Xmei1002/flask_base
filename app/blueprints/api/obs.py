from . import api
from flask import request, current_app
from app.utils.api_utils import RET, json_response, handle_api_call
from app.services import hwobs_service
from app.services.auth_service import token_auth
from app.schemas.hwobs_schemas import HWOBSSchema

@api.route('/upload', methods=['POST'])
@handle_api_call
def upload_obs_file():
  '''
    上传文件
  '''
  schema = HWOBSSchema()
  data = schema.load(request.files)
  file = data.get('file')
  file_name = file.filename
  print("=======")
  print(file,file_name)
  hwobs_service.upload_file(file,file_name)
