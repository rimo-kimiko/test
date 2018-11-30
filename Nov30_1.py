# opening

# CSV存在確認

# CSVファイルが存在しない場合

# CSVファイル作成


#　CSVファイルが存在する場合
    # CSVファイル内のデータ確認

    # CSVファイルにデータが存在する場合
        # 投票数の多い順にデータをソートする

        #CSVファイル読込

        # CSVファイルデータのレストランリストループを行う

            # オススメのレストランを紹介して好きか嫌いかを尋ねる
                #オススメのレストランが好きな場合　
                #csvのレストラン名にカウントを追加
                # リスト内の全てのレストランを紹介する


            #　オススメのレストランが嫌いな場合
                #レストランリスト内のレストラン名をカウントが多い順に紹介する
                #リスト内の全てのレストランを紹介する

                    #リスト内の全データの紹介が完了してループを抜ける

        # 好きなレストランを質問する
        restaurant = input(name + 'さん。どこのレストランが好きですか?')

        # CSV書き込み
        with open('restaurant_list.csv', 'a+') as csv_file:
        csv_file.write(restaurant)


    # CSVファイルにデータが存在しない場合

    # 好きなレストランを質問する
    restaurant = input(name + 'さん。どこのレストランが好きですか?')

    # CSV書き込み
    with open('restaurant_list.csv', 'a+') as csv_file:
    csv_file.write(restaurant)

# closing
