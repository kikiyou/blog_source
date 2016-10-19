# 關閉VirtualBox Host與Guest之間的時間同步

基本上，VirtualBox灌好之後，Host OS與Guest OS之間，就會自動開啟時間同步，也就是你在Host OS改了時間，Guest OS就會自動去更新成這個新的時間。但有些時刻，我們會想要讓這兩者之間的時間是不同步的，這時候就需要GetHostTimeDisabled這個功能出場了。


GetHostTimeDisabled這個變數並沒有任何的GUI介面可以去設定，唯一可以處理的就是回歸到VBoxManage.exe來運行。如果你沒有將VBoxManage.exe設定成全域可運行的話，那麼請自行切換到VirtualBox預設目錄去處理。接下來請大家打開cmd切到console模式吧！

列舉你目前電腦下所有的VM Guest OS
C:\Users\Administrator>VBoxManage list vms
"PC 000" {3c279b5b-7f47-4663-86ed-435e9e0dbba8}
"PC 001" {85eb55b3-7c6f-47d5-9273-42564c0ed795}
"PC 002" {e4e1de06-c508-4d71-93a3-d373ee9b9de7}
"PC 003" {4a9bf0d6-b7dc-4d97-ba85-9b65db7ec84b}
"PC 004" {7315c768-a353-4604-bb57-dbd5505724fc}
"PC 005" {7c96a6c8-c8ea-4fb6-8ced-fa8b55ff4be9}
"PC 006" {329bb2d9-1d07-4d8f-993e-fdae3bdf1d54}
對你想要禁止時間同步的Guest OS開刀
比對上例，假設我們想要對PC 006這一台電腦進行時間同步的禁止，那麼我們要下這樣的指令：
``` bash
VBoxManage setextradata "PC 006" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" "1"
```
改完之後，如果沒有任何的錯誤資訊，把Guest OS關機，然後Host OS也要重新開機，就完成了！如果有一天想要改回來，那也很簡單，請使用下列的指令來解決即可。

VBoxManage setextradata "PC 006" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" "0"