# Quizzx.ai

Quizzx.ai is a powerful question generation tool that leverages the capabilities of OpenAI's DaVinci model to generate multiple-choice questions (MCQs) from custom databases. Whether you have PDFs, Word documents, plain text files, or other formats, Quizzx.ai can extract relevant information and transform it into contextually appropriate MCQs.

## Features

- Generate MCQs from custom databases, including PDFs, Word documents, text files, and more.
- Utilizes OpenAI's DaVinci model for intelligent and contextually relevant question generation.
- Developed by students from the University at Buffalo.

## Getting Started

To start using Quizzx.ai, follow the steps below:

1. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

2. Create a file called 'secrets.env' and store the following API keys
   ```
   OPENAI_API_KEY=""
   SECRET_KEY=""
   EMAIL_PASS=""
   MODE = "DEV"
   ```

3. Run ```docker compose build``` or sometimes ```docker-compose build```, depending on your setup.

4. Then run ```docker compose -f ./docker-compose-dev up``` if you are in developing software.

5. Start the Quizzx.ai server by running the following command:

   ```shell
   python manage.py runserver
   ```

6. Access Quizzx.ai by visiting `http://localhost:8000` in your web browser.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions to Quizzx.ai are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repository).

## Support

If you need any assistance or have questions regarding Quizzx.ai, please contact the developers at [email@example.com](mailto:namannir@buffalo.edu) or (mailto@samar.singh.saini@buffalo.edu).

Happy quizzing with Quizzx.ai!