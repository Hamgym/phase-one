# Task 1

def find_and_print(messages, current_station):
  # 每個分支都有對應的維度
  coords = {
    "Songshan":(0,0),
    "Nanjing Sanmin":(1,0),
    "Taipei Arena":(2,0),
    "Nanjing Fuxing":(3,0),
    "Songjiang Nanjing":(4,0),
    "Zhongshan":(5,0),
    "Beimen":(6,0),
    "Ximen":(7,0),
    "Xiaonanmen":(8,0),
    "Chiang Kai-Shek Memorial Hall":(9,0),
    "Guting":(10,0),
    "Taipower Building":(11,0),
    "Gongguan":(12,0),
    "Wanlong":(13,0),
    "Jingmei":(14,0),
    "Dapinglin":(15,0),
    "Qizhang":(16,0),
    "Xiaobitan":(16,1),
    "Xindian City Hall":(17,0),        
    "Xindian":(18,0),        
  }
  # 只保留訊息中的站台名稱資訊
  for name in messages:
    for station in coords:
      if messages[name].find(station) >= 0:
        messages[name] = station
        break
  # 計算從當前站台到其他站台所需的步數
  step = []
  for name in messages:
    x1, y1 = coords[messages[name]]
    x0, y0 = coords[current_station]
    step.append(abs(x1-x0)+abs(y1-y0))
  # 印出對應最小步數的人名
  index = step.index(min(step))
  i = 0
  for name in messages:
    if i == index:
      print(name)
      break
    i += 1

messages={
  "Leslie":"I'm at home near Xiaobitan station.",
  "Bob":"I'm at Ximen MRT station.",
  "Mary":"I have a drink near Jingmei MRT station.",
  "Copper":"I just saw a concert at Taipei Arena.",
  "Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian


print("=====================================")

# Task 2

# 建立顧問的排程表
schedules = [[0 for _ in range(24)] for _ in range(3)]
# 定義預約函式
def book(consultants, hour, duration, criteria):  
  # 檢查是否可預約  
  def check(schedule, appt):
    for i in range(24):
      if (schedule[i] & appt[i]):      
        return False
    return True
  # 根據評價預約
  def rate_oriented():    
    rates = [consultant["rate"] for consultant in consultants]
    s_rates = sorted(rates, reverse=True)
    for rate in s_rates:
      index = rates.index(rate)
      if check(schedules[index], appt):
        for i in range(24):
          if appt[i] == 1: schedules[index][i] = 1            
        print(consultants[index]["name"])
        break
    else:
      print("No Service")
  # 根據價格預約
  def price_oriented():    
    prices = [consultant["price"] for consultant in consultants]
    s_prices = sorted(prices)
    for price in s_prices:
      index = prices.index(price)
      if check(schedules[index], appt):
        for i in range(24):
          if appt[i] == 1: schedules[index][i] = 1            
        print(consultants[index]["name"])
        break
    else:
      print("No Service")

  # 建立顧客的預約表(appointment)
  appt = [0 for _ in range(24)]
  for i in range(hour, hour+duration): appt[i] = 1    
  # 根據標準進行預約
  if criteria == "rate":
    rate_oriented()
  else:
    price_oriented()

consultants=[
  {"name":"John", "rate":4.5, "price":1000},
  {"name":"Bob", "rate":3, "price":1200},
  {"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


print("=====================================")

# Task 3

def func(*data):
  import math
  mids = [name[math.floor(len(name)/2)] for name in data]
  counts = [mids.count(char) for char in mids]
  i = 0
  for count in counts:
    if count == 1:
      print(data[i])
      break
    else:
      i += 1
  else:
    print("沒有")

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安


print("=====================================")

# Task 4

def get_number(index):
  diff = [4,4,-1]
  result = 0
  for i in range(index):
    result += diff[i%3]
  print(result)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


print("=====================================")

# Task 5

def find(spaces, stat, n):
  avail = [spaces[i]*stat[i] for i in range(len(spaces))]  
  s_avail = sorted(avail)
    
  for num in s_avail:
    if num >= n:
      print(avail.index(num))
      break
  else:
    print(-1)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2