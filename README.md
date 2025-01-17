# taiwan_lottery

The program retrieves data from [Taiwan Lottery](http://www.taiwanlottery.com.tw/index_new.aspx). For prize verification, please refer to the official Taiwan Lottery website.

# Program Logic

The source code of the [Taiwan Lottery](http://www.taiwanlottery.com.tw/index_new.aspx) website separates the colors of the winning numbers. Therefore, all numbers are first crawled by color. Once retrieved, the colors can be matched to the official website for usage.

Both the draw date and draw period are crawled into a list at once. Subsequently, these are extracted based on the block division in the webpage's source code.

Variables for the draw date and draw period:
```python
date    = [] # Announced date
periods = [] # Number of periods
```

# Screenshot

![screenshoot](https://i.imgur.com/VBA4xXU.png)
