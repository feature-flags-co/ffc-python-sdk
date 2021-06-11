# 敏捷开关 Python SDK 

本项目为 [敏捷开关 https://www.feature-flags.co](https://www.feature-flags.co) 的 Python SDK

This is a Python SDK for [https://www.feature-flags.co](https://www.feature-flags.co), a feature flag management system

## 安装

```
  pip install feature-flags-co
```

## 简易教程

以下为一个简单例子，对于 Web API, 一个 User Session 只需要初始化一次
The following is a simple example, for Web API, only need to initialize once for a single User Session

```
    from feature_flags_co import FfcClient, FfcUser
  
    ffc_user = FfcUser(
        user_name=['user_name'],
        email=['email'],
        key=['key'],
        customize_properties= [ // 可以为空 (Can be omitted)
            {'phoneNumber': '13895462538'} // 任意 dict， 此电话号码并不存在 (arbitrary dict key and value)
        ]
    )
    
    # 初始化 Client， 针对一个终端用户只需要初始化一次 
    # Initialization of the client
    ffc_client = FfcClient(['environment_secret'], ffc_user)
    
    # 调用 variation 方法， 获取具体某一个 feature flag 的值，defaultResult 为当服务器返回异常时默认的返回值
    # Call variation method to get the value of a specific feature flag, defaultResult would be result if any exception happened during the call
    result = ffc_client.variation([feature-flag-key], defaultResult=False)
    
    print(f'Hi, {result}')
    
    # 接下来根据 result 打开或者关闭某功能
    # Now we can use the value of result to switch on/off some fonctionalities
    if result：
        pass
        
```
