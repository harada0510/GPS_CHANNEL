# FOR_RAHOK_SENSE
Gift for Mr. Rahok

# Licence
CopyRight (c) 2018 Shuto Kawabata

Released under the MIT licence

https://opensource.org/licenses/MIT

# 内容
ブラウザ上でプロットしたwaypointの緯度，経度を全自動で取得，CSVファイルに保存するHTMLとJavaScript<br>
保存したファイルの緯度，経度をロボットの自律走行で扱うためのマップ（直交平面座標系）に変換するプログラム．<br>
高専のときに用いていたWGS84座標系も同時に算出し，比較を行うプログラム．
<img src="https://github.com/shutokawabata0723/FOR_RAHOK_SENSE/blob/master/fig/gps_channel.png" width="900px">
結果はこんな感じ( ^ω^ )
<img src="https://github.com/shutokawabata0723/FOR_RAHOK_SENSE/blob/master/fig/kosen2.png" width="900px">



# Program files
### 0_googleMap.html
waypointをプロットしたあとに，CSVに保存ボタンを押せば，プロットしたwaypoint番号と緯度，経度が保存される
<br>あえてHTMLの中にJavaScriptを記述してるから，仕様を少しいじる程度であればそこをいじってね
### 1_make_xy.py
とってきた緯度経度を平面座標に変換する（平面直交座標系）
ここのモジュール，pyprojを開いて見れば，普通はCかC++で書かれてるからちょっと解析すればそのままロボットの自己位置修正部分の座標変換式として移植できると思う．

### 1_make_xy_WGS84.py
とってきた緯度経度を平面座標に変換する（WGS84座標系）

### 2_offset.py
変換された平面座標（絶対座標のまま）をスタート地点を軸にした相対座標系に変換（平面直交座標系Ver）

### 2_offset_WGS84.py
変換された平面座標（絶対座標のまま）をスタート地点を軸にした相対座標系に変換（WGS84Ver）

### 3_plot.py
相対座標に変換された平面直交座標系とWGS84座標系の（X,Y)を描写する．　
<br>plot.pngとしてプロット図のスクショが自動で保存される．


### shell.sh
以上に挙げたプログラムの実行を自動化してくれるシェルスクリプト．
<br>output.csvの座標変換から（X,Y）の描写まで一貫してやってくれる．



# How to use
#### 環境：Python2.7（MacbookかLinuxならデフォルトで入ってる）
```pip install pyproj```

で座標変換モジュールpyprojをインストール

#### 実行方法：0_googleMap.htmlをブラウザで開いてwaypointを打ったあと，「CSVに保存」ボタン押してoutput.csvをダウンロード．
#### ダウンロードしたoutput.csvをディレクトリ「data」内に移し，'sh shell.sh'でシェルスクリプトを実行するか，以下の手順で実行する．

| File | Execute |IN | OUT |
----|----|----|----
|0_googleMap.html|上記||output.csv|
|1_make_xy.py|python 1_make_xy.py|output.csv|xy.csv|
|1_make_xy_WGS84.py|python 1_make_xy_WGS84.py|output.csv|xy_WGS84.csv|
|2_offset.py|python 2_offset.py|xy.csv|xy_offseted.csv|
|2_offset_WGS84.py|python 2_offset_WGS84.py|xy_WGS84.csv|xy_WGS84_offseted.csv|
|3_rptate.py|python 3_rotate.py|xy_offseted.csv<br>xy_WGS84_offseted.csv|xy_rotated.csv<br>xy_WGS84_rotated.csv|
|3_plot.py|python 3_plot.py|xy_rotated.csv<br>xy_WGS84_rotated.csv|plot.png|


# Plane rectangular coordinate system
#### X's positive direction: North
#### Y's positive direction: East
#### Z's positive direction: Sky
つまり今自分が立ってる頭の真上がZ方向で，北がX軸の正方向，東がY軸の正方向ってこと（一番直感的にわかると思う）
https://vldb.gsi.go.jp/sokuchi/surveycalc/surveycalc/algorithm/bl2xy/bl2xy.htm
本来，使うべきだった座標系！！！
<br>これで作ったマップとこれで変換した自己位置情報(X,Y)を使えば，　当時の移動ロボットの自己位置修正プログラムにそのまま移植するだけで格段に精度がよくなる（はず）．

# WGS84 coordinate system
#### X's positive direction: West
#### Y's positive direction: South
#### Z's positive direction: Earth's above
正確にはこの図におけるXYZのこと↓（実際には東西南北で示せない）<br>
https://www.enri.go.jp/~fks442/K_MUSEN/1st/1st060428rev2.pdf
<br>ここに出てくるe,n,uが，ちょうどPlane rectangular coordinate system（平面直交座標系）のXYZに対応する！！
<br>この座標系を扱う場合は，(X0,Y0,Z0),(X1,Y1,Z1)...(Xn,Yn,Zn)のように常にこのXYZの三次元で扱わなければ意味ない
<br>このXYZ３次元の点と点を線で結んだものは，平面の自律移動ロボットのマップとして用いることが可能だが，そんなことするのは手間なので，座標系そのものにこだわりがなければ，先のPlane rectangular coordinate system（平面直角座標系）を使う
<br>自分が高専の時にこの座標系でロボットの自動運転ができた理由は，算出したX[m]とY[m]に対して定数（確か1.3くらい）をかけることで，XYZの３次元で算出した点と点を結んだ場合の平面上のX[m]，Y[m]と同程度の大きさになったからであり，かつ，日本の緯度は比較的高い（Z軸となる北極に近い）ので，本来考慮すべきZ軸上の変化が極度に小さいから．（つまり北極の中心点で実験するならこの座標系のXとYだけで全く問題なく綺麗に自律走行する．逆に，赤道直下のマレーシアとかでやったらおわり．）一番の理由は，GoogleMapsから取得した経緯度情報をマップとして扱うのにも，ロボットの自己位置修正として経緯度を扱うのにも，　統一してこの座標系を使っていたことがなんとか自律移動できる唯一の救い．
<br>当時，自律走行はするものの，やけに片方向に寄ったり，少し大回りをするのは以上が原因




# ロボットのDGPS自己位置修正プログラムについて
確かDGPSの自己位置取得間隔は１[s]<br>
単純に考えて，時刻t[s]にDGPSで受信した位置情報は，実は時刻t-1[s]の時のロボットの座標ってことになる．<br>
そしてロボットは常に移動していて，速度は0.5-1.0[m/s]<br>
つまり，タイヤのエンコーダのみでどんなに正確に移動できていたとしても，エンコーダで算出した（X,Y)座標とDGPSで受け取った（X,Y)座標には0.5-1.0[m]程の差が常に生じていたことになる．
結論としては，時刻t[s]にDGPSが受け取った座標（X,Y）と時刻t-1[s]にエンコーダで算出した（X,Y)座標を比較するべきである．

