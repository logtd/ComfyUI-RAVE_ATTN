from .nodes.apply_rave_attention_node import ApplyRaveAttentionNode
from .nodes.override_attention_sd15_node import AttentionOverrideSD15Node
from .nodes.override_attention_sdxl_node import AttentionOverrideSDXLNode


NODE_CLASS_MAPPINGS = {
    "ApplyRaveAttentionNode": ApplyRaveAttentionNode,
    "AttentionOverrideSD15Node": AttentionOverrideSD15Node,
    "AttentionOverrideSDXLNode": AttentionOverrideSDXLNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ApplyRaveAttentionNode": "Apply Rave Attention",
    "AttentionOverrideSD15Node": "Attention Override (SD1.5)",
    "AttentionOverrideSDXLNode": "Attention Override (SDXL)",
}
