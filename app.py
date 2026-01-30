# -*- coding: utf-8 -*-
"""BERT base uncased Fill-Mask WebUI（前端展示，不加载模型）"""
import gradio as gr

MASK_TOKEN = "[MASK]"


def run_fill_mask(text: str):
    """遮罩填充占位：仅展示界面与结果区域，不执行模型推理。"""
    if not (text or "").strip():
        return "请在输入框中输入包含 [MASK] 的英文句子，例如：Paris is the [MASK] of France."
    if MASK_TOKEN not in text:
        return "输入中需包含 [MASK] 占位符。示例：The goal of life is [MASK]."
    lines = [
        "【演示模式】未加载模型，以下为示例输出格式：\n",
        "输入句子：" + text.strip(),
        "",
        "Top-5 候选词（加载模型后将显示真实分数与 token）：",
        "  1. -- (score: --)",
        "  2. -- (score: --)",
        "  3. -- (score: --)",
        "  4. -- (score: --)",
        "  5. -- (score: --)",
    ]
    return "\n".join(lines)


with gr.Blocks(title="BERT base uncased Fill-Mask WebUI") as demo:
    gr.Markdown(
        "# BERT base uncased Fill-Mask WebUI\n\n"
        "基于 BERT 的英文遮罩语言模型可视化界面。"
        "支持输入含 [MASK] 的句子并查看预测候选（演示模式不加载模型）。"
    )
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="输入句子（需包含 [MASK]）",
                placeholder="例如：Paris is the [MASK] of France.",
                lines=3,
            )
            run_btn = gr.Button("填充预测", variant="primary")
        with gr.Column(scale=1):
            output_text = gr.Textbox(label="预测结果", lines=14)
    run_btn.click(
        fn=run_fill_mask,
        inputs=[input_text],
        outputs=[output_text],
    )
    gr.Markdown(
        "---\n**模型说明**：本界面用于加载 BERT base uncased（Fill-Mask）进行遮罩词预测与结果可视化。"
        "当前为演示模式，不加载真实权重。"
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7864, share=False)
