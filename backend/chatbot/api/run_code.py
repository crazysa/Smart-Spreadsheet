from langchain.agents.agent_types import AgentType
# from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
# import pandas as pd
import os
import pandas as pd
# from langchain_openai import OpenAI
import re
from langchain_openai import ChatOpenAI
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework.response import Response

os.environ['OPENAI_API_KEY'] = 'sk-uaDHPQUUz3C06hMLBnKQT3BlbkFJ8yzbmaLa8ffuMTOBKQE'

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]

def sort_wrt_numbers(list):
    list.sort(key=natural_keys)
    return list


#http://127.0.0.1:8000/api/?format=json
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def run( prompt = "What is the Total Cash and Cash Equivalent of Oct. AND Nov. of 2023 combined?", local_folder_path = '/home/shubham/Desktop/Smart-Spreadsheet/output_tables/') -> str:
    return Response(
            status=status.HTTP_200_OK,
            data="Calibration Failed. Please check your input data and make sure the frames are of good quality before trying again")
    all_csv = []

    for file in sort_wrt_numbers(os.listdir(local_folder_path)):
        print(os.path.join(local_folder_path, file))
        pandas_df = pd.read_csv(os.path.join(local_folder_path, file))
        pandas_df.dropna(how='all', axis=1, inplace=True) 
        all_csv.append(pandas_df)
    # df = pd.read_csv(local_file_path)

    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        all_csv,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    # response = agent.run(prompt)
    response = agent.invoke(prompt)
    print(response)

    return response

# with strong enough computer and enough data we can fine tune any open source model to reduce price
# def run_hugging_face( prompt: str, local_folder_path: str) -> str:
#     from datasets import load_dataset
#     from transformers import AutoTokenizer, AutoModelForCausalLM
#     from peft import PeftModel


#     base_model = AutoModelForCausalLM.from_pretrained(
#         'meta-llama/Llama-2-7b-chat-hf',
#         trust_remote_code=True,
#         device_map="auto",
#         torch_dtype=torch.float16,   # optional if you have enough VRAM
#     )
#     tokenizer = AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-chat-hf')

#     model = PeftModel.from_pretrained(base_model, 'FinGPT/fingpt-forecaster_dow30_llama2-7b_lora')
#     model = model.eval()

#     return response

# output_folder = 
# api_key = "sk-uaDHPQUUz3C06hMLBnKQT3BlbkFJ8yzbmaLa8ffuMTOBKQE"
# prompt = 
# run(api_key,prompt,  output_folder)