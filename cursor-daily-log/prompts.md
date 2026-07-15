# cursor-daily-log 提示词

路径以本机 `config.json` 为准（见 `config.example.json`）。

## 生成本日日志

```text
请按 cursor-daily-log skill：抓取今天的 Cursor 会话，写入配置的日志目录，
要有今日主线 + 各会话一句摘要，不要堆原话。跑完把主线念给我听。
```

## 补某一天

```text
用 cursor-daily-log 补写指定日期的 Cursor 日志（主线 + 会话摘要）。
日期：YYYY-MM-DD
```

## 安装 / 修好定时

```text
帮我安装 cursor-daily-log 到本机，写好 config.json（vault 和 python 路径），
并注册每天固定时间的计划任务。装完跑一次验证。
```

## 只要主线口述（不改文件）

```text
根据今天的 Cursor 会话，口头按几条主线总结今天做了什么（先别写文件）。
```
