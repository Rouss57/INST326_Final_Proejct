'''
Name: Nicolas Rousselot
Directory ID: nroussel
Assignment: Final Project
Date: 8/15/23

Below is a personality quiz to measure somebody’s agreeableness, which is one trait in the big five personality quiz (OCEAN). 
There are various questions with the options agree, neutral and disagree, which are then visual represented 
in graphs at the end of the quiz. I was able to incorporate information from 9 out of the 13 modules. 

I tried to implement content from each module:
1.	Python Fundamentals part 1 – Code uses variables
2.	Python Fundamentals part 2 – Code uses lists
3.	Testing – Includes a testing script to test for invalid input
4.	Basics of OOP – Code uses classes
5.	Container data types part 1 – Code uses dictionaries
6.	Container data types part 2 – Not Applicable
7.	Advanced OOP – code uses a class based structure which enables inheritance.
8.	Regular expressions – Not Applicable
9.	Collaborative Programming – Code is uploaded to GitHub
10.	Data Analysis – quiz answers are represented through various graphs at end of quiz
11.	Databases and SQL - The dataset, which is the answers to the quiz, is exported into the same directory as the python file 
at the end of the quiz as an .csv file to enable it to be imported to MySQL Workbench. 
12.	Data on the web – Not Applicable
13.	Web Scraping – Not Applicable

'''

import matplotlib.pyplot as plt
import csv


class Question:
    """
    A base class for representing a question.
    Attributes:
        text (str): The text of the question.
    Methods:
        display(): To be overridden by subclasses. Displays the question.
    """
    def __init__(self, text):
        """
        Initialize a Question instance.
        Args:
            text (str): The text of the question.
        """
        self.text = text
    def display(self):
        """
        Display the question.
        """
        pass  # This method is to be overridden by subclasses

class MultipleChoiceQuestion(Question):
    """
    A subclass of Question representing a multiple-choice question.
    Attributes:
        text (str): The text of the question.
        options (dict): A dictionary containing options for the question.
    Methods:
        display(): Displays the question and its options.
    """
    def __init__(self, text, options):
        """
        Initialize a MultipleChoiceQuestion instance.
        Args:
            text (str): The text of the question.
            options (dict): A dictionary containing options for the question.
        """
        super().__init__(text)
        self.options = options

    def display(self):
        """
        Display the question and its options
        """
        print(self.text)
        for option, text in self.options.items():
            print(f"{option}. {text}")

class Quiz:
    """
    Represents a quiz with questions and responses.
    Attributes:
        questions (list): A list of Question objects.
        responses (list): A list to store user responses.
    Methods:
        add_response(response): Add a user response to the responses list.
        take_quiz(): Take the quiz by displaying questions and collecting responses.
        calculate_scores(): Calculate scores based on user responses.
        visualize_bar_chart(scores): Visualize scores using a bar chart.
        visualize_pie_chart(scores): Visualize scores using a pie chart.
        visualize_line_plot(scores): Visualize scores using a line plot.
        visualize_horizontal_bar(scores): Visualize scores using a horizontal bar chart.
    """
    def __init__(self, questions):
        """
        Initialize a Quiz instance.
        Args:
            questions (list): A list of Question objects.
        """
        self.questions = questions
        self.responses = []

    def add_response(self, response):
        """
        Add a user response to the responses list.
        Args:
            response (str): The user's response to a question.
        """
        self.responses.append(response)

    def take_quiz(self):
        """
        Take the quiz by displaying questions and collecting responses.
        """
        for idx, question in enumerate(self.questions):
            question.display()
            response = input("Enter your choice: ").upper()
            while response not in question.options:
                print("Invalid response. Please choose a valid option.")
                response = input("Enter your choice: ").upper()
            self.add_response(response)

    def calculate_scores(self):
        """
        Calculate scores based on user responses.
        Returns:
            dict: A dictionary containing scores for different traits ('A', 'N', 'D').
        """
        scores = {'A': 0, 'N': 0, 'D': 0}
        for response in self.responses:
            scores[response] += 1
        return scores
    
    def export_to_csv(self, filename):
        """
        Export quiz responses to a CSV file.
        This method exports the questions along with their corresponding user responses to a CSV file.
        Args:
            filename (str): The name of the CSV file to be created or overwritten.
        Raises:
            IOError: If there is an issue with file I/O.
        Example:
            quiz.export_to_csv('quiz_responses.csv')
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Question', 'Response']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for question, response in zip(self.questions, self.responses):
                writer.writerow({'Question': question.text, 'Response': question.options[response]})

# Methods to visualiza data
        """
        Visualize scores using a bar chart.
        Args:
            scores (dict): A dictionary containing scores for different traits ('A', 'N', 'D').
        """
    def visualize_bar_chart(self, scores):
        traits = ["Agreeableness", "Neutral", "Disagreeableness"]
        counts = [scores['A'], scores['N'], scores['D']]
        plt.bar(traits, counts)
        plt.xlabel("Response")
        plt.ylabel("Frequency")
        plt.title("Agreeableness - Personality Trait")
        plt.show()

    def visualize_pie_chart(self, scores):
        """
        Visualize scores using a pie chart.
        Args:
            scores (dict): A dictionary containing scores for different traits ('A', 'N', 'D').
        """
        traits = ["Agreeableness", "Neutral", "Disagreeableness"]
        counts = [scores['A'], scores['N'], scores['D']]
        plt.pie(counts, labels=traits, autopct="%1.1f%%")
        plt.title("Agreeableness - Personality Trait")
        plt.show()

    def visualize_line_plot(self, scores):
        """
        Visualize scores using a line plot.
        Args:
            scores (dict): A dictionary containing scores for different traits ('A', 'N', 'D').
        """
        traits = ["Agreeableness", "Neutral", "Disagreeableness"]
        counts = [scores['A'], scores['N'], scores['D']]
        plt.plot(traits, counts, marker='o')
        plt.xlabel("Response")
        plt.ylabel("Frequency")
        plt.title("Agreeableness - Personality Trait")
        plt.show()

# Add questions using MultipleChoiceQuestion
questions = [
    MultipleChoiceQuestion("I value harmony in my relationships and interactions.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I tend to avoid arguments and disagreements whenever possible.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I believe that compromise is essential for maintaining healthy relationships.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("In general, I believe that people are inherently good.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I find it easy to get along with most people I meet.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I tend to put others' needs ahead of my own.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I'm patient and understanding with people, even when they make mistakes.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I enjoy collaborating with others on projects and tasks.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I find it challenging to say no when someone asks for a favor.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),
    MultipleChoiceQuestion("I feel upset when I perceive that I've hurt someone's feelings.", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"}),

    # Add more questions
]

quiz = Quiz(questions)
quiz.take_quiz()
scores = quiz.calculate_scores()
# Visuzalize data
quiz.visualize_bar_chart(scores)
quiz.visualize_pie_chart(scores)
quiz.visualize_line_plot(scores)
# Export to CSV file
quiz.export_to_csv('quiz_results.csv')
