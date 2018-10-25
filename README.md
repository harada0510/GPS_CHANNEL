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

# WGS84 coordinate system
#### X's positive direction: West
#### Y's positive direction: South
#### Z's positive direction: Earth's above
正確にはこの図におけるXYZのこと↓（実際には東西南北で示せない）<br>
https://www.enri.go.jp/~fks442/K_MUSEN/1st/1st060428rev2.pdf
<br>ここに出てくるe,n,uが，ちょうどPlane rectangular coordinate system（平面直交座標系）のXYZに対応する！！
<br>この座標系を扱う場合は，(X0,Y0,Z0),(X1,Y1,Z1)...(Xn,Yn,Zn)のように常にこのXYZの三次元でなければ意味ない
<br>このXYZ３次元の点と点を線で結んだものは，平面の自律移動ロボットのマップとして用いることが可能だが，そんなことするのは手間なので，座標系そのものにこだわりがなければ，Plane rectangular coordinate system（平面直角座標系）を使う
<br>自分が高専の時にこの座標系でロボットの自動運転ができた理由は，算出したX[m]とY[m]に対して定数（確か1.3）くらい
# How to use

## 0_googleMap.html


## 1_make_xy.py

## 1_make_xy_WGS84.py

