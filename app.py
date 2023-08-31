
import openai
import streamlit as st
import pandas as pd
from io import StringIO
import time
from datetime import datetime
import  threading
from option import Answer_outPut
import streamlit as st


from io import BytesIO
import os
# To split our transcript into pieces
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Our chat model. We'll use the default which is gpt-3.5-turbo
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from base_prompt import *
from chat_prompt_map import *

# Load .env file

# Import load_dotenv
from dotenv import load_dotenv

load_dotenv()

from example import few_short_example
def main():
    st.title("Transcript Analysis")

    uploaded_file = st.file_uploader("Choose a text file")


    option = st.selectbox(
    'Select option from dropdown?',
    ('Sentiment','Action Items'))
    text=""
    if st.button("Show Results"):
        if uploaded_file is not None:
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                #st.write(bytes_data)

    # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                #st.write(stringio)

    # To read file as string:
                string_data = stringio.read()
                #st.write(string_data)
            
                st.markdown('**Transcript:**.')
                st.text_area(label="Text:", value=string_data, height=250)
                # st.write(result["text"])
            
            

                content = string_data
                
                text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=2000, chunk_overlap=250)
                texts = text_splitter.create_documents([content])
                llm = ChatOpenAI(model="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"),temperature=0)
                chat_prompt_map1=chat_promptMap()
                chat_prompt_combine1=chat_prompt_combine()
                chain = load_summarize_chain(llm,
                                chain_type="map_reduce",
                                map_prompt=chat_prompt_map1,
                                combine_prompt=chat_prompt_combine1,
                                verbose=True
                                )
                
                summary_output_options = Answer_outPut()
                user_selection=option
                print(user_selection)

                
                # if option == 'action_result':
                #     user_selection1=summary_output_options['action_item']
                
                #     output = chain.run({
                #                         "input_documents": texts,
                #                         "output_format" : summary_output_options[user_selection1]
                #                     })
                #     texts=output
                ex=few_short_example()
                ex=ex['examples']
                output = chain.run({
                                    "input_documents": texts,
                                        "output_format" : summary_output_options[user_selection],
                                        "texts": texts

                                    })
                st.markdown('**Answer:**.')
                st.text_area(label="Results", value=output, height=350)
    
    
       

        
        
    

if __name__ == "__main__": 
    main()