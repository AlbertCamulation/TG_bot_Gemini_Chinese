
from custom_functions.tg_check_user import check_user

from  variable import Globals as global_var

import logging,os,json
# import asyncio,random,time
from datetime import datetime
from telegram.constants import ChatAction,ParseMode
from telegram import __version__ as TG_VER

from pyquery import PyQuery as pq 

try:
  from telegram import __version_info__
except ImportError:
  __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
  raise RuntimeError(
    f"This example is not compatible with your current PTB version {TG_VER}. To view the "
    f"{TG_VER} version of this example, "
    f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
  )
from telegram import (
  # ForceReply, 
  # InlineQueryResultArticle, 
  # InputTextMessageContent, 
  # InputFile,
  InlineKeyboardButton, 
  InlineKeyboardMarkup,
  # KeyboardButton,
  # KeyboardButtonPollType,
  # Poll,
  # ReplyKeyboardMarkup,
  # ReplyKeyboardRemove,
  Update)
from telegram.ext import (
  Application,
  CallbackQueryHandler,
  CommandHandler,
  CallbackContext,
  ContextTypes,
  filters,
  MessageHandler
  # ConversationHandler,
  # PollAnswerHandler,
  # PollHandler,
)

# 啟用日誌記錄
logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# 設置 httpx 的日誌記錄等級為更高，避免所有 GET 和 POST 請求都被記錄
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
# 設置日誌格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 創建文件日誌記錄器
file_handler = logging.FileHandler(global_var.file_handler_logging_FileHandler_path)
file_handler.setLevel(logging.DEBUG)  # 設置文件日誌的記錄等級

# 將格式應用於文件處理程序
file_handler.setFormatter(formatter)

# 為 logger 添加文件處理程序
# 在文件的其他地方设置 logger，例如在全局范围或在函数之外
logger.addHandler(file_handler)

# logger critical func
def log_the_critical(user):
  logger.critical(
      f"uid={user.id},first_name={user.first_name},is_bot={user.is_bot},username={user.username},is_premium={user.is_premium}，未經授權使用。"
  )

# async 00 _ THE SAMPLE OF FUNCTIONS
async def function_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  user = update.effective_user
  check_usr = check_user(user,'normal')

  if check_usr['bool'] == False:
    log_the_critical(user)
    await update.message.reply_html(check_usr['text'])
    return
  
  #####
  # Your Code Here!!! #
  #####

# async 01 _ help
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text("NOBODY WILL HELP YOU AND GO FUCK YOURSELF")

# async 07 _ handle_document
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  user = update.effective_user
  check_usr = check_user(user,'critical')

  if check_usr['bool'] == False:
    log_the_critical(user)
    await update.message.reply_html(check_usr['text'])
    return
  
  await update.message.reply_text("執行上傳檔案程序中...")
  # 获取文件对象
  document = update.message.document
  # 获取文件信息
  try:
    file_id = document.file_id
  except:
    await update.message.reply_text(f"Sry about that. NOT support this shit.")
    return
  file_name = document.file_name
  # 檢查副檔名是否在允許的列表中
  allowed_extensions = {".key", ".pem", ".crt",".xlsx"}
  if any(file_name.lower().endswith(ext) for ext in allowed_extensions):
    logger.info("文件上傳成功！")
  else:
    await update.message.reply_text("不允許上傳該類型的文件。")
    return
  # 使用 context.bot.get_file 方法获取文件对象
  file = await context.bot.get_file(file_id)
  
  # 下载文件到本地驱动
  file_path = os.path.join(global_var.UPLOADS_DIR, f"{file_name}")
  try:
    await file.download_to_drive(custom_path=file_path)
  except Exception as e:
    await update.message.reply_text(f"{e}\nPlease retry.")
    logger.error(e)

  # 处理文件内容
  with open(file_path, 'rb') :
    await update.message.reply_text(f"{file_name} downloaded to local drive.")

# async 11 _ handle_text
# 处理用户输入的文本消息。
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  from custom_functions.tg_handle_message import tg_handle_message
  """处理用户输入的文本消息。"""
  user = update.effective_user
  user_input = update.message.text
  
  check_usr = check_user(user,'normal')
  logger.info(f"User {update.effective_user.id} input: {user_input}")
  if check_usr['bool'] == False:
    log_the_critical(user)
    await update.message.reply_html(check_usr['text'])
    return
  
  result =tg_handle_message(user_input)
  if result['special']=='default':
    final_text=result['result']
    try:
      await update.message.reply_text(text=final_text, parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
      print(e)
    return
  elif result['special']=='gemini':
    try:
      await update.message.reply_text(text=result['result'], parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
      try:
        result=result['result'].replace('*','')
        logger.info (result)
        await update.message.reply_text(text=f"{result}", parse_mode=ParseMode.MARKDOWN_V2)
      except  Exception as e:
        await update.message.reply_text(text=f"{e}")
    return 


def main() -> None:
  """運行機器人."""
  application = Application.builder().token(global_var.TOKEN_Telegram).build()

  # MessageHandler
  application.add_handler(MessageHandler(filters.TEXT& ~filters.COMMAND, handle_text))
  application.add_handler(MessageHandler(filters.ATTACHMENT, handle_document))

  # CommandHandler
  application.add_handler(CommandHandler("help", help_handler))
  
  # 在uploads目录中创建文件夹以保存上传的文件
  os.makedirs(global_var.UPLOADS_DIR, exist_ok=True)
  
  logger.info("### Application is running ... ###")
  # run_polling
  application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
  main()