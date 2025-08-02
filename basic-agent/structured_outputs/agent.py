from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


#--- Define output Schema --

class EmailContent(BaseModel):
  subject: str = Field(
    description="The subject line of the email. Should be concise and consisten"
  )
  body: str = Field (
    description="The main content of the email. Should be well formatted and proper greeting and paragraphs, and signature"
  )

root_agent = LlmAgent(
    name="structure_outputs",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Email Agent",
    instruction="""
    You are an Email Generation Assistant.
    Your task is to generate a professional email based on the user's request.
    GUIDELINES:
    - Create an appropriate subject line (concise and relevant)
    - Write well-structured email body with:
        * Professional greeting
        * clear and concise main content
        * appropriate closing
        * your name as the signature
    - Suggest relevant attachments if applicable (empty list if needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching the format below:
    {
      "subject": "Subject line here",
      "body: "Email body here with proper paragraphs and formatting"
    }
     
    DO NOT include any explanations or additional text outside the json response

    """,
    output_key="email",
    output_schema=EmailContent,
)