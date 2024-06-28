import logging
from pathlib import Path

from mcgen.context import Context
from mcgen.utils import summarize_registry

LOG = logging.getLogger(__name__)


def process(ctx: Context, **options):
    """Create a summary of each vanilla registry."""

    data_path = Path("data/minecraft")
    LOG.info(f"Summarizing data at: {data_path}")

    # TODO Scan for registries automatically. #enhance

    data_summary = {}

    # advancements
    data_summary["advancement"] = summarize_registry(ctx, data_path / "advancement")

    # loot tables
    data_summary["loot_table"] = summarize_registry(ctx, data_path / "loot_table")

    # recipes
    data_summary["recipe"] = summarize_registry(ctx, data_path / "recipe")

    # tags
    data_summary["tags"] = {}
    data_summary["tags"]["block"] = summarize_registry(ctx, data_path / "tags/block")
    data_summary["tags"]["entity_type"] = summarize_registry(
        ctx, data_path / "tags/entity_type"
    )
    data_summary["tags"]["fluid"] = summarize_registry(ctx, data_path / "tags/fluid")
    data_summary["tags"]["game_event"] = summarize_registry(
        ctx, data_path / "tags/game_event"
    )
    data_summary["tags"]["item"] = summarize_registry(ctx, data_path / "tags/item")

    ctx.write_json_node(data_summary, data_path)
    ctx.write_min_json_node(data_summary, data_path)
