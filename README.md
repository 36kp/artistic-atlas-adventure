# Artistic Atlas Adventure

Welcome to the Artistic Atlas Adventure project! This project aims to create an interactive and visually stunning atlas that showcases various artistic landmarks and cultural sites around the world.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [External Sources and Citations](#external-sources-and-citations)

## Introduction

The Artistic Atlas Adventure is an open-source project designed to provide users with an immersive experience exploring artistic and cultural landmarks. Whether you're an art enthusiast, a traveler, or just curious about the world's artistic heritage, this project is for you.

### Goal
- ✅ Perform EDA on publicly available image data
- ✅ Data clean-up and pickling
- ✅ Train a Convolutional Neural Network to classify images
- ✅ Use image class information to generate a prompt for GPT

#### Image Classification using CNN

1. Initial CNN Model

    ![Initial Model](docs/img/Initial%20Model.png)

2. Hyper-tuned Model using Random Search

    ![Tuned Model](docs/img/Trained%20Model.png)

## Project Structure

The project is organized into the following directories:

- `docs`: Contains documentation and images related to the project. See the [README.md](docs/README.md) in this directory for more details.
- `model`: Includes the trained models and related files. See the [README.md](model/README.md) in this directory for more details.
- `pickles`: Stores the pickled data files used in the project. See the [README.md](pickles/README.md) in this directory for more details.
- `src`: Contains the source code for the project. See the [README.md](src/README.md) in this directory for more details.

## Prerequisites

Before you begin, ensure you have met the following requirements:

This project uses OpenAI API to generate images, you need to set up your `OPENAI_API_KEY`. Follow these steps:

1. Register at [https://openai.com/api/](https://openai.com/api/) to get your API key.
2. Create a `.env` file in the root directory of the project.
3. Add your API key to the `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Installation

To get started with the Artistic Atlas Adventure, follow these steps:

0. Installing Dependencies
    ```bash
    pip install -r requirements.txt
    ```

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/artistic-atlas-adventure.git
    ```
2. Navigate to the project directory:
    ```bash
    cd artistic-atlas-adventure
    ```
3. Install the required dependencies:
    ```bash
    npm install
    ```

## Usage

To run the project locally, use the following command:
```bash
npm start
```
Open your web browser and go to `http://localhost:3000` to explore the Artistic Atlas Adventure.

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your commit message"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## External Sources and Citations

This project utilizes data and images from various external sources. Proper attribution is given to the original authors and creators. Below is a list of sources and citations:

- Training images data source: [Intel Image Classification](https://www.kaggle.com/datasets/puneet6060/intel-image-classification)

Enjoy your journey through the Artistic Atlas Adventure! Artistic Atlas Adventure!