# AsiaYo_Test
* **第一種方式** 
* ### 先執行 `python test.py` 在本地建立Server

* ### 打開瀏覽器, 在網址輸入'http://127.0.0.1:5000/?source=USD&target=JPY&amount=$1,525'

* **第二種方式** 
* ### 先執行 `python test.py` 在本地建立Server

* ### 在執行`python request_get.py '參數'`

### !! 參數在外面加入''(單引號) !! 
### Ex: `python request_get.py '?source=USD&target=JPY&amount=$1,525'`

* **第三種方式**
* ### 先執行 `python test.py` 在本地建立Server
 
* ### 在Linux Server上輸入`curl http://[本機地址]:5000/'?source=USD&target=JPY&amount=$1,525'`
  ![圖片](https://github.com/zelunlun/AsiaYo_Test/assets/96367374/ba4334ae-256c-4797-8ddb-39fd2b3806a9)
