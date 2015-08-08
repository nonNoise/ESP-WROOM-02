===========================================================
ATコマンド集
===========================================================


0.ATコマンドの構文
-----------------------------------------------------------
.. csv-table:: ATコマンドの構文
   :header: "Command", "内容"
   :widths: 15, 30

    "AT+<x>=?","コマンド確認用（？）"
    "AT+<x>?","変数内容表示"
    "AT+<x>=<...>","変数に代入"
    "AT+<x>","コマンド実行"



1.ATコマンド 基本形
-----------------------------------------------------------
.. csv-table:: ATコマンドの構文
   :header: "Command","内容","戻り値内容"
   :widths: 15,50, 20

    "AT","テスト用ATコマンド",">AT"
    "AT+RST","リセットコマンド","Boot文字が見える"
    "AT+GMR","バージョン確認用コマンド","バージョンが表示される"
    "AT+GSLP","Deap-Sleapモードに移行","(確認中)"
    "ATE","エコー有り無し指定？","(確認中)"
    "AT+RESTORE", "Factory Reset","(確認中)"
    "AT+UART", "シリアル通信設定（速度等）","(確認中)"
    "AT+UART_CUR", "シリアル通信設定","(確認中)"
    "AT+UART_DEF","シリアル通信設定","(確認中)"
    "AT+SLEEP", "Sleep mode","(確認中)"
    "AT+RFPOWER", "Set RF TX Power","(確認中)"
    "AT+RFVDD", "RF TX Power according to VDD33","(確認中)"


2.ATコマンド WiFi周りのコマンド
-----------------------------------------------------------

:station: クライアントモード(子機)
:softAP: アクセスポイントモード(親機)
:station+softAP: クライアント＆アクセスポイントモード

.. csv-table:: ATコマンドの構文
   :header: "Command","内容","戻り値内容"
   :widths: 15,50,20


    "AT+CWMODE","WiFiモード選択(station/softAP/station+softAP)","( )"
    "AT+CWMODE_CUR","WIFI mode(sta/AP/sta+AP)Won’t save to Flash","( )"
    "AT+CWMODE_DEF","WIFI default mode(sta/AP/sta+AP)Save to Flash","( )"
    "AT+CWJAP","アクセスポイントに接続する","( )"
    "AT+CWJAP_CUR","Connect to AP, won’t save to Flash","( )"
    "AT+CWJAP_DEF","Connect to AP, save to Flash","( )"
    "AT+CWLAP","接続可能なアクセスポイントを表示","( )"
    "AT+CWQAP","アクセスポイントへの接続を切る","( )"
    "AT+CWSAP","softAP使用時の詳細設定","( )"
    "AT+CWSAP_CUR","Set configuration of ESP8266 softAP Won’t save to Flash.","( )"
    "AT+CWSAP_DEF","Set configuration of ESP8266 softAP Save to Flash.","( )"
    "AT+CWLIF","softAP使用時にAPに接続されているIPを表示","( )"
    "AT+CWDHCP","Enable/Disable DHCP, [@deprecated]","( )"
    "AT+CWDHCP_CUR","Enable/Disable DHCP, won’t save to Flash","( )"
    "AT+CWDHCP_DEF","Enable/Disable DHCP, save to Flash","( )"
    "AT+CWAUTOCONN","Connect to AP automatically when power on","( )"
    "AT+CIPSTAMAC","Set mac address of ESP8266 station[@deprecated]","( )"
    "AT+CIPSTAMAC_CUR","Set mac address of ESP8266 station Won’t save to Flash.","( )"
    "AT+CIPSTAMAC_DEF","Set mac address of ESP8266 station Save to Flash.","( )"
    "AT+CIPAPMAC","Set mac address of ESP8266 softAP[@deprecated]","( )"
    "AT+CIPAPMAC_CUR","Set mac address of ESP8266 softAP Won’t save to Flash.","( )"
    "AT+CIPAPMAC_DEF","Set mac address of ESP8266 softAP Save to Flash.","( )"
    "AT+CIPSTA","Set IP address of ESP8266 station, [@deprecated]","( )"
    "AT+CIPSTA_CUR","Set IP address of ESP8266 station Won’t save to Flash.","( )"
    "AT+CIPSTA_DEF","Set IP address of ESP8266 station Save to Flash.","( )"
    "AT+CIPAP","Set IP address of ESP8266 softAP Won’t save to Flash.","( )"
    "AT+CIPAP_CUR","Set IP address of ESP8266 softAP Save to Flash.","( )"
    "AT+CIPAP_DEF","Set IP address of ESP8266 softAP, [@deprecated]","( )"




3.ATコマンド TCP/IP及びUDP周りのコマンド
-----------------------------------------------------------
.. csv-table:: ATコマンドの構文
   :header: "Command","内容","戻り値内容"
   :widths: 15,50,20

    "AT+CIPSTATUS", "コネクション状態の表示","( )"
    "AT+CIPSTART", "TCP/IP及びUDPへの接続先設定＆接続開始","( )"
    "AT+CIPSEND", "データー送信モード","( )"
    "AT+CIPSENDEX", "Send data, if <length> or '\0' is met, data will be sent","( )"
    "AT+CIPSENDBUF", "Write data into TCP-send-buffer","( )"
    "AT+CIPBUFRESET", "Reset segment ID count","( )"
    "AT+CIPBUFSTATUS", "Check status of TCP-send-buffer","( )"
    "AT+CIPCHECKSEG", "Check if a specific segment is sent or not","( )"
    "AT+CIPCLOSE", "コネクションを切断","( )"
    "AT+CIFSR", "ローカルIPの表示","( )"
    "AT+CIPMUX", "マルチコネクションモードの設定","( )"
    "AT+CIPSERVER", "サーバーモードとして設定","( )"
    "AT+CIPMODE", "転送モードの設定","( )"
    "AT+SAVETRANSLINK", "Save transparent transmission link to Flash","( )"
    "AT+CIPSTO", "TCPのタイムアウト時間の設定","( )"
    "AT+CIUPDATE", "Upgrade firmware through network","( )"
    "AT+PING", "PINGコマンド","( )"
    "AT+CIPDINFO","Show remote IP and remote port with '+IPD'","( )"







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

:初版: 2015/08/09

:作成者: Yuta kitagami
:連絡先: kitagami@artifactnoise.com
:twitter: @nonNoise