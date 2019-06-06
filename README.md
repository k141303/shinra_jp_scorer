# shinra_scorer_2019
森羅プロジェクト2019用のスコアラーです。

カテゴリー毎の採点ができます。
オプションを指定することでオフセットずれの確認もできます。

## 使い方
~~~bash
python3 scoring.py [正答のパス] \
                   [システム結果のパス]
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
~~~bash
python3 scoring.py dataset/Airport_Mini_Answer.json \
                   dataset/Airport_Dummy_Result.json \
                   --html dataset/Airport_HTML \
                   --text dataset/Airport_TEXT \
                   --target dataset/target.csv \
                   --error error \
                   --score score
~~~
