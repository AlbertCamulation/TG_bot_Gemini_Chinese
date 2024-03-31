

from custom_functions.tg_escape_markdown import escape

def tg_handle_message(user_input):
  result={'special':'default', 'result': ''}

  if 'markdownv2' in user_input:
    output='''
messageEntityBold =>  *bold*
messageEntityItalic => _italic_
messageEntityCode => `code`
messageInlineURL=> [inline URL](https://google.com.tw)
messageEntityPre => 
```python
print('Hello World')
```
'''
  else:
    from custom_functions.tg_gemini import tg_gemini
    print('use Gemini')
    try:
      output = tg_gemini(user_input)
    except Exception as e:
      output = str(e)
    # print('虛無')
    
    
  result['result']= escape(output)
  return result