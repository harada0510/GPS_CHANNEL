# FOR_RAHOK_SENSE
Gift for Mr. Rahok

# Licence
CopyRight (c) 2018 Shuto Kawabata

Released under the MIT licence

https://opensource.org/licenses/MIT


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
<br>自分が高専の時にこの座標系でロボットの自動運転ができた理由は，算出したX[m]とY[m]に対して定数（確か1.3くらい）をかけることで，XYZの３次元で算出した点と点を結んだ場合の平面上のX[m]，Y[m]と同程度の大きさになったからであり，かつ，日本の緯度は比較的高い（Z軸となる北極に近い）ので，本来考慮すべきZ軸上の変化が極度に小さいから．（つまり北極の中心点で実験するならこの座標系のXとYだけで全く問題なく綺麗に自律走行する．　逆に，　赤道直下のマレーシアとかでやったらおわり．）一番の理由は，　GoogleMapsから取得した経緯度情報をマップとして扱うのにも，　ロボットの自己位置修正として経緯度を扱うのにも，　統一してこの座標系を使っていたことがなんとか自律移動できる唯一の救い．
<br>当時，自律走行はするものの，やけに片方向に寄ったり，少し大回りをするのは以上が原因

# How to use

## 0_googleMap.html
ここで，waypointをプロットしたあとに，CSVに保存ボタンを押せば，プロットしたwaypoint番号と緯度，経度が保存される
## 1_make_xy.py

## 1_make_xy_WGS84.py

