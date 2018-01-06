# imu_subscriber

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Kuwamai/imu_subscriber.git
$ cd ~/catkin_ws/
$ catkin_make
```

何かしらでIMUのパブリッシャーを作る  
例えば以下のドライバパッケージ

```
$ roslaunch lab_usb_9axisimu_driver lab_usb_9axisimu_driver.launch  
```

ノード、トピックの確認
```
$ rosnode list
$ rostopic list
```

rosrunで起動してlogに保存

```
$ rosrun imu_subscriber imu_subscriber.py > log.txt
```

