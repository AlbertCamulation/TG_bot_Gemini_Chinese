# 1. 執行 pip 安裝

在終端機輸入以下指令，安裝程式所需的套件：

```
pip install -r requirements.txt
```

# 2. 修改參數

在程式主目錄中，找到檔案 variable.py。此檔案包含程式運作的參數設置。

根據你的需求，修改以下參數：

### 設定 TOKEN
```python
TOKEN_Telegram = '?'
TOKEN_Gemini='???'
```

### 設定白名單
```python
uid_myself_tg='??'
allowed_user_ids_critical=[uid_myself_tg]
allowed_user_ids=[
    '???',
    uid_myself_tg
]  
```

### 設定 Log 路徑
```python
custom_front_head='??'
```

請將路徑和參數替換為你的實際設定。