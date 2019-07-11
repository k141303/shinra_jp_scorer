# shinra_scorer_2019
森羅プロジェクト2019用のスコアラーです。

カテゴリー毎に採点ができます。  
(全カテゴリーの同時採点は今後の実装予定とします。)  
オプションを指定することでオフセットずれの確認もできます。  

html_offset/text_offsetのそれぞれで採点を行います。  
どちらかのみでの採点を行いたい場合には、html_offset/text_offsetの必要な方のみをシステム結果に記載してください。  

## 使い方
~~~bash
python3 scoring.py [正答のワンライナーjsonのパス] \
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
~~~Python
from shinra_scorer_2019 import get_score

#オフセットズレの確認をしない場合
score = get_score(answer, result ,target = target)

#オフセットズレの確認をする場合
score, error = get_score(answer, result, target = target, html_path = html, plane_path = text)
~~~
answer : 正答ワンライナーjsonのパス(listとして読み込んだデータでも可)  
result : システム結果ワンライナーjsonのパス(listとして読み込んだデータでも可)  
target : 採点対象のpage_idを列挙したcsvファイルのパス(listでも可)  
html_path : htmlファイルが格納されたフォルダのパス  
text_path : textファイルが格納されたフォルダのパス
