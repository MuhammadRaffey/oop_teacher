# OOP Teacher

A CrewAI-powered educational tool designed to teach Object-Oriented Programming concepts in C++. This project uses AI agents to provide both theoretical explanations and practical code examples for various OOP concepts.

## Features

- Interactive learning experience with AI-powered explanations
- Detailed C++ code examples for each OOP concept
- Automatic generation of combined markdown files with explanations and code
- Training mode with result tracking
- Clean and well-structured output format

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/oop_teacher.git
cd oop_teacher
```

2. Set up a virtual environment (recommended):

```bash
uv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
uv sync
```

4. Set up environment variables:
   Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Run the OOP Teacher:

```bash
uv run kickoff
```

2. Enter an OOP topic when prompted (e.g., "inheritance", "polymorphism", "encapsulation")

3. The program will generate:
   - A theoretical explanation of the concept
   - Practical C++ code examples
   - A combined markdown file with both explanation and implementation

## Output Files

- `oop_combined_output.md`: Contains both the concept explanation and code implementation

## Project Structure

```
oop_teacher/
├── src/
│   └── oop_teacher/
│       ├── crews/
│       │   └── oop_crew/
│       │       ├── config/
│       │       │   ├── agents.yaml
│       │       │   └── tasks.yaml
│       │       └── oop_crew.py
│       └── main.py
├── .env
├── README.md
└── LICENSE
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [CrewAI](https://docs.crewai.com/)
- Powered by OpenAI's API
