# E-Cology9.0-SQL-POC

## 概述
这是一个用于检测e-cology(FileDownloadForOutDoc)前台SQL注入漏洞的python版本的poc。它可以对单个 URL 或包含多个 URL 的文本文件进行检测，并输出结果。

## 功能
- 检测e-cology(FileDownloadForOutDoc)前台SQL注入漏洞。
- 支持单个 URL 和包含多个 URL 的文本文件。

## 影响范围
- Ecology 9.x 补丁版本 < 10.58.0
- Ecology 8.x 补丁版本 < 10.58.0

## 使用方法

1. 确保已安装所需的 Python 版本。
2. 安装所需的依赖库：`pip install -r requirements.txt`。
3. 使用单个 URL 运行代码：`python main.py -u <URL>`。
4. 使用包含多个 URL 的文本文件运行代码：`python main.py -t <文本文件路径>`。
5. 单个url结果将显示在终端，多个url则会保存在名为 `e-cology-9.0-OA-result.txt` 的文件中。

## 注意事项

- 在运行代码之前，请确保目标网站的可访问性。
- 仅在合法授权下使用该代码。
- 作者对于使用该代码和产生的后果不承担任何责任。
