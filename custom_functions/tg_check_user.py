from  variable import Globals as global_var

# #v1
# def check_user(user_id):
#   if str(user_id)in allowed_user_ids:
#     return True
#   else:
#     return False
  
# #critical     
# def check_user_critical(user_id):
#   if str(user_id)in allowed_user_ids_critical:
#     return True
#   else:
#     return False

#v3
def check_user(user,level):
  if level == 'critical':
    check_usr_list= global_var.allowed_user_ids_critical
  elif  level == 'normal':
    check_usr_list= global_var.allowed_user_ids
  
  if str(user.id)in check_usr_list:
    return {'bool':True}
  else:
    return {'bool':False,'text':f'你哪位？\n{user.mention_html()} 滾吧！'}