from qr_tools import decode_image, encode_image
import gradio as gr

with gr.Blocks(title="QR Maker") as ui:
    with gr.Row():
        qr_code_image = gr.Image(label="QR Code", value="b44eb5c7-8bfe-4ffe-9c05-8d5a2247c42d.png", type="numpy")
        with gr.Column():
            qr_value = gr.TextArea(label="Value")
            with gr.Row():
                get_qr_code_value_btn = gr.Button("Get Value")
                set_qr_code_value_btn = gr.Button("Set Value")
    
    get_qr_code_value_btn.click(decode_image, inputs=[qr_code_image], outputs=[qr_value])
    set_qr_code_value_btn.click(encode_image, inputs=[qr_value], outputs=[qr_code_image])

ui.launch()