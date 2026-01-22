from __future__ import annotations

import pandas as pd
from pathlib import Path


def gerar_mensagem(nome: str) -> str:
    """Gera uma mensagem simples e personalizada."""
    return f"Olá {nome}, temos uma oferta especial disponível para você!"


def main() -> None:
    # Paths
    base_dir = Path(__file__).parent
    input_path = base_dir / "data" / "input_users.csv"
    output_path = base_dir / "data" / "output_messages.csv"

    # -------- Extract --------
    if not input_path.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {input_path}\n"
            "Crie o arquivo data/input_users.csv com as colunas: nome,conta,cartao."
        )

    df = pd.read_csv(input_path)

    # Validação básica
    colunas_obrigatorias = {"nome", "conta", "cartao"}
    if not colunas_obrigatorias.issubset(df.columns):
        raise ValueError(
            f"O CSV precisa conter as colunas: {sorted(colunas_obrigatorias)}. "
            f"Colunas encontradas: {list(df.columns)}"
        )

    # -------- Transform --------
    df["mensagem"] = df["nome"].astype(str).apply(gerar_mensagem)

    # Mantém somente o necessário na saída (opcional)
    df_saida = df[["nome", "mensagem"]].copy()

    # -------- Load --------
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_saida.to_csv(output_path, index=False, encoding="utf-8")

    print("✅ ETL concluído com sucesso!")
    print(f"📥 Entrada: {input_path}")
    print(f"📤 Saída:   {output_path}")
    print("\nPrévia do resultado:")
    print(df_saida.head())


if __name__ == "__main__":
    main()
