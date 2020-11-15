# -*- coding: utf-8 -*-
# Author: kelvinBen
# Github: https://github.com/kelvinBen/AppInfoScanner


# 此处用于搜索组件信息
# com.alibaba.fastjson -> fastjson
# com.google.gson -> gson
# com.fasterxml.jackson -> jackson
# net.sf.json -> 
# javax.xml.parsers.DocumentBuilder -> dom方式
# javax.xml.parsers.SAXParser -> sax方式
# org.jdom.input.SAXBuilder -> jdom
# org.dom4j.io.SAXReader -> dom4j
filter_components = [
    'com.alibaba.fastjson',
    'com.google.gson',
    'com.fasterxml.jackson',
    'net.sf.json',
    'javax.xml.parsers.DocumentBuilder',
    'javax.xml.parsers.SAXParser',
    'org.jdom.input.SAXBuilder',
    'org.dom4j.io.SAXReader'
]

# 此处目前支持过滤
# 1. https://以及http://开头的
# 2. IPv4的ip地址
# 3. URI地址,URI不能很好的拼接所以此处忽略
filter_strs =[
    r'https://.*|http://.*',
    r'.*://([[0-9]{1,3}\.]{3}[0-9]{1,3}).*',
    # r'/[a-z0-9A-Z]+/.*'
]

# 此处忽略常见的域名等信息
filter_no = [
    # r'.*127.0.0.1',
    # r'.*0.0.0.0',
    # r'.*localhost',
    # r'.*w3.org',
    # r'.*apache.org',
    # r'.*android.com',
    # r'.*weixin.qq.com',
    # r'.*jpush.cn',
    # r'.*umengcloud.com',
    # r'.*umeng.com',
    # r'.*baidu.com',
    # r'.*apple.com',
    # r'.*alibaba.com',
    # r'.*qq.com',
    # r'.*sohu.com',
    # r'.*openssl.org',
    # r'.*weibo.com',
    # r'.*wechat.com',
    # r'.*.amap.com',
    # r'.*openxmlformats.org',
    # r'.*github.com',
    # r'.*w3school.com.cn',
    # r'.*google.com'
]

# 此处配置壳信息
shell_list =[
    'com.stub.StubApp',
    's.h.e.l.l.S',
    'com.Kiwisec.KiwiSecApplication',
    'com.Kiwisec.ProxyApplication',
    'com.secshell.secData.ApplicationWrapper',
    'com.secneo.apkwrapper.ApplicationWrapper',
    'com.tencent.StubShell.TxAppEntry',
    'c.b.c.b',
    'MyWrapperProxyApplication',
    'cn.securitystack.stee.AppStub',
    'com.linchaolong.apktoolplus.jiagu.ProxyApplication',
    'com.coral.util.StubApplication',
    'com.mogosec.AppMgr',
    'io.flutter.app.FlutterApplication'
]

# 此处配置需要扫描的web文件后缀
web_file_suffix =[
    "html",
    "js",
    "html",
    "xml",
    "php",
    "jsp",
    "class",
    "asp",
    "aspx",
    "py"
]

