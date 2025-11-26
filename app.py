import gradio as gr


def build_app(description):
    return f"You entered: {description}\n\nThis prototype will eventually build an AI app for you using your description!"


iface = gr.Interface(
    fn=build_app,
    inputs="text",
    outputs="text",
    title="AI App Builder Prototype",
    description="Enter your app idea and receive a placeholder response. Hosted on Hugging Face Spaces for free."
)


if __name__ == "__main__":
    iface.launch()
