# python实现shellcode异或加密自动化

实现的结果如下：
1.python脚本里面xor key随机生成 长度16位
2.加密后的payload和key直接写入到模板里面
3.编译 使用gcc编译  每次输出文件名随机 完成一个自动化过程

用法

```shell
python main.py shellcode.bin
```

其中shellcode.bin是自己的shellcode二进制文件,项目中的是一个弹出错误框的shellcode，有如下效果：

![image-20231104171530091](https://raw.githubusercontent.com/fdxsec/md_images/master/img/image-20231104171530091.png)

![image-20231104171502906](https://raw.githubusercontent.com/fdxsec/md_images/master/img/image-20231104171502906.png)


注意，在编译的时候可以在脚本自定义编译命令
学习免杀时写的一个脚本，没有什么技术难度，大佬勿喷。还有许多可以改进的地方，比如隐藏掉黑窗口，大家可以在模板文件里面修改或者加入更多个性化的东西。
项目地址：https://github.com/fdxsec/xor_shellcode
经过测试，是可以过掉火绒的

![image](https://github.com/fdxsec/xor_shellcode/assets/117912115/96666b17-5ed5-4704-af28-4657ec3df9ce)

