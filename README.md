# Skin Diagnosis Interface

Skin Diagnosis Interface is a web application designed to assist in the identification and diagnosis of various skin conditions using machine learning techniques. The application leverages a trained model to analyze skin images and provide diagnostic suggestions.

## Features

- **User-Friendly Interface**: Utilizes Streamlit to offer an intuitive and interactive user experience.
- **Image Analysis**: Allows users to upload skin images for analysis.
- **Diagnostic Feedback**: Provides diagnostic suggestions based on the uploaded images.

## Installation

To set up the Skin Diagnosis Interface locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/mthd98/Skin-Diagnosis-Interface.git
   ```


2. **Navigate to the Project Directory**:

   ```bash
   cd Skin-Diagnosis-Interface
   ```


3. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```


4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

To run the application:


```bash
streamlit run StreamlitApp.py
```


This command will launch the web application, accessible at `http://localhost:8501/`.

## Project Structure

- **StreamlitApp.py**: Main script to run the Streamlit application.
- **Utilities/**: Contains utility functions and modules supporting the main application.
- **test.ipynb**: Jupyter Notebook for testing and experimentation.
- **requirements.txt**: Lists all Python dependencies required to run the application.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](https://github.com/mthd98/Skin-Diagnosis-Interface/blob/main/LICENSE) file.
