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
6. 最終的な Mermaid コードをまず `.tmp/architecture.md` に書き込んでください。
7. 書き込み後、`mkdir -p output/[プロジェクトコード]/diagrams/ && mv .tmp/architecture.md output/[プロジェクトコード]/diagrams/architecture.md` を実行してください。**注意：必ずファイルを書き出すよう強制してください。**

## タスク B: Python Diagrams 図表 (再利用ロジックのヒントを含む)

1. Terraform のコアリソースの関係を分析します。
2. コードの再利用性を高めるために、ユーザーが `.agents/skills/arch-diagram/scripts/` に基本テンプレートをすでに持っているかどうかを参照し、存在する場合はそのヘルパー関数をインポートするか、そのパターンに従って構築してください。
3. `output/[プロジェクトコード]/diagrams/generate.py` という名前の Python スクリプトを生成します。
4. このスクリプトは `diagrams` ライブラリと関連するクラウドプロバイダーのアイコンをインポートする必要があります（例：`from diagrams.aws.compute import EC2`）。
5. スクリプトの最後に、結果の画像が同じディレクトリに出力されるようにコードを追加します。例：`with Diagram("Cloud Architecture", show=False, filename=f"output/{project_name}/diagrams/architecture"):`
6. 生成する Python 脚本自体は、まずは `.tmp/generate.py` に書き込んでください。
   - その後、`mkdir -p output/[プロジェクトコード]/diagrams/ && mv .tmp/generate.py output/[プロジェクトコード]/diagrams/generate.py` を実行します。
7. その後、環境チェックとインストールを自動で行い、コマンドを実行してスクリプトを実行します：`python output/[プロジェクトコード]/diagrams/generate.py`
8. PNG 画像を `output/[プロジェクトコード]/diagrams/architecture.png` に出力します。

# 実行後のステップ

生成が完了したら以下の手順でユーザーと対話してください：

1. **成果物の案内**: 「アーキテクチャ図が準備できました。現在の構成図を確認してください。図をプレビューするには `output/[プロジェクトコード]/diagrams/architecture.md` をクリックして開くか、同ディレクトリ内の `.png` 画像を参照してください。」と伝えます。
2. **追加要件の確認**: 「この構成図を確認して、追加したい機能や変更点はありますか？自然言語で言っていただければ、すぐに図とコードに反映します。」と問いかけます。（※Terraformの知識は不要であることを強調します）
3. **イテレーション**: ユーザーからのフィードバックに基づき、コードと図を更新します。
4. **完了案内とデプロイ準備**: ユーザーが満足したら、次のステップを案内します：「設計が完了しました。実際にAWS上にリソースを作成するには、以下の準備が必要です：

   **前提条件（重要）:**
   1. **AWS CLI のインストール**: お使いのPCに `aws` コマンドがインストールされていること。
   2. **認証設定**: ターミナルで `aws configure` を実行し、適切な IAM ユーザーの `Access Key ID` と `Secret Access Key` が設定されていること。
   3. **権限**: 使用する IAM ユーザーに、Terraform がリソースを作成するための十分な権限（AdministratorAccess など）が付与されていること。

   **実行コマンド**:
   ```bash
   cd output/[プロジェクトコード]/terraform
   terraform init    # 初期化
   terraform plan    # 実行プランの確認
   terraform apply   # 実際のリソース作成（実行時に 'yes' と入力）
   ```
   もし認証設定や AWS の準備に不安がある場合は、私に聞いてください。」と伝えて終了します。
