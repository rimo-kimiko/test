# opening
import os
import csv
name = input('こんにちは!私はRobokoです。あなたの名前は何ですか?')
#IF1 CSVファイル存在確認
if not os.path.exists('restaurant_list.csv'):
    #NO------1 CSVファイルが存在しない場合

    # CSVファイル作成
    with open('restaurant_list.csv', 'w') as csv_file:
        f=()

# CSVファイルを開く
with open('restaurant_list.csv') as csv_file:
    #CSVファイルのデータをリスト型変数代入
    restaurant_lst = list(csv.reader(csv_file))
    restaurant_lst_flat = [x for row in restaurant_lst for x in row]

    #IF2 CSVファイル内のデータが２件以上ある場合
    if int(len(restaurant_lst_flat))>=2:
    #YES------2        CSVファイルにデータが存在する場合

    # 投票数の多い順にデータをソートする
        restaurant_lst_flat.sort()
        print(restaurant_lst_flat)

    import collections
    c=collections.Counter(restaurant_lst_flat)

    values,counts = zip(*c.most_common())


    #LOOP1 CSVファイルデータのレストランリストループを行う
    for i in values:
        #オススメのレストランを紹介する。
        print('私のオススメのレストランは、'+ i +'です。')
        #IF3 YES,No尋ねる
        while True:
            choice = input('このレストランは好きですか? [Yes/No]:')
            #YES------3     オススメのレストランが好きな場合
            if choice in ['y', 'ye', 'yes', 'Yes', 'YES']:
        #csvのレストラン名にカウントを追加
                    break

            #NO-------3 オススメのレストランが嫌いな場合
            # else choice in ['n', 'no', 'No']:
            #         continue

    # 好きなレストランを質問する
    restaurant=input('あなたのお気にりのレストランは何ですか？')

    # CSV書き込み
    with open('restaurant_list.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name':restaurant, 'Count': 1})

    # 好きなレストランを質問する
restaurant=input('あなたのお気にりのレストランは何ですか？')

# CSV書き込み
with open('restaurant_list.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name':restaurant, 'Count':1})

 #closing
print(name + 'さん。ありがとうございました。良い一日を!さようなら。')