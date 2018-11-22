# NumberFilter
provisional headers are shown
pip install selenium

pip install Pyinstaller

pyinstaller .\Scripts\Main.py -w -F


https://www.cnblogs.com/zhaof/p/6953241.html
https://www.cnblogs.com/luozx207/p/9003214.html
http://selenium-release.storage.googleapis.com/index.html
https://www.cnblogs.com/yogayan/p/6710119.html
https://www.cnblogs.com/wisdom-1983/p/5027396.html
https://blog.csdn.net/illegalname/article/details/77164521
https://www.cnblogs.com/qingchunjun/p/4208159.html
https://www.cnblogs.com/kongzhagen/p/6145429.html
https://jingyan.baidu.com/article/a378c960b47034b3282830bb.html

chromedriver.exe webdriver.ChromeOptions()
https://www.cnblogs.com/z-x-y/p/9026226.html

隐藏 chromedriver.exe 修改selenium包中的service.py
https://blog.csdn.net/La_vie_est_belle/article/details/81252588
https://www.cnblogs.com/gaigaige/p/7881130.html
https://stackoverflow.com/questions/33983860/hide-chromedriver-console-in-python?rq=1

self.process = subprocess.Popen(cmd, env=self.env,
    close_fds=platform.system() != 'Windows',
    stdout=self.log_file,
    stderr=self.log_file,
    stdin=PIPE,
    creationflags=subprocess.CREATE_NO_WINDOW) <- add code


切换frame
https://blog.csdn.net/huilan_same/article/details/52200586
driver.switch_to.frame(frame)

取值
textValue = elem_Txt.get_attribute("value")
textValue = driver.execute_script("return arguments[0].value", elem_Txt)
赋值
driver.execute_script("return arguments[0].value='1234=1'", elem_Txt)