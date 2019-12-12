#!/usr/bin/python
# coding: utf-8

git_base_url = "https://github.com/gfw-breaker/banned-news/blob/master/pages"

head = ''

#head = "#### 由于频繁封锁，请参考 [手把手翻墙教程](https://github.com/gfw-breaker/guides/wiki/)，安卓用户请使用 [网门](https://github.com/gfw-breaker/bn-android/blob/master/ogate.md) 或 [禁闻聚合](https://github.com/gfw-breaker/bn-android) 免翻墙观看热门YouTube频道 \n\n"

#head += "#### 旧版本禁闻聚合安卓APP已经失效，请删除，然后重新[下载安装新版本](https://github.com/gfw-breaker/bn-android) \n\n"

#head += "#### [热点新闻](热点新闻.md)  &nbsp;&nbsp;|&nbsp;&nbsp; [明慧二十周年报告](https://github.com/gfw-breaker/mh-reports/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp;[明慧期刊](https://github.com/gfw-breaker/mh-qikan) &nbsp;&nbsp;|&nbsp;&nbsp; [明慧海外之窗](https://github.com/gfw-breaker/mh-news/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [神韵特别报道](https://github.com/gfw-breaker/mh-news/blob/master/shenyun.md) \n"

#head += "#### [法轮功真相](https://github.com/gfw-breaker/truth/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [九评共产党](../../../../9ping.md/blob/master/README.md) &nbsp;|&nbsp; [解体党文化](../../../../jtdwh.md/blob/master/README.md)  &nbsp;|&nbsp; [共产主义的终极目的](../../../../gczydzjmd.md/blob/master/README.md) &nbsp;|&nbsp; [魔鬼在统治我们的世界](../../../../mgztzwmdsj.md/blob/master/README.md) \n"

menu = "#### [首页](https://github.com/gfw-breaker/banned-news/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [手把手翻墙教程](https://github.com/gfw-breaker/guides/wiki) &nbsp;&nbsp;|&nbsp;&nbsp; [禁闻聚合安卓版](https://github.com/gfw-breaker/bn-android) &nbsp;&nbsp;|&nbsp;&nbsp; [网门安卓版](https://github.com/oGate2/oGate) &nbsp;&nbsp;|&nbsp;&nbsp; [神州正道安卓版](https://github.com/SzzdOgate/update) \n\n"

tail = "#### [首页](https://github.com/gfw-breaker/banned-news/blob/master/README.md) &nbsp;|&nbsp; [一键翻墙软件](https://github.com/gfw-breaker/nogfw/blob/master/README.md) &nbsp;| [《九评共产党》](https://github.com/gfw-breaker/9ping.md/blob/master/README.md#九评之一评共产党是什么) | [《解体党文化》](https://github.com/gfw-breaker/jtdwh.md/blob/master/README.md) | [《共产主义的终极目的》](https://github.com/gfw-breaker/gczydzjmd.md/blob/master/README.md)\n\n"

proxy = "\n\n#### [翻墙必看视频（文昭、江峰、法轮功、八九六四、香港反送中...）](https://github.com/gfw-breaker/banned-news/blob/master/pages/link3.md)\n\n"

def write_page(channel, f_name, f_path, title, link, content):
	new_link = git_base_url + '/' + channel + '/' + f_name
	body = '### ' + title
	body += "\n------------------------\n\n" + menu + "\n\n" +  content
	body += "\n<hr/>\n手机上长按并复制下列链接或二维码分享本文章：<br/>"
	body += "\n" + new_link + " <br/>"
	body += "\n<a href='" + new_link + "'><img src='" + new_link + ".png'/></a> <br/>"
	body += "\n原文地址（需翻墙访问）：" + link + "\n"
	body += "\n\n------------------------\n" + tail 
	body += "\n<img src='http://gfw-breaker.win/banned-news/" + f_path[3:] + "' width='0px' height='0px'/>"
	fh = open(f_path, 'w')
	fh.write(body)
	fh.close()


