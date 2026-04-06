# Smart Infra エージェント設定ガイド

Smart Infra プロジェクトは、エージェントのスキル (Agent Skills) に基づいたインフラストラクチャ自動化ツールセットです。

## ディレクトリ構造
プロジェクトにはいくつかの事前定義されたスキル (Skills) が含まれています：
- `.agents/skills/cloud-architect`: クラウドアーキテクトの視点から、プロジェクトの要件を明確化します。
- `.agents/skills/iac-generate`: Terraform コードを生成します。
- `.agents/skills/arch-diagram`: Terraform のアーキテクチャ図をレンダリングします。
- `.agents/skills/infra-flow`: 統合されたガイドプロセスを提供するマスターディスパッチャです。

## 行動ガイドライン
1. デフォルトでは、ユーザーが新しいクラウドアーキテクチャのアイデアを伝えてきた場合、自動化された要件ガイド、IaCコード生成、および描画フローを開始するために `infra-flow` を直接実行することをユーザーに推奨できます。
2. ユーザーのデータを保存する際は、常に `output/[プロジェクトコード]/terraform` や `output/[プロジェクトコード]/diagrams` などのパスを使用してください。
3. `.agents/skills` 配下のファイルを参考として積極的に活用することを忘れないでください。
