# Usage Guide

This document provides instructions on how to use the AI Malaria Detection system.

## Prerequisites

Before using the system, ensure you have the following installed:
- Python 3.8 or higher
- Required Python packages (install using `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AI-Malaria-Detection-YOLOv8-SVM.git
    cd AI-Malaria-Detection-YOLOv8-SVM
    ```

2. Install the required packages:
    ```sh
    pip install -r app/requirements.txt
    ```

## Running the Application

To run the application, execute the following command:
```sh
python app/main.py
```

## Using the Detection System

1. **Upload Image**: Use the interface to upload a blood smear image.
2. **Run Detection**: Click the "Detect" button to run the malaria detection algorithm.
3. **View Results**: The results, including detected regions and classification, will be displayed on the screen.

## Evaluation

To evaluate the model's performance, use the provided test scripts:
```sh
pytest
```

## Additional Resources

- [Project Proposal](index.md)
- [Model Documentation](../models/README.md)

For further assistance, refer to the [README](../README.md) file.