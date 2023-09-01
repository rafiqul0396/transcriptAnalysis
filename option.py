
def Answer_outPut():
    summary_output_options = {
   
    'Sentiment': """
    - only give me the sentiment of the conversation no need of action item.
     - Sentiment: Your task is to classify its sentiment as positive, neutral, or negative.
     - Reason: Your task is to classify the reason for the sentiment.
""",
    'extraction':"""
    - your task is to find out the title  of the conversation between the customer and sale person.
    """,

    'Action Items' : """
    - find out the action item in the input section and return the action item

    Please format the tasks as follows and avoid repetition:

    - For two-way Conversation:

      {
         "action_item": {
            "actor": "name of the Actor",
            "action": "action item"
         }
      },
      {
         "action_item": {
            "actor": "name of the actor",
            "action": "action item"
         }
      },
      {
         "action_item": {
            "actor": "name of the Actor",
            "action": "action item"
         }
      }
   ]
   so on
    """
    }
    return  summary_output_options