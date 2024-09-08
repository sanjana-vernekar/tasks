def cricket_chatbot():
    print("Hello! I'm your Cricket Chatbot. Ask me anything about cricket!")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! What cricket information are you looking for?")
        elif "who won the world cup" in user_input:
            print("Chatbot: The winner of the most recent ICC Cricket World Cup is England (2019).")
        elif "who is the best batsman" in user_input:
            print("Chatbot: Opinions vary, but Sachin Tendulkar, Virat Kohli, and Steve Smith are often considered among the best.")
        elif "how many overs in a t20 match" in user_input:
            print("Chatbot: A T20 cricket match consists of 20 overs per side.")
        elif "who has the most runs in odi" in user_input:
            print("Chatbot: As of now, Sachin Tendulkar holds the record for the most runs in One Day Internationals (ODIs).")
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Enjoy your cricket!")
            break
        else:
            print("Chatbot: I'm not sure about that. Can you ask something else related to cricket?")

# Run the chatbot
cricket_chatbot()