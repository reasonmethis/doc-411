from langchain.prompts.prompt import PromptTemplate

# condense_question_template = """Given the following Conversation and Follow Up Query, add context to Query so that it can be understood without needing to read the whole conversation: include necessary details from the conversation to make Query completely standalone. For example, if the Query is "and then?" then Standalone Query could be "In the conversation where you, Assistant, just summarized the first Harry Potter book, you are asked: and then?"

# Conversation:
# {chat_history}
# Follow Up Query: {question}
# Standalone Query:"""
condense_question_template = """Given the following conversation and a follow up Query, rephrase Query to be understood by itself. Incorporate only necessary details from Chat History to make Query completely (!) self-contained, standalone. Preserve the exact meaning and tone of Query - for example if Query is "wtf!" DO NOT (!) rephrase it to sound more intelligent and polite, instead preserve it to keep the exact meaning and simply add context to make it standalone, like this: "wtf! (For Context: the preceding query is in response to a summary of US Constitution)".

Chat History:
{chat_history}
Follow Up Query: {question}
Standalone Query: """
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(condense_question_template)

qa_system_template = """System: Use the following pieces of context to respond to the user's message. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
{context}
----------------
Human: {question}"""
QA_PROMPT_CHAT = PromptTemplate(
    template=qa_system_template, input_variables=["context", "question"]
)
