from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


llm= OpenAI(temperature=0.7,openai_api_key='')
def genreate_resurant_name_and_items(cuisine):
    prompt_template_name=PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a resturant for {cuisine} food. Suggest a fency name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key ='resturant_name')

    prompt_template_items=PromptTemplate(
    input_variables=['resturant_name'],
    template="Suggest some menu items for {resturant_name}. "
    )
    food_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')
    chain = SequentialChain(
    chains =[name_chain, food_items_chain],
    input_variables =['cuisine'],
    output_variables=['resturant_name' ,'menu_items'],
    )

    response=chain({'cuisine': cuisine})

    return response


if __name__=='__main__':
    print(genreate_resurant_name_and_items('Italian'))