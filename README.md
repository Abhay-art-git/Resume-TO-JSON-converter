#  Resume Parser to JSON 📄➡️📦

<p align="center">
  <img src="https://img.shields.io/github/license/[your-username]/[repository-name]" alt="License">
  <img src="https://img.shields.io/github/stars/[your-username]/[repository-name]?style=social" alt="Stars">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Actively%20Developed-green" alt="Project Status">
</p>

An intelligent Python-based resume parser that extracts key information from resume files (`.pdf`, `.docx`) and converts it into a clean, structured JSON format, perfect for automating recruitment and data analysis workflows.

---

## ✨ How It Works: Before & After

This tool takes an unstructured resume file and turns it into valuable, machine-readable data.

<table>
  <tr>
    <td align="center"><strong>Input (Resume File)</strong></td>
    <td align="center"><strong>Output (Structured JSON)</strong></td>
  </tr>
  <tr>
    <td>
      <p align="center">
        📄<br>
        <code>my_resume.pdf</code><br>
        or<br>
        <code>candidate_cv.docx</code>
      </p>
    </td>
    <td>
<pre><code>{
  "personal_info": {
    "name": "Jane Doe",
    "email": "jane.doe@email.com",
    "phone": "123-456-7890",
    "location": "San Francisco, CA",
    "linkedin": "linkedin.com/in/janedoe"
  },
  "education": [
    {
      "degree": "Master of Science in Computer Science",
      "university": "Stanford University",
      "graduation_year": "2024"
    }
  ],
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Tech Solutions Inc.",
      "start_date": "June 2024",
      "end_date": "Present",
      "description": "Developed and maintained web applications using Python and Django."
    }
  ],
  "skills": [
    "Python",
    "JavaScript",
    "Django",
    "React",
    "SQL",
    "Docker",
    "AWS"
  ]
}
</code></pre>
    </td>
  </tr>
</table>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [JSON Output Structure](#json-output-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## About The Project

Manually sifting through hundreds of resumes is time-consuming and prone to error. **[Your Project Name]** was created to solve this problem. It leverages Natural Language Processing (NLP) to automatically identify and extract critical information from resumes, saving countless hours for recruiters and hiring managers.

This tool can serve as the backbone for:
* Applicant Tracking Systems (ATS)
* Candidate recommendation engines
* Automated talent pipeline management

---

## Key Features

-   **Multi-Format Support:** Parses both `.pdf` and `.docx` file formats.
-   **Comprehensive Data Extraction:** Extracts personal details, work experience, education, and skills.
-   **Structured Output:** Provides clean and consistent JSON output for easy integration with other systems.
-   **Extensible:** The parsing logic can be customized to extract additional or custom fields.
-   **Lightweight & Fast:** Built with efficient libraries for quick processing.

---

## JSON Output Structure

The parser returns a JSON object with the following primary keys:

| Key             | Type          | Description                                         |
| --------------- | ------------- | --------------------------------------------------- |
| `personal_info` | `Object`      | Candidate's contact and personal details.           |
| `education`     | `Array<Object>` | A list of educational qualifications.               |
| `experience`    | `Array<Object>` | A list of previous job experiences.                 |
| `skills`        | `Array<String>` | A list of skills identified in the resume.          |

---

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.9 or newer
-   `pip` package manager

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)[your-username]/[repository-name].git
    cd [repository-name]
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Download NLP Models (if using libraries like spaCy):**
    ```sh
    # This command downloads the English language model for spaCy
    python -m spacy download en_core_web_sm
    ```

---

## Usage

You can use the parser directly from the command line.

1.  Place the resume files you want to parse inside the `resumes/` directory (or any other directory).
2.  Run the main script with the path to the resume file as an argument.

**Example:**

```sh
python parse.py --file path/to/your/resume.pdf
