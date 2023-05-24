<!-- markdownlint-disable MD033 MD036 MD041 -->

<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-helloworld

_✨ Hello World! ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-helloworld.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-helloworld">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-helloworld.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

你好，世界

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-helloworld

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-helloworld

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-helloworld

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-helloworld

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-helloworld

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_helloworld"]

</details>

## 🎉 使用

### 指令表

| 指令  | 权限 | 需要@ |   范围    | 说明  |
| :---: | :--: | :---: | :-------: | :---: |
| hello |  无  |  否   | 私聊/群聊 | world |
