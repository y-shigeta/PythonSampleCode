# 画像座標の取得関数
def get_coord(png):
    # 画像ファイルのパス
    file_path = png+".png"
    if "radio_" == png[:6]:
    # ラジオボタンは左上から10ほど右下
        x,y,w,h = pag.locateOnScreen(file_path)
        temp_coord = (x+10,y+10)
    else:
    # ラジオボタン以外は真ん中
        temp_coord = pag.locateCenterOnScreen(file_path)
    # Noneチェック
    if temp_coord is None:
        print(file_path+"の座標が見つかりませんでした")
        sys.exit()
    return temp_coord

# 画像リスト
png_list=["csv", "system", "text_name", "text_price", "radio_single", "radio_set", "text_comment", "button_next"]
# 画像座標
coord = {}
for png in png_list:
    x,y = get_coord(png)
    coord.update({png:{"x":x, "y":y}})
# 余白座標(次へボタンの少し下の余白部分とする)
x,y = (coord["button_next"]["x"], coord["button_next"]["y"]+20)
coord.update({"margin":{"x":x, "y":y}})
print(coord)

# システムに入力する行数
rows = 5
pag.PAUSE = 1.0
# CSVファイルをアクティブに
pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
# 指定行数分ループ
for row in range(0, rows):
    # 商品名
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_name"]["x"], y=coord["text_name"]["y"])
    pag.hotkey('ctrl', 'v')
    # 値段
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_price"]["x"], y=coord["text_price"]["y"])
    pag.hotkey('ctrl', 'v')
    # 単品/セット
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    num = str(pyperclip.paste()).strip()
    if num == "単品":
        pag.click(x=coord["radio_single"]["x"], y=coord["radio_single"]["y"])
    elif num == "セット":
        pag.click(x=coord["radio_set"]["x"], y=coord["radio_set"]["y"])
    # 説明
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_comment"]["x"], y=coord["text_comment"]["y"])
    pag.hotkey('ctrl', 'v')
    # 次へボタン
    pag.click(x=coord["button_next"]["x"], y=coord["button_next"]["y"])
    pag.click(x=coord["margin"]["x"], y=coord["margin"]["y"])
    # CSVファイルの次の行へ
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press(['enter', 'enter'])
