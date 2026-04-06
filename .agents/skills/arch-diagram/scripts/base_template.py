# base_template.py
# このテンプレートは、arch-diagram スキルのコード層の基本リファレンススケルトンとして使用されます。
# AI が具体的な図表を生成するたびに、このスケルトンを参照してビジネス側のコードを補完することができます。

from diagrams import Diagram, Cluster, Edge
# 一般的なクラウドプロバイダーノードのインポート例 (実際のインポートは Terraform コードに基づいて判断します)
from diagrams.aws.security import Cognito, WAF, KMS
from diagrams.aws.network import APIGateway, VPC, PrivateSubnet, NATGateway, InternetGateway, PublicSubnet
from diagrams.aws.compute import Lambda, EC2, ECS
from diagrams.aws.database import Aurora, RDS, DynamodbTable
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Client
from diagrams.onprem.auth import Oauth2Proxy

DEF_GRAPH_ATTR = {
    "fontsize": "12",
    "bgcolor": "transparent"
}

def create_base_diagram(project_name: str, app_name: str, output_path: str):
    """
    標準的で美しい初期 Diagram 構造を提供します。
    実際の使用では、AI は同様のメソッドを呼び出し、with コードブロック内にノードの関係を入力できます。
    """
    # 作成された diagram をコンテキストに返す
    return Diagram(
        name=f"[{project_name}] {app_name} Architecture",
        show=False,
        filename=output_path,
        graph_attr=DEF_GRAPH_ATTR,
        direction="TB" # 上から下へのレイアウト
    )

# 使用例 (各クラウドアーキテクチャは固有であるため、ノード間のリンクは AI によって動的に書き換えられる必要があります):
"""
if __name__ == "__main__":
    project_id = "demo-project"
    out_path = f"../../../../output/{project_id}/diagrams/architecture"
    
    with create_base_diagram(project_id, "Application System", out_path):
        client = Client("Users")
        with Cluster("AWS Cloud"):
            with Cluster("VPC"):
                api = APIGateway("API Gateway")
                client >> Edge(label="HTTPS") >> api
                # 新しいビジネス図要素の配線を追加 ...
"""
