# 功能
- 获取token
- 发送信息
- 双号互聊
- 钉钉机器人提醒

# 文件结构
```
discord.py
config.py
formatdata.py
utils.py
.gitignore
README.md
data
    discord.csv # discord账号
    ip.csv # 独立ip
    channel_messages.txt # 从频道中获取的聊天内容
    fix_messages.txt # 固定聊天内容
    discord_info.json # 项目的一些discord信息
```

需要补齐的敏感数据文件

discord.csv

你的discord账号.这个discord_token是需要程序获取的,会自动填充进来,可以留空
```
discord_id|discord_create_email|discord_password|discord_username|discord_token
1|xxxxx|xxxxx|xxxxx|xxxxx
......
```

ip.csv

你的独立ip数据
```
proxy_ip:proxy_port:proxy_username:proxy_password
xxxxx:xxxxx:xxxxx:xxxxx
xxxxx:xxxxx:xxxxx:xxxxx
......
```

config.py
```
discord_file = './data/discord.csv'
discord_fix_messages_file = './data/fix_messages.txt'
discord_channel_messages_file = './data/channel_messages.txt'
discord_info_file = './data/discord_info.json'
ip_file = './data/ip.csv'
# 钉钉机器人id
ROBOTID = 'xxxxx'
```

# 钉钉机器人设置

https://open.dingtalk.com/document/orgapp/custom-robot-access

这个就是一个提醒功能.当别人@你让你回复时需要及时处理.所以加个提醒.