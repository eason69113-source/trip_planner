from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from agent.env_utils import *
from langchain.chat_models import init_chat_model
from zai import ZhipuAiClient

llm = ChatOpenAI(model='deepseek-r1',
                 temperature=0.5,
                 api_key=DASHSCOPE_API_KEY,
                 base_url=DASHSCOPE_API_URL
                 )

llm1 = ChatDeepSeek(model='deepseek-r1',
                    temperature=0.5,
                    api_key=DASHSCOPE_API_KEY,
                    api_base=DASHSCOPE_API_URL
                    )

llm2 = init_chat_model(model='deepseek-chat',
                       temperature=0.5,
                       model_provider='deepseek', #或者使用openai 使用openai等于方法1，使用deepseek等于方法2
                       api_key=DEEPSEEK_API_KEY,
                       base_url=DEEPSEEK_API_URL
                       )

llm3 = ChatOpenAI(model='qwen-max',
                  temperature=0.5,
                  extra_body={"enable_search": True},
                  api_key=DASHSCOPE_API_KEY,
                  base_url=DASHSCOPE_API_URL
)

llm4 = ZhipuAiClient(api_key=ZHIPUAI_API_KEY)

# llm4 = init_chat_model(model='gml-4.5',
#                        temperature=0.5,
#                        model_provider='openai',
#                        api_key=ZHIPUAI_API_KEY,
#                        base_url=ZHIPUAI_API_URL
#                        )
