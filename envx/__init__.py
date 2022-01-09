#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import platform


def basic(
        file_name: str
):
    inner_file_name = file_name.lower()

    if platform.system() == 'Windows':  # Windows
        basic_return = {
            'sys_support': True,
            'path_separator': '\\',
            'env_path': 'C:\\env\\',
            'file_dir': 'C:\\env\\%s' % inner_file_name
        }
        return basic_return
    elif platform.system() == 'Darwin':  # macOS
        basic_return = {
            'sys_support': True,
            'path_separator': '/',
            'env_path': '/Users/env/',
            'file_dir': '/Users/env/%s' % inner_file_name
        }
        return basic_return
    elif platform.system() == 'Linux':  # Linux
        basic_return = {
            'sys_support': True,
            'path_separator': '/',
            'env_path': '/env/',
            'file_dir': '/env/%s' % inner_file_name
        }
        return basic_return
    else:
        basic_return = {
            'sys_support': False,
            'path_separator': '',
            'env_path': '',
            'file_dir': ''
        }
        return basic_return


def read(
        file_name: str
):
    """
    file_name:环境文件名称，包括后缀名，不区分，例如：
        mysql.env
        mongo.env
        redis.env

    环境文件的内容是以航区分，以=符号指定，例如：HOST=192.168.0.1
    读取的结果是一个dict，将原来的行按照=符号组成键值对，例如：{"HOST": "192.168.0.1"}

    环境文件路径支持：
        Windows：
            C:\
        macOS:
            /Users/env/
        Linux:
            /env/
    """
    env_dict = dict()
    basic_info = basic(file_name=file_name)
    file_dir = basic_info['file_dir']
    f = open(file_dir, encoding='utf-8')
    file_read = f.read()
    lines = file_read.split('\n')
    for each_line in lines:
        if '=' in each_line:
            each_line_split = each_line.split('=')
            env_dict[each_line_split[0]] = each_line_split[1]
        else:
            pass
    return env_dict