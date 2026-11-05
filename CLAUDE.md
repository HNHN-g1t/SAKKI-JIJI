# SAKKI-JIJI 作業メモ（Claude 向け）

中学受験・社会の暗記ヒーロー「サッ記マン」の **時事ネタ** 学習アプリ。兄弟リポジトリ [SAKKI-MAN](https://github.com/HNHN-g1t/SAKKI-MAN)（地図クイズ・キャラ設定）と同じ形式・同じ配色で作る。

## 公開URL（スマホで確認する場所）

メインは Vercel（ユーザーがスマホで見るのはこちら）:

- 入口: https://sakki-jiji.vercel.app/
- 時事ニュースクイズ: https://sakki-jiji.vercel.app/jiji-quiz/

予備に GitHub Pages（https://hnhn-g1t.github.io/SAKKI-JIJI/）。

main に push すると、Vercel（`vercel.json`）と GitHub Actions（`.github/workflows/pages.yml`）の両方が `tools/build_site.py` でビルドして公開する（1〜2分）。

**コミットの作者は必ず `HNHN <821yas@gmail.com>` にする**（`git config user.name HNHN` / `git config user.email 821yas@gmail.com`）。Vercel の無料プランは、Vercel アカウントにいない作者のコミットを公開しない（数秒で failure になる）。

## 作業ルール

- 質問されたら、まず質問に答える。制作・変更は、必要なら進めてよいか確認してから着手する。
- 確率・集計など数値が絡むものは、必ずコードを実行して結果を出す（暗算・推定で答えない）。
- 変更したら README.md「最近の変更」の先頭に `日付 Claude：内容` を1行足す。
- 検証が通ったら main に push まで済ませる（スマホで見られないと終わっていない）。

## 時事ニュースクイズ（apps/jiji-quiz）

- 問題は `data/questions.json`。`choices` の先頭が正解（画面では毎回まぜる）。`when`＝ニュースの時期、`exp`＝解説、`link`＝つながる教科書知識、`src`＝[SOURCES.md](apps/jiji-quiz/SOURCES.md) の出典番号、`checked`＝確かめた日、`area`＝`jp`（日本国内）か `world`（世界）、`rank`＝重要度 `S`/`A`（任意）、`tags`＝タグの配列（任意。例：`2026年愛知・名古屋大会`）
- 出題は **日本国内のできごとを重視**。「全部まぜて」は日本国内7問・世界3問（`template.html` の `ALL_WORLD`）。問題を足すときも日本国内を多めにする
- **時事は事実の正確さが命**。問題を足すときは必ずWebなどで公表資料を確かめ、SOURCES.md に出典を足す。速報値と確定値がちがう数字は、どちらかを明記する。確かめられないものは入れない
- `index.html` はビルドの出力。直接編集しない。`src/template.html` と `data/questions.json` を直す
- ビルド（Windows は `py -3`、それ以外は `python3`）。問題データの形（4択が重複なし・コースの存在など）もここで確かめる:

  ```
  py -3 apps/jiji-quiz/tools/build.py
  ```

- ビルドした `index.html` も必ずコミットする。忘れると Actions の「ビルド忘れチェック」で公開が止まる
- 検証: ビルド → ブラウザで 375px 幅で開き、横にはみ出さないこと・1コース最後まで解けること・コンソールエラーなし
- 記録は localStorage の `sakki-jiji-v1`（コースごとの最高点・問題ごとの正誤）

## ファビコン

SAKKI-MAN と同じ「記」マーク。元画像は `site/favicon-source.webp`。差し替えたら `py -3 tools/build_icons.py`（Pillow が必要）で `site/` に各サイズを作り直す。
スマホはアイコンを強く覚え込むので、画像を差し替えたら `site/index.html`・`src/template.html`・`site/manifest.webmanifest` の `?v=` の数字を上げる。

## アプリを増やすとき

`apps/<名前>/` に置き、`tools/build_site.py` の `APPS` と `site/index.html` のリンクに1行ずつ足す。
