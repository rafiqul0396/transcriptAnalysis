
def few_short_example():
    example_few_short = {
    
"examples": """


Please format the tasks as follows and avoid repetition:

For Two-way Conversation:
## output

   [
      {
         "action_item": {
            "actor": "Customer Care Executive",
            "action": "Forward the customer's information to the corporate office for further investigation."
         }
      },
      {
         "action_item": {
            "actor": "Caller",
            "action": "Wait for an email regarding the refund within two to four business days."
         }
      },
      {
         "action_item": {
            "actor": "Customer Care Executive",
            "action": "Ensure the details of the call are forwarded to the corporate office for further investigation."
         }
      }
   ]

If It's a One-way Conversation:
## input:
Hi, I'm sorry I missed you. This is Roxanne calling from MBNA Canada Bank. I'm calling to let you know about our new Platinum Plus MasterCard with no annual fee 
and an introductory interest rate of 5.9%. Please give me a call at 1-800-416-8000 to discuss this great offer further and remember to mention your priority code AKP5. 
That number again is 1-800-416-8000. And your priority code is AKP5. I look forward to hearing from you soon.

## output:
   [
  {
    "action_item": {
      "actor": "Service Representative",
      "action": "Call Roxanne back at 1-800-416-8000 to discuss the new Platinum Plus MasterCard offer with no annual fee and an introductory interest rate of 5.9%. Mention priority code AKP5."
    }
  }
]
"""
   
    }
    return example_few_short