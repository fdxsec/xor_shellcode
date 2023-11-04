# python实现shellcode异或加密自动化

实现的结果如下：
1.python脚本里面xor key随机生成 长度16位
2.加密后的payload和key直接写入到模板里面
3.编译 使用gcc编译  每次输出文件名随机 完成一个自动化过程

用法

```shell
python xorencrypt.py shellcode.bin
```

其中shellcode.bin是自己的shellcode二进制文件,项目中的是一个弹出错误框的shellcode，有如下效果：

![image-20231104171530091](https://raw.githubusercontent.com/fdxsec/md_images/master/img/image-20231104171530091.png)

![image-20231104171502906](https://raw.githubusercontent.com/fdxsec/md_images/master/img/image-20231104171502906.png)

学习免杀时写的一个脚本，没有什么技术难度，大佬勿喷。
