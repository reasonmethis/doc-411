from langchain.prompts.prompt import PromptTemplate

# condense_question_template = """Given the following Conversation and Follow Up Query, add context to Query so that it can be understood without needing to read the whole conversation: include necessary details from the conversation to make Query completely standalone. For example, if the Query is "and then?" then Standalone Query could be "In the conversation where you, Assistant, just summarized the first Harry Potter book, you are asked: and then?"

# Conversation:
# {chat_history}
# Follow Up Query: {question}
# Standalone Query:"""
condense_question_template = """Given the following chat history (between Human and you, the Assistant) add context to the last Query from Human so that it can be understood without needing to read the whole conversation: include necessary details from the conversation to make Query completely standalone:
1. First put the original Query as is or very slightly modified (e.g. replacing "she" with who this refers to) 
2. Then, add "[For context: <condensed summary to yourself of the relevant parts of the chat history: if Human asks a question and the answer is clear from the chat history, include it in the summary>]"

Examples of possible Standalone Queries:
- "And then? [For context: Human wrote this in response to your summary of the Big Bang. The general conversation was about the history of the universe.]"
- "How do you know this? [For context: you just summarized relevant parts of your knowledge base answering Human's question about installing Langchain. Briefly, you explained that they need to run "pip install langchain" and likely other libraries like openai, tiktoken, etc.]"
- "hm [For context: Human asked you to write a poem about Washington and you wrote one.]"
- "What was my first message to you? [For context: Human's first message in our chat history was <exact first message from Human in chat history, verbatim>.]

Chat History:
{chat_history}
Last Query from Human: {question}
Please modify the preceding Query as instructed: """
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(condense_question_template)

qa_system_template = """You are a helpful Assistant AI. In addition to your usual skills and knowledge you've also been equipped with your own special knowledge base. You have retrieved the most relevant parts of your knowledge base you could find to respond to the user's message, although some or even all of these parts may still be irrelevant.

Please respond to the user's message just as you normally would in a conversation, but feel free to draw on the relevant portions of your knowledge base you retrieved, as well as your other skills. One thing is - if the user clearly needs some information that you don't know or you don't understand what the user wants, it's ok to admit it or ask for clarification. First you will see the relevant parts of your knowledge base you retrieved, followed by the human's message. The Human's message may or may not also include the system's summary of your previous conversation with Human, for context.

{context}
----------------
Human: {question}
Your Response: """
QA_PROMPT_CHAT = PromptTemplate(
    template=qa_system_template, input_variables=["context", "question"]
)
