# shinra_scorer_2019
森羅プロジェクト2019用のスコアラーです。

カテゴリー毎に採点ができます。
(全カテゴリーの同時採点は今後の実装予定とします。)
オプションを指定することでオフセットずれの確認もできます。

システム結果内のhtml_offset/text_offsetの存在する方で採点を行います。
両方存在する場合は両方で採点を行います。

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
dataset下にデータが用意してあります。実行してみてください。
~~~bash
python3 scoring.py dataset/Airport_Mini_Answer.json \
                   dataset/Airport_Dummy_Result.json \
                   --html dataset/Airport_HTML \
                   --text dataset/Airport_TEXT \
                   --target dataset/target.csv \
                   --error error \
                   --score score
~~~


## Pythonモジュールとして呼び出す
~~~Python
import score

#オフセットズレの確認をしない場合
score = get_score(args.answer, args.result ,target = args.target)

#オフセットズレの確認をする場合
score, error = get_score(args.answer, args.result, target = args.target, html_path = args.html, plane_path = args.text)
~~~
answer : 正答(w)
## Pythonモジュールとして呼び出すan
## Pythonモジュールとして呼び出すn
## Pythonモジュールとして呼び出すra
## Pythonモジュールとして呼び出すi
## Pythonモジュールとして呼び出すn
## Pythonモジュールとして呼び出すa
## Pythonモジュールとして呼び出すwe
## Pythonモジュールとして呼び出すi
## Pythonモジュールとして呼び出すl
## Pythonモジュールとして呼び出すu
## Pythonモジュールとして呼び出す
