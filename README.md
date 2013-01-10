blocktree
=========
Tries to figure out hierachy from device mapper and udev


INSTALL
=======

yum install python-pyudev python-pyblock

Run
===
As root 

```
./blocktree.py
```

Here you can see the output on my laptop, 2 LVs on seperate luks encrypted devices on 2 partitions
```
vg_tandoori-lv_swap
 ↳        luks-abc23be0-e933-4de6-92a0-ff656c34ca50
  ↳                /dev/sda3
--------------------------------------------------------------------------------
vg_tandoori-lv_root
 ↳        luks-2dfe6ecd-777e-4ebd-a4b3-c01f69ad9752
  ↳                /dev/sda5
--------------------------------------------------------------------------------
luks-2dfe6ecd-777e-4ebd-a4b3-c01f69ad9752
 ↳        /dev/sda5
--------------------------------------------------------------------------------
luks-abc23be0-e933-4de6-92a0-ff656c34ca50
 ↳        /dev/sda3

```


