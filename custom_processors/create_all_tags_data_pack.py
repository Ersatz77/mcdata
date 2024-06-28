import json
import logging
from pathlib import Path

from mcgen.context import Context

LOG = logging.getLogger(__name__)

SUPPORTED_REGISTRIES = {
    "minecraft:block": "block",
    "minecraft:entity_type": "entity_type",
    "minecraft:fluid": "fluid",
    "minecraft:game_event": "game_event",
    "minecraft:item": "item",
}


def process(ctx: Context, **options):
    """Create a data pack with tags containing all values of various registries."""

    packs_reldir = Path("datapacks")
    pack_reldir = packs_reldir / "mcdata.all_tags"
    LOG.info(f"Creating 'all tags' data pack at: {pack_reldir}")

    # load registries.json
    registries_inpath = ctx.input_dir / "reports/registries.json"
    with open(registries_inpath) as fp:
        registries_data = json.load(fp)

    # create a new tag for each registry that supports tags
    tags_reldir = pack_reldir / "data/mcdata/tags"
    for reg_name, tag_type in SUPPORTED_REGISTRIES.items():
        registry = registries_data[reg_name]
        reg_entries = registry["entries"]
        tag_file_relpath = tags_reldir / tag_type / "all.json"
        LOG.debug(
            f"Writing tag for registry {reg_name} with {len(reg_entries)} values"
            + " at: {tag_file_name}"
        )
        tag_values = sorted(list(reg_entries.keys()))
        tag_content = {"values": tag_values}
        ctx.write_json_file(tag_content, tag_file_relpath)

    # create a pack.mcmeta
    pack_mcmeta_relpath = pack_reldir / "pack.mcmeta"
    pack_mcmeta_content = {
        "path": {
            # TODO Dynamic pack_format based on extracted jar files? #enhance
            "pack_format": 48,
            "description": "mcdata: all tags",
        }
    }
    ctx.write_json_file(pack_mcmeta_content, pack_mcmeta_relpath)
