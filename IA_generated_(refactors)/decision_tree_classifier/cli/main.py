from core.decision_tree import DecisionNode, traverse, print_tree

def run_cli():
    dog = DecisionNode(label='Dog')
    cat = DecisionNode(label='Cat')
    bird = DecisionNode(label='Bird')
    fish = DecisionNode(label='Fish')

    mammal_node = DecisionNode(
        question='Does it bark?', left=dog, right=cat
    )
    fly_node = DecisionNode(
        question='Can it fly?', left=bird, right=fish
    )
    root = DecisionNode(
        question='Is it a mammal?',
        left=mammal_node,
        right=fly_node,
    )

    while True:
        print('\nDomestic Animal Classifier Decision Tree CLI')
        print('1. Visualize decision tree')
        print('2. Classify an animal (interactive)')
        print('3. Exit')
        choice = input('Choose an option (1/2/3): ').strip()
        if choice == '1':
            print('\nDecision Tree Structure:')
            print_tree(root)
        elif choice == '2':
            print('\nAnswer the questions to classify the animal:')
            traverse(root)
        elif choice == '3':
            print('Exiting.')
            break
        else:
            print('Invalid option. Please choose 1, 2, or 3.')
