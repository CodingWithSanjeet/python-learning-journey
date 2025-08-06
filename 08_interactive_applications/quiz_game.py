questions = {
    # "Which Redux Toolkit function is used to create reducers and actions together?": "createSlice",
    # "Which hook lets you extract state from the Redux store in a component?": "useSelector",
    # "Which React hook is used to create local state in functional components?": "useState",
    # "Which hook is used to perform side effects in React components?": "useEffect",
    # "What is the return type of a functional component in React?": "JSX",
    # "Which keyword is used to create a new array by transforming each element?": "map",
    # "Which JavaScript array method filters elements based on a condition?": "filter",
    # "Which hook allows you to access DOM elements directly in React?": "useRef",
    # "Which method in Redux Toolkit configures the store?": "configureStore",
    # "Which hook is used to dispatch actions in Redux Toolkit?": "useDispatch",
    "What is the output of this code: console.log([1, 2, 3].map(x => x * 2));": "[2, 4, 6]",
    "What will be the output of: console.log([10, 20, 30].filter(x => x > 15));": "[20, 30]"
}

score = 0
total_questions = len(questions)
print("Welcom to the Quiz Game!")
print("Type 'quit' anytime to exit\n")

for question, correct_ans in questions.items():
    user_answer = input(question)
    if user_answer.lower() == 'quit':
        break
    elif user_answer.lower() == correct_ans.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {correct_ans}")
    print()
    
print(f"Quiz completed. Your score is {score}/{total_questions}")