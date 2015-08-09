===============================================
ATコマンド サンプル集
===============================================

初めに
----------------------------------------------

ESP-WROOM-02を使う上でよく使うコマンドをまとめていきます。


:シリアル速度: 115200bps
:改行文字: CR+LF ※超重要！
:説明FWのバージョン: v1.1.1

説明の都合上、以下の記号を追加しますが、実際は送受信されません。

:送信: ●
:受信:
:コメント: ○これはコメント
:station: クライアントモード(子機)
:softAP: アクセスポイントモード(親機)
:station+softAP: クライアント＆アクセスポイントモード

1. モジュールとの接続確認
----------------------------------------------

- AT

    OK

    - ATコマンドを送る。結線やモード設定とCR+LFに問題がなければ戻ってくるはず。

- AT+GMR

    AT version:0.25.0.0(Jun  5 2015 16:27:16)

    SDK version:1.1.1

    compile time:Jun  5 2015 21:03:10

    |
    OK

    - ESP-WROOM-02のFWのバージョン確認 （上のは秋月電子で購入したもの）



2. WiFiルーターとの接続
----------------------------------------------


- AT+CWMODE=3

    |
    OK

    - 3はstation+softAPで、1ならstationdだけ。

- AT+CWLAP

    +CWLAP:(4,"xxxxxxxxx",-83,"xx:xx:xx:xx:xx:xx",1)

    +CWLAP:(4,"xxxxxxxxx",-92,"xx:xx:xx:xx:xx:xx",1)

    +CWLAP:(4,"xxxxxxxxx",-94,"xx:xx:xx:xx:xx:xx",3)

    +CWLAP:(4,"xxxxxxxxx",-57,"xx:xx:xx:xx:xx:xx",11)

    +CWLAP:(4,"xxxxxxxxx",-74,"xx:xx:xx:xx:xx:xx",11)

    +CWLAP:(2,"xxxxxxxxx",-75,"xx:xx:xx:xx:xx:xx",11)

    - 受信出来たアクセスポイントを表示

        :ecn: 0:OPEN 1:WEP 2:WPA_PSK 3:WPA2_PSK 4:WPA_WPA2_PSK
        :ssid: アクセスポイントのSSID名
        :rssi: 電波強度(dB)
        :mac: アクセスポイントのMACアドレス

- AT+CWJAP="ssid","password"


    WIFI CONNECTED

    WIFI GOT IP

    |
    OK

    - アクセスポイントに接続、無事にIPが取れればGOT IPとなる。


- AT+CIFSR

    +CIFSR:STAIP,"192.168.100.101"

    +CIFSR:STAMAC,"xx:xx:xx:xx:xx:xx"

    |
    OK

    - アクセスポイントからDHCPで割り振られたIPを表示

3. TCP/IPでサーバーに接続
----------------------------------------------

- AT+CIPSTART=”TCP”,”IPAddr”,Port

(準備中)


|
|
|
|
|
|
|
|
|
|
|

提供
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ArtifactNoise.

.. image:: img/ANlogoMark.png
    :alt: ArtifactNoise
    :scale: 18%
    :target: http://artifactnoise.com

管理情報
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:改版: 2015/08/09　GOT は GET の過去形。（ボンミス）
:初版: 2015/08/09

:作成者: Yuta kitagami
:連絡先: kitagami@artifactnoise.com
:twitter: @nonNoise
