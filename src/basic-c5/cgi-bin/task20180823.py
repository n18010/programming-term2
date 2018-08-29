#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

# ブラウザでのデバッグを有効にする
cgitb.enable()

# 全体の表示
FILE_LOG = "test-record.txt"


# HTMLを画面に出力する
def print_html(style, sum_score, ave_score, table_list):
    # ヘッダを出力
    print("Content-Type: text/html; charset=utf-8")
    print("")
    # HTMLを出力
    print("""
<html>
<head><meta charset="utf-8">
<title>成績表</title>
<style>
{0}
</style>
</head>
<body>
<h1>成績表</h1>
<div><form>
名前: <input type="text" name="name" size="15">
点数: <input type="text" name="score" size="8">
<input type="submit" value="追加">
<input type="hidden" name="mode" value="write">
</form></div><hr>
<p>合計点 {1}</p>
<p>平均点 {2}</p>
<table>
<tr><th>名前</th><th>点数</th><th>差</th></tr>
{3}
</table>
</body>
</html>
    """.format(style, sum_score, ave_score, table_list))


# 画面に書き込みログを表示する
def mode_read(form):
    sum_score = 0
    table_list = []
    total = 0
    avg_score = 0
    style = """
table {border-collapse: collapse;}
th, td {border: 1px solid; padding: 0 20px;}
.right {text-align: right;}
"""
    # ログを読み取る
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            for line in f:
                list_a = line.split(",")
                name = html.escape(list_a[0])
                sum_score += int(list_a[1])
                total += 1

            avg_score = round(sum_score / total, 2)

        with open(FILE_LOG, "r", encoding='utf-8') as f:
            for line in f:
                list_a = line.split(",")
                name = html.escape(list_a[0])
                diff_score = round(avg_score - int(list_a[1]), 2)
                table_td = """
<tr><td>{0}</td><td class="right">{1}</td><td class="right">{2}</td></tr>
                """.format(name, list_a[1], diff_score)
                table_list.append(table_td)
    print_html(style, sum_score, avg_score, "\n".join(table_list))


# 任意のURLにジャンプする
def jump(url):
    # ヘッダを出力
    print("Status: 301 Moved Permanently")
    print("Location: " + url)
    print("")
    # HTMLを出力（ヘッダがうまく動かなかった時の対策）
    print('<html><head>')
    print('<meta http-equiv="refresh" content="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">jump</a></body></html>')


# メッセージの書き込み
def mode_write(form):
    # パラメータを取得
    name = form.getvalue("name", "no name")
    score = form.getvalue("score", "")
    # ファイルに保存
    with open(FILE_LOG, "a+", encoding='utf-8') as f:
        f.write("{0},{1}\n".format(name, score))
    # 書き込み後にリダイレクト
    jump('task20180823.py')


# メイン処理
def main():
    # フォームの値を取得
    form = cgi.FieldStorage()
    # modeパラメータを取得
    mode = form.getvalue("mode", "read")
    # modeの値によって処理を変更
    if mode == "read":
        mode_read(form)
    elif mode == "write":
        mode_write(form)
    else:
        mode_read(form)


if __name__ == "__main__":
    main()
