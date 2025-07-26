import torch

import gradio as gr

from transformers import pipeline

#model_path=("../installation/models/models--sshleifer--distilbart-cnn-12-6/snapshots"
 #           "/a4f8f3ea906ed274767e9906dbaede7531d660ff")

#text_summary= pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
 #               torch_dtype=torch.bfloat16)
#text="Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman. He is known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion."
#print(text_summary(text));

def summary(inputs):
    outputs=text_summary(inputs)
    return outputs[0]['summary_text']
gr.close_all()

#demo=gr.Interface(fn=summary, inputs="text",outputs="text")
demo=gr.Interface(fn=summary,
                  inputs=[gr.Textbox(label="names os the summarise",lines=2)],
                  outputs=[gr.Textbox(label="summarized text",lines=2)],
                  title="@genai project1:Text summarizer",
                  description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT")
demo.launch()



