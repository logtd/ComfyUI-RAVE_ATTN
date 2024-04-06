from ..utils.rave_attention import get_rave_attention


default_attn = {
    'inputs': [True] * 10,
    'input_idxs': list(range(10)),
    'middle_0': True,
    'outputs': [True] * 12,
    'output_idxs': list(range(12))
}


class ApplyRaveAttentionNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "model": ("MODEL",),
                    "grid_size": ("INT", {"default": 3, "min": 1, "max": 10}),
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                },
                "optional": {
                    "attn_override": ("ATTN_OVERRIDE",)
                }
                }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "apply"

    CATEGORY = "attention"

    def apply(self, model, grid_size, seed, attn_override=default_attn):
        model = model.clone()

        inputs = attn_override['inputs']
        input_idxs = attn_override['input_idxs']
        middle_0 = attn_override['middle_0']
        outputs = attn_override['outputs']
        output_idxs = attn_override['output_idxs']

        attn = get_rave_attention(grid_size=grid_size, seed=seed)
        for idx, enabled in zip(input_idxs, inputs):
            if enabled:
                model.set_model_patch_replace(attn, 'attn1', 'input', idx)

        if middle_0:
            model.set_model_patch_replace(attn, 'attn1', 'middle', 0)

        for idx, enabled in zip(output_idxs, outputs):
            if enabled:
                model.set_model_patch_replace(attn, 'attn1', 'output', idx)

        return (model, )
