import urllib.request as req
import json
import csv

districts = ["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"]
src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# 將來源一資料放入景點列表中
spot_arr = []
with req.urlopen(src1) as res:  
  data = json.load(res)
  spots = data["data"]["results"]
  for spot in spots:
    filelist = spot["filelist"]
    end = filelist.find("https",5)
    filelist = filelist[:end]  
    row = [spot["stitle"],spot["SERIAL_NO"],spot["longitude"],spot["latitude"],filelist]    
    spot_arr.append(row[:])

# 將來源二資料放入捷運列表中
mrt_arr = []
with req.urlopen(src2) as res:  
  data = json.load(res)  
  mrts = data["data"]
  for mrt in mrts:
    row = [mrt["SERIAL_NO"],mrt["MRT"],mrt["address"]]
    mrt_arr.append(row[:])

# 讓捷運的地址內容只留下分區
i = 0
for mrt in mrt_arr:
  for district in districts:
    if (mrt[2].find(district) >= 0):
      mrt_arr[i][2] = district
      break
  i += 1

# 以分區取代景點的流水號，並在最後附上捷運站。
i = 0
for spot in spot_arr:  
  for mrt in mrt_arr:
    if (mrt[0]==spot[1]):
      spot_arr[i][1] = mrt[2]
      spot_arr[i].append(mrt[1])
      break
  i += 1

# 將景點列表寫入spot.csv，不包括捷運站資訊。
with open("spot.csv", mode="w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  end = len(spot)-1
  for spot in spot_arr:
    writer.writerow(spot[:end])

# 建立捷運對應景點之字典
output = {}
for spot in spot_arr:  
  output[spot[5]] = []
for spot in spot_arr:
  output[spot[5]].append(spot[0])

# 將捷運及對應景點寫入mrt.csv
with open("mrt.csv", mode="w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)  
  for mrt in output:
    writer.writerow([mrt,*output[mrt]])