""" ゲームの流れ
1.ゲームタイトルは「Puzzle&Monsters」（略して「Puzmon」）とする。
2.プレイヤーは、ゲームスタート時点で4匹のモンスター（青龍、朱雀、白虎、玄武）を従えている。
3.プレイヤーは、ゲームスタート直後に４匹の味方モンスターとパーティを編成してダンジョンに行く。
4.ダンジョンでは5回のバトルが発生し、すべてのバトルで敵モンスターのHPを0にすればゲームクリア。
  途中でパーティのHPが5になるとゲームオーバー。
5.各バトルは、パーティ対敵モンスター1匹の構図で戦う。敵モンスターのHPを0にすると次のバトルに進む。
6.バトルで戦う相手は、登場順に「スライム」「ゴブリン」「オオコウモリ」「ウェアウルフ」「ドラゴン」とする。
7.ゲーム終了時には、「GAME OVER!!」または「GAME CLERED!!」のメッセージとともに、倒した敵モンスターの数を表示する。 """

""" パラメータの概要
1.敵モンスターのパラメータは、名前、HP、最大HP、属性、攻撃力、防御力とする。
2.味方モンスターのパラメータは、敵モンスターのパラメータと同じとする。
3.パーティのパラメータは、プレイヤー名、4匹の味方モンスター、パーティのHP及び最大HP、防御力とする。
4.パーティ編成時、パーティに参加している味方モンスターのHPの合計値がパーティのHP及び最大HPとなる。
  また、味方モンスターの防御力の平均値がパーティの防御力となる。
5.ダンジョン内のバトルでは、パーティのHPが増減し、味方モンスターごとのHPは増減しない。 """

# 作成開始日：2026/02/17　作成者：平島　隼平

# インポート

# グローバル変数の宣言

# 関数宣言
def main():
    player=input('プレイヤー名を入力してください>>')
    print('*** Puzzle & Monsters ***')
    knock_down = go_dungeon(player)
    if knock_down==5:
        print('*** GAME CLERED!! ***')
        print(f'倒したモンスター数={knock_down}')
    else:
        print('*** GAME OVER!! ***')
        print(f'倒したモンスター数={knock_down}')

def go_dungeon(player):
    monsters=['スライム','ゴブリン','オオコウモリ','ウェアウルフ','ドラゴン']
    knock_down=0
    print(f'{player}はダンジョンに到達した')
    for i in monsters:
        is_win=do_battle(i)
        if is_win==1:
            knock_down += 1
        print(is_win)
    print(f'{player}はダンジョンを制覇した')
    return knock_down

def do_battle(monster_name):
    print(f'{monster_name}が現れた！')
    print(f'{monster_name}を倒した！')
    flag=1
    return flag


# main関数の呼び出し

main()
