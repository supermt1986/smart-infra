---
name: arch-diagram
description: 生成された Terraform スクリプトを Mermaid アーキテクチャのラフスケッチと Python diagrams でレンダリングされたプロフェッショナルなアーキテクチャ図に同時に変換します。
---

# 目標

`output/[プロジェクトコード]/terraform/` ディレクトリに配置された Terraform 設定コードを直感的な視覚的アーキテクチャ図に変換します。
このスキルを実行するたびに、**必ずデフォルトで Mermaid のラフスケッチと Python Diagrams のプロフェッショナル図を同時に生成する必要があります**。
プロジェクトコードがわからない場合は、ユーザーに尋ねてください。

# 生成タスク

以下の2つのタスクを順番に実行する必要があります：

## タスク A: Mermaid アーキテクチャ図 (クイックプレビュー)

1. `output/[プロジェクトコード]/terraform/` 内のすべての `.tf` ファイルを分析します。
2. コアリソースとそれらの論理的関係を抽出します。
3. 標準的な Mermaid 構文 `graph TB` を使用してフローチャートを作成します。
4. `subgraph` を最大限に活用して、ネットワークの分離や論理グループを表現します。一般的な絵文字を使用して異なるリソースを表現できます（例: 🌐 VPC, 🖥️ EC2, 🗄️ SQL）。
5. **極めて重要な Mermaid の互換性要件:**
    - Node ID と subgraph ID は、半角英字とアンダースコアのみで構成される必要があり、**決して**スペース、ダッシュ、またはその他の句読点を含めてはいけません。
    - すべての Label (表示テキスト) に特殊記号や日本語などの複雑な文字が含まれる場合は、**必ずダブルクォーテーションで囲む**必要があります。
6. 最終的な Mermaid コードを `output/[プロジェクトコード]/diagrams/architecture.md` ファイルに書き込みます。**注意：必ずファイルを書き出すよう強制してください。**

## タスク B: Python Diagrams 図表 (再利用ロジックのヒントを含む)

1. Terraform のコアリソースの関係を分析します。
2. コードの再利用性を高めるために、ユーザーが `.agents/skills/arch-diagram/scripts/` に基本テンプレートをすでに持っているかどうかを参照し、存在する場合はそのヘルパー関数をインポートするか、そのパターンに従って構築してください。
3. `output/[プロジェクトコード]/diagrams/generate.py` という名前の Python スクリプトを生成します。
4. このスクリプトは `diagrams` ライブラリと関連するクラウドプロバイダーのアイコンをインポートする必要があります（例：`from diagrams.aws.compute import EC2`）。
5. スクリプトの最後に、結果の画像が同じディレクトリに出力されるようにコードを追加します。例：`with Diagram("Cloud Architecture", show=False, filename=f"output/{project_name}/diagrams/architecture"):`
6. **極めて重要な自動化ステップ:** Python スクリプトを実行する前に、システムに環境が整っているかを自動的にチェックし、不足している場合は**自発的に以下のコマンドを実行して依存関係をインストールしてください（ユーザーに手動操作を求めないこと）**：
   - ターミナルで `python -c "import diagrams"` を実行してチェックし、エラーが出た場合は `pip install diagrams` を実行します。
   - `dot -V` コマンドを実行して graphviz があるかチェックし、見つからない場合は `brew install graphviz` (macOSの場合) または `apt-get install graphviz` などを自発的に実行してインストールします。
7. 環境が確認できたら、コマンドを実行してスクリプトを実行します：`python output/[プロジェクトコード]/diagrams/generate.py`
8. PNG 画像を `output/[プロジェクトコード]/diagrams/architecture.png` に出力します。

# 実行後のステップ
生成が完了したらユーザーに伝えてください：「アーキテクチャ図がすべて準備できました。チャットボックスは直接のプレビューをサポートしていないため、Mermaid のラフスケッチをプレビューするには `output/[プロジェクトコード]/diagrams/architecture.md` をクリックして開くか、同ディレクトリ内の `.png` 画像を参照して最終的な描画結果を確認することをお勧めします。」
