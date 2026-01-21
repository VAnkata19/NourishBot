from dotenv import load_dotenv
from modules import grocery_offers
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os

def get_best_offers(information):

    offers_template = """
    You are receiving scraped data on current offers from a grocery store.
    The data is a list of tuples where each tuple contains the title, description,
    and deal information of the grocery item.

    Look at the information below and do the following:
    1. Find the best offers by comparing the original price and the discount price.
    2. Do not repeat items.
    3. Only return items that can be used to make meals. Don't return snacks, sweets or non-food items.

    For Example:
        Title: Chicken Breast
        Description: Fresh chicken breast, 1kg
        Deal: Was 10.00 USD, now 7.00 USD

    Information:
    {information}
    """

    meals_template = """
    You receive grocery items below:
    {items}

    Your task is to generate 3 easy recipes using these items.

    Format your response as an email body.
    """

    shopping_template = """
    You receive grocery items:
    {items}

    And meal recipes:
    {meals}

    Your task is to create a consolidated shopping list needed to prepare the meals. Dont include any duplicates.

    Example:
    [Meal Name]
    - Ingredient 1
    - Ingredient 2
    - Ingredient 3
    
    

    Format your response as an email body.
    """

    offers_prompt = PromptTemplate(
        input_variables=["information"],
        template=offers_template
    )

    meals_prompt = PromptTemplate(
        input_variables=["items"],
        template=meals_template
    )

    shopping_prompt = PromptTemplate(
        input_variables=["items", "meals"],
        template=shopping_template
    )

    llm = ChatOpenAI(model="gpt-4-turbo", temperature=1)

    offers_response = llm.invoke(
        offers_prompt.format(information=information)
    )

    meals_response = llm.invoke(
        meals_prompt.format(items=offers_response.content)
    )

    shopping_response = llm.invoke(
        shopping_prompt.format(
            items=offers_response.content,
            meals=meals_response.content
        )
    )

    return (
        offers_response.content,
        meals_response.content,
        shopping_response.content
    )
