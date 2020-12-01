# FGO_Bluetooth_Assistant
### 项目简介，请仔细阅读（[跳转至中文部分](#jump1)）
This is the V2.0 ver game assitant for Fate Grand Order (iOS &amp; Android both suitable). For details, see [the following photos](#jump2), or [my video on bilibili](https://www.bilibili.com/video/av82095192?p=2).

### Important：
Android phones can be directly controlled by a windows PC or Mac PC, but iPhone can only be controlled by a Mac PC. (For players of Chinese sever:)If you are Android player or ios player with Mac PC , I highly recommend you to use Airtest or other scripts on Github(like [this](https://github.com/hgjazhgj/FGO-py)), because they are totally zero cost and have more functions. This programm let those who play FGO on iOS devices but only have Windows PC realise automatic play, just like using Adb to control Android devices. 

(For players of Japanese sever:)Japanese FGO client has currently cancelled root check for Android devices, but we are not sure whether it will come back in the future. More importantly, it's not allowed to use an Android emulator to play FGO. So for Japanese player, whatever the device you are using, this maybe the best solution.

I'm not clear about the situation of US sever, US players may decide which to use by yourself.

To lunch this program, all you need to do is to buy a bluebooth mouse module(about 40RMB / 6USD / 800JPY) and inatall Airplayer on your PC. You don't need to install any third party software on your phone. Also no need to jailbreak or root your phone.(Make sure that your system is iOS13 or later, Android user need Android3.0 or later)

If you don't know how to connect a bluebooth mouse with your phone, just Google it!

I know that in Japan, it's not allowed to use an Android emulator to play FGO, but this programm use the phone's own function to realize automatic play. It's time to liberate your hands and time!

Since I'm a FGO player of Chinese server, all the image templates are Chinese ver. For player in other countries, you need to make templates by yourself.

The following is the instruction of this programme, you can use translate webpage to read them.

<span id="jump1"> </span>
### 蓝牙模块购买指南
近日有玩家反馈我在PDF首页推荐的那家店铺大幅涨价，故不推荐大家再去该店铺购买。由于蓝牙鼠标模块是通用的，因此可以去其他店铺购买；只需注意一定要买蓝牙hid鼠标模块，不要只买一个普通的蓝牙传输模块，淘宝直接搜索“蓝牙hid模块”即可，使用方法都是大同小异的。

### 系统兼容性警告！
最新反馈，本人在安装有iOS14.1系统的iPhone12上进行了蓝牙鼠标的测试，发现鼠标在曲面屏上很难建立线性的坐标系，经过多次测试无解，故目前尚无法建立可靠的解决方案。

**但有一个好消息是我发现了一款可以通过PC直接控制iOS的软件——[虫洞](https://er.run/)，而且其支持用PyAutoGui等库实现电脑内的鼠标虚拟点击，因此可以基于该程序写一个适用于iOS13.4及以上系统和全面屏手机的脚本。**

<p style='color:red'> 近日，有玩家反馈蓝牙鼠标设备在iOS13.3系统上运行正常，但升级13.4后出现鼠标移动方向混乱的情况。同时全面屏手机因为四周为弧形而非直角，没有典型的零点，导致自行定位、修改代码困难。故这里给出系统兼容性建议：建议使用iPhone6s Plus、iPhone7(全型号)、iPhone8(全型号)等矩形屏幕手机，同时iOS13系统版本不超过13.3！ </p>

### 如何联系到我：
建议[B站私信联系](https://space.bilibili.com/13033022)。同时本人不会对诸如Python编程、代码修改等个人问题进行解答，仅接受bug反馈以及优化建议等内容的讨论。

### 国服玩家请阅读此处
日服实装C呆了！！！6加成不换人队伍明年大家也可以体验到了，狂武藏或仇凛一宝都可以冲了，祝大家泳装活动都能抽到狂武藏。

由于国服安卓没有root检测，也可以用模拟器上，推荐直接使用[hgjazhgjd大佬的脚本文件](https://github.com/hgjazhgj/FGO-py)；如果你是iOS用户同时也有Mac电脑，可以选择使用网易开发的Airtest来进行控制，其代码兼容python，可以自行探索编程；对于没有Mac的iOS用户，同时又不想越狱的，这应该是最好的解决方案了，成本仅40软妹币，相信对于各位氪佬来说根本微不足道（滑稽）。

**淘宝上的苹果脚本基本需要越狱，即使不用越狱的也是卖家自行修改了客户端，不保证安全**。

使用效果如下图所示，视频演示详见[B站视频](https://www.bilibili.com/video/av82095192?p=2)：
<span id="jump2"> </span>

![image1](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/1.jpg)

![image2](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/2.jpg)

![image3](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/3.jpg)


## 更新日志
### 2020-11-23：
1.新增了基于虫洞的识图驱动文件，可以与原来的进行无缝切换，注意使用前需要将该文件中的手机名称填写自己iPhone的名称，否则会找不到窗口。鼠标驱动部分可以使用PyAutoGui库实现，编程比硬件简单很多，我就不再写了，搭配虫洞使用的小伙伴可以自己写一下；

2.FGO_func的退出战斗部分更新了翻车后补刀的功能，替换了原来的短信提醒人工处理(因为我的阵容在今年圣诞无限池3面打15w血的布姐可能剩个血皮，故加入了此功能，简单来说就是将敌方平砍到死)。

### 2020-10-4：
1.修复了fgo_func中find_friend函数中在未寻找到指定助战英灵后进入死循环的bug(这个bug可能已经存在很久了，但去年可能人品比较好一直没出问题，只需将110行的WaitForFriendShowReady方法后面加个括号就行了)。

### 2020-9-4：
1.新增了御主礼装文件，可以在该文件中定义御主礼装的功能，将函数传入FGO_func中的Master_skill函数中即可快速实现礼装切换，无需大量修改代码。

### 2020-8-21：
1.四周年正式推出了“连续出击”的功能，对程序中的进入战斗部分进行了相应的修改。

### 2020-5-1:
1.优化了FGO_fuc.py文件中enter_battle函数，在没有检测到“上次执行”标志的情况下，默认点击界面上最上面的关卡。

### 2020-4-27：
1.修改了FGO_fuc.py文件中的第114、117行，将函数检测元素从`Master_face`改为`Attack_button`，为2月1日代码轻量化重构时的遗漏修改。

### 2020-3-24:
1.修复了ReadMe.pdf中模块进入AT指令方法中的错误表达。

### 2020-3-11:
1.新增了Smart_Battle.py文件，提供了3个实现宝具、卡牌颜色以及可用技能的检测函数(API)：

>1.1 GetAvailableTreasureDevice()函数，检测可用的宝具，返回可用的宝具位置列表，如[1,2]表示1、2号位英灵的宝具可用（需在选卡界面检测）；

>1.2 GetCardIndex()函数，用于获取卡牌颜色，返回五张卡颜色值的列表，如['Art','Buster',...,'Quick']；

>1.3 GetAvailableSkillIndex()函数，获取英灵的可用技能，返回列表，如[[1,2],[3],[]],表示1号位英灵的1、2技能可用；2号位英灵3技能可用，3号位英灵无可用技能。

**以上3个API可以用作智能化战斗的底层检测函数，配合相应的上层逻辑可以实现诸如色卡连携、自动释放技能宝具等高级功能。由于本人box练度足够且本项目是以刷无限池为目的开发的，故不想进一步开发智能化战斗的算法，有兴趣的玩家可以自行研究。**

2.删除了鸡肋的Config脚本读取功能，修改战斗脚本直接从FGO_func.py里的battle函数里修改即可。

### 2020-3-4:
1.删除了Word版的ReadMe，重新编写了PDF版的ReadMe。使用教程更加详细易懂。

### 2020-2-25:
1.fgo_optional_func中新增搓丸子的功能(不是最省QP的那种方法)。

### 2020-2-23:
1.修复了鼠标长时间来回移动会向左上方漂移的问题；

2.fgo_optional_func中新增友情池抽取功能，日后将添加搓丸子的功能。

### 2020-2-1：
1.在截图和图像识别部分加入了熔断功能，防止因小概率事件(如电话，低电量提醒等事件)导致程序死在死循环里，这里使用手机短信提醒功能来提醒人工处理；

2.FGO主函数代码轻量化重构，使用面向对象方法增强了可读性，增加了以下子功能或优化：

>2.1.在feed_apple函数前增加了延时防止因投屏延迟导致的识别错误

>2.2.find_friend函数支持自定义好友(目前自带CBA及孔明的模板)，在调用main函数时修改好友名即可(默认选CBA)

>2.3.card函数增加了随机发牌的功能(防脚本检测)

3.新增了无限池抽取功能(仅仅是简单的点击功能，未使用机器视觉)。
## 一.概述
### 文件概述：
0.ReadMe文件夹中的`ReadMe.pdf`文件有模块的淘宝地址以及使用概述

1.`Base_func.py`中定义了游戏图像截取以及模板匹配函数

2.`Serial.py`中定义了蓝牙鼠标通讯函数(感谢B站玩家@lsq5i5j_提供的相关代码)

3.`FGO_func.py`定义了FGO的相关函数，包括主程序(可在程序中的battle函数里直接修改战斗脚本)

4.`Notice.py`定义了手机短信通知的函数(需注册相关服务才能使用)

5.`Config.py`~定义了csv脚本读取函数~,**(由于该功能过于鸡肋，本文件已废弃)**

6.`FGO_optional_func.py`定义了一些非核心辅助性的功能，如：抽池等

7.`Smart_Battle.py`定义了一些智能化战斗的底层识图API

8.`Mystic_Codes.py`定义了御主礼装的功能，内附模板可自行增加常用的御主礼装

9.Bluebooth文件夹包含蓝牙鼠标模块的使用方法

10.Template文件夹包含识别用的图片模板

### 功能：

**注：由于Airplay功能耗电量较大，故一些辅助性功能如抽池未使用机器视觉；同时该脚本仅根据本人自身情况开发，不能满足所有玩家的需求**

1.支持AP不够自动喂苹果(优先银苹果后金苹果，铜苹果功能暂未开发，~应该说是不想开发？~)

2.支持自动找310CBA，如需找其他助战需自行制作图片模板

3.自定义战斗脚本和战斗次数(3T脚本基本170~190秒一关)，本项目代码根据3T脚本(也可以自行增加回合数)固定来打的，并没有智能化放技能宝具的功能，需要玩家有相应练度，如果练度不够(如无拐)或想要全加成的玩家可以使用前述的[hgjazhgj的脚本文件](https://github.com/hgjazhgj/FGO-py)，但其项目仅支持安卓

4.礼装掉落手机短信提醒

5.翻车提醒(实测目前没翻过车hhh)

6.新增无限池抽取功能(不是智能化抽取)

7.新增友情池抽取功能

8.新增搓丸子功能(使用时需选好一张满破低星礼装，进入强化界面再运行，在筛选中关闭4、5星礼装显示)

8.更多功能开发中。。。。。

## 二.使用方法
0.阅读文档中的PDF文件，内部有蓝牙鼠标模块的淘宝商品界面以及程序中需要一定修改的部分的简介

1.安装python3.7运行环境(建议直接安装[Anaconda](https://www.anaconda.com/distribution/))

>1.1.安装`opencv`、`numpy`、`twilio`、`pywin32`、`pyserial`库(否则程序无法运行,`numpy`、`pywin32`库anaconda安装时自带，还有一些底层的函数库软件安装时也会自行安装，这里不再赘述)

2.安装Airplayer，分辨率调成iPhone6/6s Plus(由于本人测试环境为iPhone6s Plus，不排除其他手机模板不匹配的可能，如需使用请自行裁剪模板)

3.打开`FGO_func`文件，在`battle`函数中写入战斗脚本，在`main`函数中配置串口以及战斗次数

>3.1.英灵技能函数`character_skill`包含三个参数，分别为英灵位置、技能编号、目标英灵位置；如：想把2号位英灵的1技能加给3号位的英灵，可以写：`character_skill(2,1,3)`;想释放2号位英灵的3技能，可以写：`character_skill(2,3)`

>3.2.御主技能函数`Master_skill`包含一个御主礼装函数句柄参数，一个*args不定参数，（目前默认使用的是换人服，可自行修改）不定参数必须写技能编号，被替换英灵位置、替换目标英灵位置等信息都是可选参数，只需在使用到该指令使填写即可，如：想释放御主的1技能，可以写：`Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,1)`，想将场上第二个英灵与后排第三个英灵交换，可以写：`Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,3,2,3)`

>3.3.发牌函数`card`包含一个参数，用于写要放的宝具位置，同时系统会随机发剩下两张牌，如：想释放1号位英灵的宝具，可以写：`card(1)`，系统会选择该宝具与任意两张牌

4.配置手机短信提醒服务，如果不需要请删除`FGO_func`文件中的`sent_message`函数(若直接运行不报错也可以选择无视)

>注：注册服务请至twilio官网，并将自己的信息写入`Notice.py`文件中方可收到短信提醒

5.配置蓝牙鼠标模块，模块使用AT指令关闭自动休眠，设置一个名字即可连接(操作说明以及配置软件在bluebooth文件夹下)

6.手机连接电脑的Airplayer

7.运行`FGO_func`，等待完成即可
