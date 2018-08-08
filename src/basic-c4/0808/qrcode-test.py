# パッケージをインポート
import qrcode
#  QRコードを生成
img = qrcode.make("https://www.yahoo.co.jp/")
# ファイルに保存
img.save("qrcode-test.png")
