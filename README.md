# 序
昨天剛好逛到[vliucc](https://github.com/vliucc/taiwanlottery)的taiwanlottery project，發了issue問一下發現沒有回應，於是乾脆自己開一個project來做

# taiwan_lottery

程式內容由[台灣彩卷](http://www.taiwanlottery.com.tw/index_new.aspx)擷取，兌獎還是請由台灣彩卷官網為主。

# 程式邏輯

[台灣彩卷](http://www.taiwanlottery.com.tw/index_new.aspx)官網的source code把開獎球號顏色區隔，於是先把全部球依照顏色爬取，之後取用只要對照官網顏色就可以取用

開獎日期 開獎期號 也是一次爬取到list中 之後在依照網頁的source code的blocl區隔來抓取

開獎日期 開獎期號的變數名稱
```python
date    = []#Announced date
periods = [] #Number of periods
```
# 完成進度

- 威力彩

- 大樂透

- 今彩539

- 39合樂彩

# 螢幕截圖

![screenshoot](https://i.imgur.com/3PAd2hf.png)
