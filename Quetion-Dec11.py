# フローチャート
import csv
# opening

#IF1 CSV存在確認

    #NO------1 CSVファイルが存在しない場合

    # CSVファイル作成


    # CSVファイルを開く
    # CSVファイルのデータをリスト型変数代入

#IF2 CSVファイル内のデータが２件以上ある場合

    #YES------2        CSVファイルにデータが存在する場合

    # 投票数の多い順にデータをソートする


    #LOOP1 CSVファイルデータのレストランリストループを行う

        #オススメのレストランを紹介する。
        #IF3 YES,No尋ねる
            #YES------3     オススメのレストランが好きな場合
            #csvのレストラン名にカウントを追加
            # break


            #NO-------3 オススメのレストランが嫌いな場合
            # continue

    # 好きなレストランを質問する


    # CSV書き込み

    # NO------2      CSVファイルにデータが存在しない場合

    # 好きなレストランを質問する


    # CSV書き込み



# closing


# 質問1 フローチャートのline9-16 の部分です　　ヘッダー Name、Count 取り出して レストラン名と
#   カウント数を表示してリストを作りたいのですが　うまく行きません
 # CSVファイル作成

with open('restaurant_list.csv', 'w') as csv_file:
    fieldnames = ['Name','Count']
    writer =csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()


# CSVファイルを開く
    with open('restaurant_list.csv') as csv_file:

    # CSVファイルのデータをリスト型変数代入
        restaurant_lst = list(csv.reader(csv_file))

        restaurant_lst_flat = [x for row in restaurant_lst for x in row]
        restaurant_lst_flat.remove('Name')
        restaurant_lst_flat.remove('Count')

#IF2 CSVファイル内のデータが２件以上ある場合
if len(restaurant_lst) >=2:
    #YES------2        CSVファイルにデータが存在する場合

    # 投票数の多い順にデータをソートする