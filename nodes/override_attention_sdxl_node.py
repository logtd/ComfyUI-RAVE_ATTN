
class AttentionOverrideSDXLNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "input_4": ("BOOLEAN", {"default": True}),
                    "input_5": ("BOOLEAN", {"default": True}),
                    "input_7": ("BOOLEAN", {"default": True}),
                    "input_8": ("BOOLEAN", {"default": True}),
                    "middle_0": ("BOOLEAN", {"default": True}),
                    "output_1": ("BOOLEAN", {"default": True}),
                    "output_2": ("BOOLEAN", {"default": True}),
                    "output_3": ("BOOLEAN", {"default": True}),
                    "output_4": ("BOOLEAN", {"default": True}),
                    "output_5": ("BOOLEAN", {"default": True}),
                }
                }

    RETURN_TYPES = ("ATTN_OVERRIDE",)
    FUNCTION = "apply"

    CATEGORY = "attention"

    def apply(self,
              input_4, input_5, input_7, input_8,
              middle_0,
              output_1, output_2, output_3, output_4, output_5):
        inputs = [input_4, input_5, input_7, input_8]
        input_idxs = [4, 5, 7, 8]
        outputs = [output_1, output_2, output_3, output_4, output_5]
        output_idxs = [1, 2, 3, 4, 5]

        attn = {
            'inputs': inputs,
            'input_idxs': input_idxs,
            'outputs': outputs,
            'output_idxs': output_idxs,
            'middle_0': middle_0
        }

        return (attn, )
