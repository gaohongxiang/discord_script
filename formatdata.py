import pandas as pd
import os,sys
sys.path.append(os.getcwd()) # 工作目录
from config import *
from utils import try_except_code

# 组装数据
@try_except_code
def my_format_data(start_num, end_num):
    """组装数据
        
    Attributes:
        start_num:开始账号
        end_num:结束账号
        is_bitbrowser:是否为比特浏览器数据 True:比特浏览器 False:ads浏览器
    """
    if int(start_num) <= 0 or int(end_num) <= 0:
        print('账号必须大于0')
        return
    if int(start_num) > int(end_num):
        print('开始账号必须小于或等于结束账号')
        return
    # ip数据
    all_ip = pd.read_csv(ip_file, sep=':', engine='python')
    all_ip['proxy'] = "socks5://" + all_ip['proxy_username'] +":" + all_ip['proxy_password'] +"@" + all_ip['proxy_ip'] +":" + all_ip['proxy_port'].map(str)
    # discord数据
    all_discord = pd.read_csv(discord_file,sep='|', engine='python')
    
    data = pd.merge(left=all_ip,right=all_discord,left_index=True,right_index=True,how='inner')

    data = data.iloc[int(start_num)-1:int(end_num),:].reset_index(drop=True)
    data = data.to_dict('records')
    return data

def project_info(project):
    """收集到的项目的信息"""
    discord_info = json.load(open(discord_info_file,'r',encoding="utf-8")) # 项目信息文件，需要自己查看discord
    guild_id = discord_info[project]['guild_id'] # 加入的服务器id
    from_channel_list = discord_info[project]['from_channel_list'] # 消息来源频道id，可以从多个频道获取
    to_channel = discord_info[project]['to_channel'] # 发送消息的频道id
    mods = discord_info[project]['mods'] # 频道管理员
    keywords = discord_info[project]['keywords'] # 关键字
    return guild_id, from_channel_list, to_channel, mods, keywords

if __name__ == '__main__':

    my_format_data = my_format_data(1, 20)
    print(my_format_data)
