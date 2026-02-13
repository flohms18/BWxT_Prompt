from dotenv import load_dotenv
load_dotenv()

from leo_prompt_optimizer import (
    optimize_prompt,
    set_groq_api_key,
    set_openai_api_key,
    set_client
)

# Required: set backend provider
set_client(provider="groq")

# Prompt example
optimized = optimize_prompt(
    prompt_draft="Write potc 6 with Davy Jones",
    user_input_example="[POTENTIAL INPUT EXAMPLE]",
    llm_output_example="[POTENTIAL OUTPUT EXAMPLE]", 
    top_instruction="[POTENTIAL EXTRA CONTEXT, SPECIFIC INSTRUCTION TO FOCUS ON FOR THE LLM]", # Optional
    model="llama3-70b",            # Optional: model choie based on your provider(e.g. "gpt-4", "llama3-70b", etc.)
)

print(optimized)