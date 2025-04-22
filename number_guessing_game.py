import random

while True:
    print("=== ゲームスタート！数字を当ててみよう===")
    
    level = input("難易度を選択してください(easy / normal / hard) : ").lower()
    
    if level == "easy":
        max_num = 10
    elif level == "normal":
        max_num = 20
    elif level == "hard":
        max_num = 50
    else:
        print("無効な入力です。 easy / normal / hard から選んでください。 ")
        continue

    secret = random.randint(1, max_num)
    score = 100
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"{attempt}回目のチャンス！１〜{max_num}の数字を当てて！: "))

        if guess == secret:
            print("正解！")
            print(f"スコアは{score}点です")
            break
        elif guess > secret:
            print("ヒント：もっと小さいよ！")
        else:
            print("ヒント: もっと大きいよ! ")
        
        score -= 20
    else:
        print(f"残念！正解は{secret}でした。スコアは{score}点です ")
        
    again = input("もう一度遊びますか？ (y/n) : ")
    if again.lower() != "y":
        print("ゲーム終了！ありがとう！")
        break
                
                