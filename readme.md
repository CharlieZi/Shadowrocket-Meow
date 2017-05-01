## Other Rules

用来用去发现大道至简，去广告效果其实不好，索性就用MEOW的逻辑。
同时小火箭也是iOS下支持DNS、Host的好梯子，不如就开个Host的坑，后续更新可能不会那么勤快，毕竟自有国情在。规则都为自用，一些自己常用的规则会逐步添加，一切的逻辑就是用到再说，有问题开Issue。

## 两种逻辑

- 境外IP 全部走代理

**规则地址：**<https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/MeowList.conf>

![地址扫码](https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/QR/MeowList.png)

- 全部直连，只用Host

  **规则地址：**<https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/QR/Host-list.conf>

<<<<<<< HEAD
![地址扫码](https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/QR/Host-list.png)

=======
-   默认只对 `被墙` 且 `世界前 500` 的网站进行代理。
-   在 SR 中如果将 `全局路由` 设置为 `代理`，则变为代理所有非大陆网站。\*
-   广告过滤，包括网页广告、App 广告和视频广告。
-   严格控制规则的体积，毕竟这是每次数据请求都会被运行一次的东西。
-   使用开源的力量，逐渐成为 SR 上最好用的规则！

\* 本规则默认模式应为 `配置`，如果只是需要长期地代理所有非大陆网站，本规则并不是最佳方案。

**规则地址：**<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_adb.conf>
>>>>>>> h2y/master

- 开发用List,不保证能用

  **规则地址：**<https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/develop/devList.conf>

![地址扫码](https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/QR/devList.png)




## 计划

- 增加Apple DNS

- 代码重构，现在的太简陋了

## 感谢

- host列表来自 一键go host
- 




**问题反馈**

<<<<<<< HEAD

=======
任何问题欢迎在 [Issues](https://github.com/h2y/Shadowrocket-ADBlock-Rules/issues) 中反馈，如果没有账号可以去 [我的网站](https://hzy.pw/p/2096#comments) 中留言。


## 捐助

本项目不接受任何形式的捐助，因为自由地上网本来就是大家的权利，没有必要为此付出更多的代价。

但是，作为一个翻墙规则，不可避免的会对网站有所遗漏，需要大家来共同完善，当发现不好用的地方时，请打开 SR 的日志功能，检查一下是哪一个被墙的域名走了直连，或者是哪一个可以直连的域名走了代理。

将需要修改的信息反馈给我，大家的努力会让这个规则越来越完善！
>>>>>>> h2y/master
