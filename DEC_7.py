import  csv
# opening
def opening():
    name = input('こんにちは!私はRobokoです。あなたの名前は何ですか?')

    #asking(好きなレストランを質問する  , CSV書き込み )
    # 好きなレストランを質問する
    def ask_restaurant():
        restaurant = input(name + 'さん。あなたのお気にりのレストランは何ですか？')

        # CSV書き込み
        with open('restaurant_list.csv', 'w')as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()  # header
            writer.writerow({'Name': restaurant, 'Count': 1})

        return restaurant
    ask_restaurant()


    # closing()
    def closing():
        print(name + 'さん。ありがとうございました。良い一日を!さようなら。')

    closing()
# opening()

# def closing():
#
opening()