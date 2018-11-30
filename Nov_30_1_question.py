# opening
import os
import csv
name = input('こんにちは!私はRobokoです。あなたの名前は何ですか?')

# CSV存在確認
os.path.exists('restaurant_list.csv')

# CSVファイルが存在しない場合
if not os.path.exists('restaurant_list.csv'):
    # CSVファイル作成
    with open('restaurant_list_csv', 'w') as csv_file:
        csv_file.write('')



#　CSVファイルが存在する場合
    # CSVファイル内のデータ確認   (CSVファイル内のデータ確認 方法　ここがわかりません )





    # CSVファイルにデータが存在する場合
        #CSVファイル読込
        # 投票数の多い順にデータをソートする