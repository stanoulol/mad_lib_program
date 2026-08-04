# Mad Libs Generator

A Python program that generates a customized Mad Libs story by replacing placeholder words in a text file with user-provided input.

This project was built from scratch as a practice exercise in Python, focusing on file handling, string manipulation, and user interaction.

## About

This project is my implementation of the **Mad Libs** practice project from Chapter 10 of *Automate the Boring Stuff with Python*.

I completed the implementation independently without following the provided solution or hints, using it as an exercise to practice Python file handling and string manipulation.

## Features

* Reads a text file containing placeholder words
* Detects the following placeholders:

  * `ADJECTIVE`
  * `NOUN`
  * `VERB`
  * `ADVERB`
* Prompts the user to replace each placeholder with their own word
* Preserves punctuation and formatting in the original text
* Prints the completed story to the terminal
* Saves the completed story to a new text file

## Example

### Input file

```text
The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.
```

### User input

```text
Enter an adjective:
silly

Enter a noun:
chandelier

Enter a verb:
screamed

Enter a noun:
pickup truck
```

### Output

```text
The silly panda walked to the chandelier and then screamed.
A nearby pickup truck was unaffected by these events.
```

## Requirements

* Python 3.x

No external libraries are required.

## Usage

Run the program:

```bash
python mad_libs.py
```

Follow the prompts to enter replacement words. The completed story will be displayed in the terminal and saved as a new text file.

## Concepts Practiced

* File reading and writing
* String processing
* User input
* Loops
* Lists
* Conditional logic
* Working with text files
* Basic program design

## Future Improvements

* Allow custom placeholder types
* Support multiple input story templates
* Randomly choose from several templates
* Preserve capitalization automatically
* Add command-line arguments for input and output files

## Disclaimer

This project was created for learning and practice purposes.
