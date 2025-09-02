from responses import responses

def get_response(user_input: str) -> str:
    """
    Matches user input with predefined responses (rule-based).
    """
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return responses[key]

    # Default response
    return "🤔 Hmm… I’m not sure how to respond to that. Could you try asking me differently?"
