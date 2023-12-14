# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
"""
import json
import time
import random
import string


def generate_id() -> str:
    """
    Math.random().toString(36).substring(7) + new Date().getTime()
    """
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    timestamp = int(time.time() * 1000)
    return f"{random_string}{timestamp}"


def pattern_modify(patterns: list[dict]) -> list[dict]:
    """
    New version also add "*://" in the pattern. The function can remove it.
    """
    ret = []
    for val in patterns:
        ret.append(this := {})
        this.update(val)
        if this["type"] == "wildcard" and this["pattern"].startswith("*://") and this["pattern"].endswith("/"):
            this["pattern"] = this["pattern"][4:-1]
        this["protocols"] = 1  # 1 means http and https
        this["type"] = 1 if val["type"] == "wildcard" else 2

    return ret


def data_modify(data: dict) -> dict:
    """
    Input the new type config, return the old type.
    """
    ret = {}

    type_map = {"http": 1, "https": 2, "socks5": 3, "socks4": 4, "direct": 5}

    ret["mode"] = "disabled"
    ret["proxySettings"] = proxy_settings = []

    for index, val in enumerate(data["data"]):
        item_id = generate_id()
        # proxy_setting = dict.fromkeys(["active", "title", "color", "port", "username", "password", "cc"], val)
        proxy_settings.append(proxy_setting := {})

        proxy_setting["active"] = val["active"]
        proxy_setting["title"] = val["title"]
        proxy_setting["color"] = val["color"]
        proxy_setting["port"] = val["port"]
        proxy_setting["username"] = val["username"]
        proxy_setting["password"] = val["password"]
        proxy_setting["cc"] = val["cc"]
        proxy_setting["index"] = index
        proxy_setting["address"] = val["hostname"]
        proxy_setting["country"] = ""
        proxy_setting["whitePatterns"] = pattern_modify(val["include"])
        proxy_setting["blackPatterns"] = pattern_modify(val["exclude"])
        proxy_setting["type"] = type_map[val["type"]]
        proxy_setting["proxyDNS"] = False
        proxy_setting["pacURL"] = val["pac"]
        proxy_setting["id"] = item_id

    return ret

def main(file_path, save_path):
    """
    :pram file_path: the old type config path
    :pram save_path: the new type config path to save
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    data = data_modify(data)
    with open(save_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    import os
    import sys
    try:
        file_path, save_path = sys.argv[1:]
    except ValueError:
        print("Usage: python3 main.py <file_path> <save_path>")
        print("You can also input them now:")
        file_path = input("File path: ")
        save_path = input("Save path: ")
    main(file_path, save_path)
    print("Done! Find the file in the save path", os.path.abspath(save_path).join('""'))
