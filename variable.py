class Globals:
  
  ####### TOKEN #######
  TOKEN_Telegram = '?'
  TOKEN_Gemini='?'

  ####### UID #######
  uid_myself_tg='?'
  allowed_user_ids_critical=[uid_myself_tg]
  allowed_user_ids=[
    '?',
    uid_myself_tg
  ]  

  ####### PATH #######
  custom_front_head='?'
  
  # Logger 位置
  file_handler_logging_FileHandler_path=custom_front_head+'log/access.log'

  # 用于保存上传文件的路径
  UPLOADS_DIR = custom_front_head+'uploads'
  
 