# shinra_scorer_2019
森羅プロジェクト2019用のスコアラーです。

カテゴリー毎に採点ができます。  
(全カテゴリーの同時採点は今後の実装予定とします。)  
オプションを指定することでオフセットずれの確認もできます。  

html_offset/text_offsetのそれぞれで採点を行います。  
どちらかのみでの採点を行いたい場合には、html_offset/text_offsetの必要な方のみをシステム結果に記載してください。  

## 使い方
~~~bash
python3 shinra_scorer_2019 [正答のワンライナーjsonのパス] \
                           [システム結果のワンライナーjsonのパス]
~~~
以下はオプション引数
~~~
--html [HTMLファイルが格納されたフォルダパス](html_offsetのズレを確認する場合に指定)
--text [プレーンテキストファイルが格納されたフォルダパス](text_offsetのズレを確認する場合に指定)
--target [採点対象のpage_idを列挙したcsvファイルのパス](指定しない場合はシステム結果に含まれるpage_idが対象になります。)
--error [エラーファイルを書き出すフォルダパス](エラーを書き出したい場合に指定)
--score [スコアを書き出すフォルダパス](スコアを書き出したい場合に指定)
~~~
こんな感じです。  

## 使用例

dataset下に簡易なデータが用意してあります。試しに実行してみてください。
~~~bash
python3 shinra_scorer_2019 shinra_scorer_2019/dataset/Airport_Mini_Answer.json \
                           shinra_scorer_2019/dataset/Airport_Dummy_Result.json \
                           --html shinra_scorer_2019/dataset/Airport_HTML \
                           --text shinra_scorer_2019/dataset/Airport_TEXT \
                           --target shinra_scorer_2019/dataset/target.csv \
                           --error error \
                           --score score
~~~

  
## Pythonモジュールとして呼び出す

以下のようにPythonモジュールとして呼び出して使うこともできます。

~~~
from shinra_scorer_2019 import get_score
~~~

## 使用例

以下のように使います。

~~~Python:test.py
import json

RESULT_PATH = "shinra_scorer_2019/dataset/Airport_Dummy_Result.json"
ANSWER_PATH = "shinra_scorer_2019/dataset/Airport_Mini_Answer.json"
HTML_PATH = "shinra_scorer_2019/dataset/Airport_HTML"
PLAIN_PATH = "shinra_scorer_2019/dataset/Airport_TEXT"

def load_oneline_json(path):
    with open(path , "r") as f:
        oneline_json_file = f.readlines()
    return [json.loads(line) for line in oneline_json_file]

from shinra_scorer_2019 import get_score

if __name__ == "__main__":
    answer = load_oneline_json(ANSWER_PATH)
    result = load_oneline_json(RESULT_PATH)

    target = [678416, 1726754, 858418, 2416040, "993202", "1001711", "1001918"]

    """
    answer : 正答ワンライナーjsonのパス(ワンライナーjsonを1行ずつ読み込んでリストに格納したデータでも可)  
    result : システム結果ワンライナーjsonのパス(ワンライナーjsonを1行ずつ読み込んでリストに格納したデータでも可) 
    target : 採点対象のpage_idを列挙したcsvファイルのパス(listでも可)  
    html_path : htmlファイルが格納されたフォルダのパス  
    text_path : textファイルが格納されたフォルダのパス
    """
    score,error = get_score(answer, result, target = target, html_path = HTML_PATH, plain_path = PLAIN_PATH)
    #パスでも可
    #score,error = get_score(ANSWER_PATH, RESULT_PATH, target = target, html_path = HTML_PATH, plain_path = PLAIN_PATH)

    print("SCORE:{}".format(score))
    print("ERROR:{}".format(error))
~~~

上記コードを以下のようにダウンロードしたこのモジュールと同じ階層において

~~~
shinra_scorer_2019/
test.py
~~~

以下コマンドで実行してみてください。

~~~
python3 test.py
~~~
