# 敏捷开关 Python SDK

本项目为 [敏捷开关 https://www.feature-flags.co](https://www.feature-flags.co) 的 Angular SDK

## 安装

```
  pip install feature-flags-co
```

## 简易教程

以下为一个简单例子，对于 Web API, 一个 User Session 只需要初始化一次

```
    from feature_flags_co import FfcClient, FfcUser
  
    ffc_user = FfcUser(
        user_name=['user_name'],
        email=['email'],
        key=['key'],
        customize_properties= [ // 可以为空
            {'phoneNumber': '13895462538'} // 任意 dict， 此电话号码并不存在
        ]
    )
    
    # 初始化 Client， 针对一个终端用户只需要初始化一次
    ffc_client = FfcClient(['environment_secret'], ffc_user)
    
    # 调用 variation 方法， 获取具体某一个 feature flag 的值，defaultResult 为当服务器返回异常时默认的返回值
    result = ffc_client.variation([feature-flag-key], defaultResult=False)
    
    print(f'Hi, {result}')
    
    # 接下来根据 result 打开或者关闭某功能
    
    if result：
        pass
        
```
