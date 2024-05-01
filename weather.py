from API import fetch

infomation = fetch.weatherAPI("https://weathernews.jp/onebox/43.059635/141.357983055556/q=%E6%9C%AD%E5%B9%8C")#URLの入力
#とても取得に時間がかかります

print(infomation.fetch_weather())#天気の取得