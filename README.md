<div align=center>

<img src="logo.png" width="50px" height="50px">

# Sparduino
在Arduino顯示Spotify目前播放音樂
</div>

![](banner.jpg)

## 安裝

* 請先安裝 `Adafruit_SSD1306` (詢問是否要安裝其依賴請點是)
* 使用任意方法將`[code.ino](code.ino)`燒入至任意Arduino。若使用其他顯示器請自行微調程式。

## 使用

至release下載`Sparduino.exe`並開啟  
以下為範例介面:
```
╦ 歡迎使用 Sparduino
║
╠ 目前可用接口:
╠═ COM5 - USB-SERIAL CH340 (COM5)
╠═ COM6 - USB-SERIAL CH340 (COM6)
║
╚ 輸入數字: 5
╔ PLEEG
╚ Alive
```

### 自行配置

1. 下載`app.py`並安裝依賴套件
2. 在`app.py`20行加入client_id和client_secret
  * 到 [Spotify 開發人員儀表板](https://developer.spotify.com/dashboard/)並使用您的 Spotify 帳戶登錄
  * 單擊“創建應用程序”按鈕並填寫表格以創建新應用程序。 為您的應用程序命名和描述，並指定任何相關的應用程序設置。
  * 創建應用程序後，您應該會看到一個包含應用程序名稱和詳細信息的頁面。 向下滾動到“Client ID”和“Client Secret”部分並記下這些值。
2. 在終端機cd到下載路徑並執行檔案`python app.py`
