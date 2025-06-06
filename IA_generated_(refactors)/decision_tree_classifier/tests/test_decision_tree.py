import unittest
from core.decision_tree import DecisionNode

class TestDecisionTree(unittest.TestCase):
    def setUp(self):
        self.dog = DecisionNode(label='Dog')
        self.cat = DecisionNode(label='Cat')
        self.bird = DecisionNode(label='Bird')
        self.fish = DecisionNode(label='Fish')

        self.mammal_node = DecisionNode(
            question='Does it bark?', left=self.dog, right=self.cat
        )
        self.fly_node = DecisionNode(
            question='Can it fly?', left=self.bird, right=self.fish
        )
        self.root = DecisionNode(
            question='Is it a mammal?',
            left=self.mammal_node,
            right=self.fly_node,
        )

    def test_leaf_labels(self):
        self.assertEqual(self.dog.label, 'Dog')
        self.assertEqual(self.cat.label, 'Cat')
        self.assertEqual(self.bird.label, 'Bird')
        self.assertEqual(self.fish.label, 'Fish')

if __name__ == '__main__':
    unittest.main()
