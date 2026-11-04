# SAKKI-JIJI

中学受験の **社会・時事問題** に特化した記憶アプリ。キャラクター「サッ記マン」の時事版（兄弟リポジトリ：[SAKKI-MAN](https://github.com/HNHN-g1t/SAKKI-MAN)）。

## アプリ（スマホで開く）

- [時事ニュースクイズ](https://sakki-jiji.vercel.app/jiji-quiz/) … ニュースの4択 → 解説 → 「つながる知識」（[出典一覧](apps/jiji-quiz/SOURCES.md)）

## ドキュメント

| ファイル | 中身 |
|---|---|
| [docs/ideas.md](docs/ideas.md) | これから足したい機能・問題 |
| [apps/jiji-quiz/SOURCES.md](apps/jiji-quiz/SOURCES.md) | 問題の出典と確認日 |

## 前提

- 対象：小4〜小6の中学受験生（と保護者）
- 範囲：2027年入試に向けた時事（おおむね2025年夏〜2026年秋のニュース）と、そこからつながる地理・歴史・公民の知識
- 方針：ニュースで「おっ」と思わせて、教科書の知識で「定着」させる

## 最近の変更

- 2026-11-04 Claude：Vercel と連携（https://sakki-jiji.vercel.app/）。コミット作者が Vercel アカウント外だと公開されないため、作者を HNHN に統一（CLAUDE.md に明記）
- 2026-11-04 Claude：リポジトリ作成。SAKKI-MAN と同じ形式（apps/・tools/build_site.py・site/・vercel.json・GitHub Pages）で、時事ニュースクイズ v1 を追加（6コース36問。政治・世界・経済くらし・人口社会・文化スポーツ・〇〇周年。4択→解説→つながる知識、コースごとの最高点と👑、まちがえた問題だけ復習）
