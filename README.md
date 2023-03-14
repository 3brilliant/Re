# ## 前言
本文为本人学习的总结，从<font color="	#FF0000">***规则到实战案例***</font>，从若有不懂可私信~~~:gift_heart::gift_heart::gift_heart::gift_heart::gift_heart::gift_heart:
## 一，什么是正则表达式？
正则表达式（Regular Expression），也叫作正则式、正规表示式、规则表达式等，是一种用于匹配文本的模式，它可以用来检查文本中是否包含特定的字符、字符串或格式，并且可以在文本中进行查找、替换或提取等操作的工具。通过使用正则表达式，可以快速、灵活地匹配、查找和替换符合某种模式的字符串。

正则表达式通常由普通字符和特殊字符（也称为元字符）组成。普通字符可以匹配自身，而特殊字符则用于描述一些特定的字符或字符集合，或者规定匹配的规则、次数、优先级等。

在使用正则表达式时，通常需要先编写一个正则表达式的模式，然后将该模式应用到目标字符串中进行匹配。在编写正则表达式时，需要考虑以下几个方面：

* 匹配的范围：需要明确要匹配的文本范围，是整个字符串还是其中一部分。

* 匹配的规则：需要明确要匹配的文本规则，是某个字符、某个字符串、某种格式，还是某个字符集合。

* 特殊字符的转义：需要注意一些特殊字符在正则表达式中具有特殊的含义，需要进行转义才能匹配其字面意义。例如，要匹配句子中的问号符号，可以使用\?进行匹配。

* 量词的使用：需要根据具体的匹配规则和需求，合理使用量词进行匹配。需要注意贪婪模式和非贪婪模式的区别，以及匹配优先级的问题。

* 分组和捕获：需要根据需求合理使用分组和捕获，以便后续操作中能够方便地使用匹配到的文本。

在实际应用中，可以使用在线正则表达式测试工具来测试和调试正则表达式，例如[Regex101](https://regex101.com/)、[RegExr](https://www.oschina.net/p/regexr?hmsr=aladdin1e1)等工具都可以帮助我们验证正则表达式的正确性和性能。

## 二，应用范围
正则表达式作为一种强大的文本处理工具，广泛应用于各种编程语言、文本编辑器、数据库等工具中。正则表达式能够快速、灵活地匹配、查找和替换符合某种模式的字符串，具有以下应用范围：

* 数据处理和清洗：在处理和清洗各种数据时，正则表达式可以快速地匹配和过滤出符合要求的数据，提高数据处理的效率。

* 文本搜索和分析：在文本搜索和分析中，正则表达式可以用于快速定位和匹配关*键字、短语、格式等，方便文本分析和统计。

* 网络爬虫和数据抓取：在网络爬虫和数据抓取中，正则表达式可以用于快速匹配和提取目标网页中的数据，例如链接、标题、内容等。

* 编程语言和脚本编写：在编写各种编程语言和脚本时，正则表达式可以用于匹配和提取字符串、校验用户输入等操作。

* 文本编辑器和命令行工具：在文本编辑器和命令行工具中，正则表达式可以用于快速查找和替换符合要求的文本，提高文本编辑和操作的效率。

总之，正则表达式在各种文本处理和数据处理场景中都有广泛的应用，掌握它可以大大提高我们的工作效率和精度。

## 三，语法
|符号|作用|
|--|--|
.|匹配任意字符，但不包括换行符|
^|匹配字符串的开头|
$|匹配字符串的结尾|
[ ]|匹配括号内的任意一个字符，例如[abc]表示匹配a、b、c中的任意一个字符|
[^]|匹配不在括号内的任意一个字符，例如[^abc]表示匹配除了a、b、c以外的任意一个字符|
丨|匹配左右两边的任意一个字符或字符集合|
()|将括号内的字符或者字符集合作为一个分组，对分组使用量词和其他操作|
*|匹配前面的字符或字符集合出现0次或多次|
+|匹配前面的字符或字符集合出现1次或多次|
？|匹配前面的字符或字符集合出现0次或1次|
{n}|匹配前面的字符或字符集合恰好出现n次|
{n,}|匹配前面的字符或字符集合至少出现n次|
{n,m}|匹配前面的字符或字符集合出现n到m次|
\d|匹配任意一个数字字符，等同于[0~9]|
\D|匹配任意一个非数字字符，等同于[^0~9]|
\w|匹配任意一个字母、数字、下划线字符，等同于[a-zA-Z0-9]|
\W|匹配任意一个非字母、数字、下划线，等同于[^a-zA-Z0-9]|
\s|匹配任意一个空白字符，包括空格、制表符、换行符等|
\S|匹配任意一个非空白字符|
(?i)|忽略大小写匹配|
(?s)|将‘ . '匹配包括换行符在内的任意字符|
(?m)|多行匹配模式，将’^‘和'$'分别匹配每行的开头和结尾|
(?x)|忽略正则表达式中的空格和注释|
\b|匹配单词的边界|
\B|匹配非单词的边界|
\<|匹配单词的开头|
\>|匹配单词的结尾|
\A|匹配字符串的开头|
\Z|匹配字符串的结尾，但不包括最后的换行符|
\z|匹配字符串的结尾，类似于 $，但 \z 不受多行模式的影响，只匹配整个字符串的末尾|

***常用的正则表达式如下：***

1. 非负整数：`^\d+$`
2. 正整数：`^[0-9]*[1-9][0-9]*$`
3. 非正整数：`^((-\d+)|(0+))$`
4. 负整数：`^-[0-9]*[1-9][0-9]*$`
5. 整数：`^-?\d+$`
6. 非负浮点数：`^\d+(\.\d+)?$`
7. 正浮点数：`^((0-9)+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$`
8. 非正浮点数：`^((-\d+\.\d+)?)|(0+(\.0+)?))$`
9. 负浮点数：`^(-((正浮点数正则式)))$`
10. 英文字符串：`^[A-Za-z]+$`
11. 英文大写串：`^[A-Z]+$`
12. 英文小写串：`^[a-z]+$`
13. 英文字符数字串：`^[A-Za-z0-9]+$`
14. 英数字加下划线串：`^\w+$`
15. E-mail地址：`^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$`
16. URL：`^[a-zA-Z]+://(\w+(-\w+)*)(\.(\w+(-\w+)*))*(\?\s*)?$` 
17. 邮政编码：`^[1-9]\d{5}$`
18. 中文：`^[\u0391-\uFFE5]+$`
19. 电话号码：`^((\d2,3)|(\d{3}\-))?(0\d2,3|0\d{2,3}-)?[1-9]\d{6,7}(\-\d{1,4})?$`
20. 手机号码：`^((\d2,3)|(\d{3}\-))?13\d{9}$`
21.双字节字符(包括汉字在内)：`^\x00-\xff`
22. 匹配首尾空格：`(^\s*)|(\s*$)（像vbscript那样的trim函数）`
23. 匹配HTML标记：`<(.*)>.*<\/\1>|<(.*) \/>`
24. 匹配空行：`\n[\s| ]*\r`
25. 提取信息中的网络链接：`(h|H)(r|R)(e|E)(f|F) *= *('|")?(\w|\\|\/|\.)+('|"| *|>)?`
26. 提取信息中的邮件地址：`\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*`
27. 提取信息中的图片链接：`(s|S)(r|R)(c|C) *= *('|")?(\w|\\|\/|\.)+('|"| *|>)?`
28. 提取信息中的IP地址：`(\d+)\.(\d+)\.(\d+)\.(\d+)`
29. 提取信息中的中国手机号码：`(86)*0*13\d{9}`
30. 提取信息中的中国固定电话号码：`(\d3,4|\d{3,4}-|\s)?\d{8}`
31. 提取信息中的中国电话号码（包括移动和固定电话）：`(\d3,4|\d{3,4}-|\s)?\d{7,14`}
32. 提取信息中的中国邮政编码：`[1-9]{1}(\d+){5}`
33. 提取信息中的浮点数（即小数）：`(-?\d*)\.?\d+`
34. 提取信息中的任何数字 ：`(-?\d*)(\.\d+)?`
35. IP：`(\d+)\.(\d+)\.(\d+)\.(\d+)`
36. 电话区号：`/^0\d{2,3}$/`
37. 腾讯QQ号：`^[1-9]*[1-9][0-9]*$`
38. 帐号(字母开头，允许5-16字节，允许字母数字下划线)：`^[a-zA-Z][a-zA-Z0-9_]{4,15}$`
39. 中文、英文、数字及下划线：`^[\u4e00-\u9fa5_a-zA-Z0-9]+$`
40. 匹配中文字符的正则表达式： `[\u4e00-\u9fa5]`
41. 匹配双字节字符(包括汉字在内)：`[^\x00-\xff]`
42. 匹配空行的正则表达式：`\n[\s| ]*\r`
43. 匹配HTML标记的正则表达式：`/<(.*)>.*<\/\1>|<(.*) \/>/`
44. 匹配首尾空格的正则表达式：`(^\s*)|(\s*$)`
45. 匹配IP地址的正则表达式：`/(\d+)\.(\d+)\.(\d+)\.(\d+)/g //`
46. 匹配Email地址的正则表达式：`\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*`
47. 匹配网址URL的正则表达式：`http://(/[\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?`
48. sql语句：`^(select|drop|delete|create|update|insert).*$`


## 四，高级功能 
正则表达式除了基本语法外，还有一些高级功能，如下所示：

* 分组捕获：使用括号将模式分组，并可以通过编号或名称捕获分组匹配的内容，例如 (\d{3})-(\d{4}) 可以匹配 123-4567，并通过编号访问匹配的内容。
* 零宽断言：用于在匹配时指定一个位置，并匹配这个位置前面或后面的内容，但不包括这个位置本身，包括正向肯定预测 (?=...)、正向否定预测 (?<!...)、反向肯定预测 (?<=...)、反向否定预测 (?!...)。
* 命名捕获组：在分组捕获的基础上，使用 (?P<name>...) 来为分组指定一个名称，可以通过名称来访问匹配的内容。



* 后向引用：使用 \n 来引用前面的第 n 个分组匹配的内容，例如 (\d{3})-\1 可以匹配 123-123。

* 贪婪量词：在重复字符或字符集合时，默认为贪婪匹配，即尽可能多地匹配，例如 a.*b 会匹配 a 开头，以 b 结尾，中间包含任何字符的字符串。
* 非贪婪量词：在重复字符或字符集合时，使用 *?、+?、?? 来实现非贪婪匹配，即尽可能少地匹配，例如 a.*?b 会匹配 a 开头，以 b 结尾，中间包含任何字符的最短字符串。

## 五，案例
在实战项目之前，先对**re模块**进行了解。
#### 1.1，re模块中三个函数
**1.match函数**
* re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None
**注：** match只能匹配到一个

**2.search函数**
* e.search 扫描整个字符串，匹配成功则返回的是一个匹配对象（这个对象包含了我们匹配的信息）；当然，若是都找不到则返回None值。
**注：** search也只能匹配到一个，找到符合规则的就返回，不会一直往后找

**3.findall函数**
* 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。

**注：** match 和 search 是匹配一次 findall 匹配所有。

**4.总结**
: 查找并返回一个匹配项的函数有3个：search、match、findall，他们的区别分别是：

: search： 查找任意位置的匹配项
match： 必须从字符串开头匹配
findall： 整个字符串与正则完全匹配

| 案例|名称|
|--|--|
[案例一](./Demo1.py)|匹配QQ号码|
[案例二](./Demo2.py)|匹配座机号码|
[案例三](./Demo3.py)|检索所有python源文件|
[案例四](./Demo4.py)|匹配账号密码|
[案例五](./Demo5.py)|匹配html标签中的内容|
[案例六](./Demo6.py)|提取数字并计算|
[案例七](./Demo7.py)|匹配整数或者小数|








