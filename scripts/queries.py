import polars as pl
from typing import List
import numpy as np

def scope_param(df: pl.LazyFrame, column: str="rpm_mapped") -> pl.LazyFrame:
    """
    takes one of the features of the genes and creates a new dataframe with the feature and target class

    Params:
        df (pl.DataFrame): TCGA-miRNA dataset
        column (str): property to built the dataframe around

    Returns:
        pl.DataFrame: polars DataFrame with target, unique case and value corresponding to each gene
    """
    scoped_df = df.pivot(index="uuid", columns="miRNA_ID", values=column).sort(by="uuid")
    alter = df.select(pl.col("uuid", "project")).sort(by="uuid")
    return scoped_df.join_asof(alter, on="uuid")

ln_norm = lambda df: df.with_columns([
        (pl.exclude(['project', 'uuid']).log()).cast(pl.Float32).round(3).over(pl.col("project"))
    ])


def prune_from_norm(df: pl.LazyFrame, exclude: List[str]=["uuid", "project"]) -> pl.LazyFrame:
    """
    removes genes from dataframe with inf values after log normalization.
    This indicates the miRNA having no expression.

    Params:
        df (pl.DataFrame): TCGA-miRNA dataset
        exclude (List[str]): columns to exclude from dataframe

    Returns:
        pl.DataFrame: polars DataFrame with target, unique case and value corresponding to each gene
    """
    alter = df.select(pl.exclude(*exclude))
    alter_vals = alter.collect(streaming=True).to_numpy()
    median = np.median(alter_vals, axis=0)
    drop_idcs = np.where(np.isinf(median))[0]
    drop_idcs = np.array(alter.columns)[drop_idcs]
    return df.drop(drop_idcs)

fill_inf = lambda df: df.with_columns(
        pl
            .when(pl.exclude("uuid", "project").is_infinite())
            .then(pl.lit(0))
            .otherwise(pl.exclude("uuid", "project"))
            .name.keep()
    )
