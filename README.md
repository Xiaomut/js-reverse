# JS 逆向学习

```py
import execjs
with open(file, 'r', encoding='utf-8') as f:
    r = f.read()
ctx = execjs.compile(r).call(method, params)
```

## 1. 基础方法
### 1.1 XHR 断点

一般 `Ajax` 加载必定有 `Json.Parse()` 解析函数，可根据关键字 `Json.Parse(` 搜索，如果有多个 `js` 文件，则再根据 `XHR` 请求页面里的部分路径搜索

### 1.2 请求参数（sign）， 请求头参数（mcode），请求链接

- 请求参数 `factory1688`
- 请求头参数 `shenzhengxin`
- 请求连接加密 `qimaidata` 
    - 搜索不到相关参数，该部分需要一步步点调试找到出现该参数的位置，再解析

如无法进入js界面，点击 `initiator` 进入主界面，搜索相应变化字段，再解析js，如果有多个js文件，则搜索路径进行筛选

### 1.3 反debug

1. 打开开发者工具弹出工具箱，刷新页面后取消在dubugger处暂停
2. 找对应数据包，解析js

## 2 部分JS细节记录

### 2.1 Crypto加密

安装指令
```cmd
npm install crypto-js
```

导入库函数
```js
const CryptoJS = require('crypto-js')
```

常用有 `Base64`, `Hex`, `AES`, `Utf8` 等，可以参照代码共有类对象替换为 `CryptoJS` 即可

### 2.2 关键字替换

常见有 `navigator`, `window`, `_window` 等

```js
global.navigator = { 'userAgent': 'node.js' }
window = global;
// let window = {

// }
```