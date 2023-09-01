# Prompt templates for dynamic values
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate, # I included this one so you know you'll have it but we won't be using it
    HumanMessagePromptTemplate
)

# To create our chat messages
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
def chat_prompt_combine():
    template="""
You are a helpful assistant that helps  find action item   at company, analyze information from a service call step by step .
Your goal is to create action item from the perspective of Action Item Representative  that will highlight key points  of the conversation over the call.
Do not respond with anything outside of the call transcript. If you don't know, say, "I don't know"
Do not repeat Action item Representative  name in your output.



#input
Hello, sorry I missed you. I'm calling on behalf of Alexa McDonough and the federal NDP. 
Election fever is running high with a widely expected federal election call this weekend. 
I wanted to invite you to come out and hear our leader, Alexa McDonough, at our Metro campaign kickoff this Friday, October 20th, 7.30 p.m. at the United Steelworkers Hall at 25 Cecil Street in downtown Toronto. 
Alexa will be the guest speaker at the Trinity Spadina nomination meeting. We want to give her a really great Toronto welcome as we head into campaign 2000 this weekend. If you can make it out that would be great. 
Bring a friend and please pass this along. Alexa is going to be speaking shortly after the meeting begins so please come early. Again, NDP federal leader Alexa McDonough will be here in town this Friday, October 20th,
 7.30 p.m. 25 Cecil Street and that's one block east of Spadina just south of College. Hope to see you there. If you would like more information please give our provincial headquarters a call at 591-8637. Thanks for your time. Bye now.

Question: what are the action items in the given input section?
Thought:The thought here is to analyze the content of the call and identify any key points or actions  item related to the political event invitation.
Action:Search[political event invitation]
Observation: The call is an invitation to an event featuring Alexa McDonough, the federal NDP leader, for their Metro campaign kickoff in Toronto on Friday, October 20th, at 7:30 p.m. The event will be held at the United Steelworkers Hall on 25 Cecil Street in downtown Toronto. The caller encourages people to attend the event, bring friends, and spread the word. They also provide contact information for more details and emphasize the importance of coming early to hear Alexa McDonough speak.
Action item:Finish[Follow up at 591-8637 for more information about the Metro campaign kickoff event with Alexa McDonough on Friday, October 20th at 7.30 p.m. at the United Steelworkers Hall at 25 Cecil Street in downtown Toronto.]

#input
Sorry I missed you. This is Miriam calling from Education Fund Services. 
We have a very important message for you. If you have children under the age of 9, you may qualify to receive up to $400 per year per child from Canada Education Savings Grant Program for your children's education. 
If you would like free information regarding this program, please call me back at 466-466-4666. I look forward to speaking with you. Thank you.
Questions: What are the action items in the given input section?
Thought: The thought here is to analyze the content of the call and identify any key points or actions related to the Education Fund Services message.
Action:Search[Education Fund Services message]
Observation: The call is from Miriam at Education Fund Services, informing the recipient that they may qualify to receive up to $400 per year per child from the Canada Education Savings Grant Program if they have children under the age of 9. The recipient is invited to call back for more information.
Action Item:Finish[Call Miriam back at 466-466-4666 to get free information about the Canada Education Savings Grant Program for children under the age of 9.]

#input
Hi, this is Jody Pierce of Infographics in Buckhead, and I'm sorry I missed you. Hey, 
hopefully this is good timing for you. I thought I'd give you a heads up that we offer, in addition to standard printing services, 
variable data, mailing services, and digital archiving. I'm always amazed that more people aren't aware that we offer this service at any rate. 
If that's something you'd be interested in, feel free to call me. This is Jody again at Infographics located here in Buckhead, and I can be reached at 404-888-8888. 
Thanks, and have a great day.

Question: what are the action item in the above input?
Thought: The thought here is to inform the recipient about the additional services offered by Infographics in Buckhead, which include variable data, mailing services, and digital archiving. The caller expresses surprise that more people aren't aware of these services.
Action: Search[Infographics] 
Observation: The call is from Jody Pierce of Infographics in Buckhead, offering additional services beyond standard printing, such as variable data, mailing services, and digital archiving. The recipient is encouraged to call Jody if they are interested in these services.
Action item:Finish[Follow up with Jody Pierce from Infographics in Buckhead regarding their additional services such as variable data, mailing services, and digital archiving]

#input
Hi, this is Arnie at Wagner, Lincoln, Mercury, Mazda in Fostoria. 
I need to talk to you about your car. Call me as soon as you can at 1-800-583-8888.
And, uh, by the way, I've got some good news.

Question:what are the action item in the given input?
Thought: The thought here is to convey that Arnie from Wagner, Lincoln, Mercury, Mazda in Fostoria is trying to reach the recipient regarding their car and has some good news.
Action: The action item is to call Arnie back at 1-800-583-8888 as soon as possible to discuss the matter regarding the car.
Observation: The call is from Arnie at the dealership, indicating the need for a conversation about the recipient's car and mentioning that there is some good news to share.
Action item:
#input
Hi, it's Kathy calling on behalf of CIBC. 
I just wanted to ensure you received our invitation to apply for the CIBC HPC Rewards Visa Card. 
This credit card comes with no annual fees of any kind. Plus, it's the only Visa card that gives you 15 HPC Rewards bonus points for every dollar on card purchases, 
which can be used to redeem for free merchandise and services offered by HPC Rewards. The current regular card interest rate is a competitive 19.5% per year.
If you're interested, call us at 1-888-517-4233 by March 17th and quote the special number 0001199. Hope to hear from you soon.

Question: what are the  action item in the given input?
Thought: The thought here is to inform the recipient about the CIBC HPC Rewards Visa Card, its benefits, and the offer to apply for it.
Action: The action item is for the recipient to call CIBC at 1-888-517-4233 by March 17th and quote the special number 0001199 if they are interested in applying for the CIBC HPC Rewards Visa Card.
Observation: The call is from Kathy on behalf of CIBC, promoting the CIBC HPC Rewards Visa Card, which comes with no annual fees and offers 15 HPC Rewards bonus points for every dollar on card purchases. The card has a competitive interest rate of 19.5% per year. The recipient is encouraged to call CIBC if they are interested in this offer.

Action items:Finish[Confirm if they received the invitation to apply for the CIBC HPC Rewards Visa Card,Provide information about the no annual fees, 15 HPC Rewards bonus points, and the regular card interest rate,Remind the customer to call before March 17th and quote the special number 0001199 if interested]


#:input
{texts}
return output in  the following format
{output_format}



"""
    system_message_prompt_combine = SystemMessagePromptTemplate.from_template(template)

    human_template="{text}" # Simply just pass the text as a human message
    human_message_prompt_combine = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt_combine = ChatPromptTemplate.from_messages(messages=[system_message_prompt_combine, human_message_prompt_combine])
    return chat_prompt_combine