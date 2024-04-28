import polars as pl


def scope_param(df: pl.DataFrame, col_name: str) -> pl.DataFrame:
    scoped = df.pivot(index="uuid", columns="miRNA_ID", values=col_name)
    return scoped.join(
            df.select(
                pl.col(["uuid", "project"]), on="uuid", how="left")
                )
