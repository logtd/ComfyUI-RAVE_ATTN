
class AttentionOverrideSD15Node:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "input_1": ("BOOLEAN", {"default": True}),
                    "input_2": ("BOOLEAN", {"default": True}),
                    "input_4": ("BOOLEAN", {"default": True}),
                    "input_5": ("BOOLEAN", {"default": True}),
                    "input_7": ("BOOLEAN", {"default": True}),
                    "input_8": ("BOOLEAN", {"default": True}),
                    "middle_0": ("BOOLEAN", {"default": True}),
                    "output_3": ("BOOLEAN", {"default": True}),
                    "output_4": ("BOOLEAN", {"default": True}),
                    "output_5": ("BOOLEAN", {"default": True}),
                    "output_6": ("BOOLEAN", {"default": True}),
                    "output_7": ("BOOLEAN", {"default": True}),
                    "output_8": ("BOOLEAN", {"default": True}),
                    "output_9": ("BOOLEAN", {"default": True}),
                    "output_10": ("BOOLEAN", {"default": True}),
                    "output_11": ("BOOLEAN", {"default": True}),
                }
                }

    RETURN_TYPES = ("ATTN_OVERRIDE",)
    FUNCTION = "apply"

    CATEGORY = "attention"

    def apply(self,
              input_1, input_2, input_4, input_5, input_7, input_8,
              middle_0,
              output_3, output_4, output_5, output_6, output_7, output_8, output_9, output_10, output_11):
        inputs = [input_1, input_2, input_4, input_5, input_7, input_8]
        input_idxs = [1, 2, 4, 5, 7, 8]
        outputs = [output_3, output_4, output_5, output_6,
                   output_7, output_8, output_9, output_10, output_11]
        output_idxs = [3, 4, 5, 6, 7, 8, 9, 10, 11]

        attn = {
            'inputs': inputs,
            'input_idxs': input_idxs,
            'outputs': outputs,
            'output_idxs': output_idxs,
            'middle_0': middle_0
        }

        return (attn, )
