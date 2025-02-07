# YHK-Windows-Driver

Driver for mini **cat/rabbit** **thermal** printer of the **YHK** type

Based off [YHK-Cat-Thermal-Printer](https://github.com/abhigkar/YHK-Cat-Thermal-Printer) and [virtualPrinter](https://github.com/TheHeadlessSourceMan/virtualPrinter) source code.
Both projects, including this one, NEEDS big refactoring. But I don't care that much.

# How to use?

1) Download the repository
2) Install Pillow, and GhostScript (and maybe other libraries, idk)
3) Turn on your printer and connect it to your Windows PC
4) Get your BT MAC Address from the connected printer
5) Copy it and paste it into "printerMACAddress" variable in "myPrinter.py"
6) Find "gswin64c.exe" or "gswinc.exe", it's usually in: "C:\Program Files (x86 if present)\gs\gsVERSION\bin\gswin(64 if present)c.exe"
7) Copy the path and paste it into "GHOSTSCRIPT_APP" variable in "myPrinter.py"
8) Run "myPrinter.py", the driver will create a new device, which you can print to. 

# Warning

I recommend you to not think about how it works. I don't wanna know or think about it, it just works - and it's all I need from it.

If you have a few extra days, please somebody refactor this, cause this is a huge pile of garbage, but a working pile of garbage, so I can't complain here.

No, I will not help you with any of this, if it does not work for you. Please, fix it yourself, and maybe submit a pull request if you want to. Thanks.

# License

IDK what's about licenses here, cause virtualPrinter is distributed with MIT license, and YHK-Cat-Thermal-Printer is not packed with any.

So I'm gonna publish it with MIT, if any listed repo's owners have any questions - reach me via [Telegram](https://t.me/Pomorgite)