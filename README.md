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

2. Update the database credentials in `settings.py` to connect Quizzx.ai to your custom database. Ensure that the credentials are accurate and reflect the configuration of your database.

3. Change the OpenAI key in `views.py` with your own OpenAI API key. This key is necessary to access the DaVinci model for generating MCQs.

4. Apply the database migrations by executing the following command:

   ```shell
   python manage.py migrate
   ```

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