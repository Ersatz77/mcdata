import logging
from pathlib import Path

from mcgen.context import Context
from mcgen.utils import summarize_registry

LOG = logging.getLogger(__name__)


def process(ctx: Context, **options):
    """Create a summary of worldgen reports."""

    worldgen_path = Path("data/minecraft/worldgen")
    LOG.info(f"Summarizing worldgen at: {worldgen_path}")

    # TODO Scan for registries automatically. #enhance
    
    worldgen_summary = {}

    # biome
    worldgen_summary["biome"] = summarize_registry(
        ctx, worldgen_path / "biome"
    )

    # configured_carver
    worldgen_summary["configured_carver"] = summarize_registry(
        ctx, worldgen_path / "configured_carver"
    )

    # configured_feature
    worldgen_summary["configured_feature"] = summarize_registry(
        ctx, worldgen_path / "configured_feature"
    )

    # density_function
    worldgen_summary["density_function"] = summarize_registry(
        ctx, worldgen_path / "density_function"
    )

    # flat_level_generator_preset
    worldgen_summary["flat_level_generator_preset"] = summarize_registry(
        ctx, worldgen_path / "flat_level_generator_preset"
    )

    # noise
    worldgen_summary["noise"] = summarize_registry(
        ctx, worldgen_path / "noise"
    )

    # noise_settings
    worldgen_summary["noise_settings"] = summarize_registry(
        ctx, worldgen_path / "noise_settings"
    )

    # placed_feature
    worldgen_summary["placed_feature"] = summarize_registry(
        ctx, worldgen_path / "placed_feature"
    )

    # processor_list
    worldgen_summary["processor_list"] = summarize_registry(
        ctx, worldgen_path / "processor_list"
    )

    # structure
    worldgen_summary["structure"] = summarize_registry(
        ctx, worldgen_path / "structure"
    )

    # structure_set
    worldgen_summary["structure_set"] = summarize_registry(
        ctx, worldgen_path / "structure_set"
    )

    # template_pool
    worldgen_summary["template_pool"] = summarize_registry(
        ctx, worldgen_path / "template_pool"
    )

    # world_preset
    worldgen_summary["world_preset"] = summarize_registry(
        ctx, worldgen_path / "world_preset"
    )

    ctx.write_json_node(worldgen_summary, worldgen_path)
    ctx.write_min_json_node(worldgen_summary, worldgen_path)
