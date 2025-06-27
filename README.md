# ⚖️ Legal Clause Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

---

## ✨ Overview

The **Legal Clause Generator** is an intuitive web application designed to assist legal professionals, students, and anyone dealing with contracts in quickly drafting common legal clauses. Powered by a robust AI backend (using a large language model), it generates relevant and context-aware clauses based on user prompts and specified clause types. The user interface is crafted with a clean, modern aesthetic, inspired by Material UI's principles, ensuring a seamless and delightful user experience.

---

## 🤔 Why Use This Tool?

In the fast-paced world of legal drafting, efficiency and accuracy are paramount. This tool addresses common challenges by:

* **Saving Time & Effort:** Quickly generate complex legal language, reducing manual drafting time and allowing you to focus on strategic legal work.
* **Ensuring Consistency & Accuracy:** Leverage AI to produce clauses that adhere to common legal structures and best practices, minimizing errors.
* **Overcoming Writer's Block:** Get a strong starting point for your clauses, even when facing a blank page or unfamiliar phrasing.
* **Learning & Reference:** Ideal for legal students or new practitioners to understand the structure and content of various clause types.
* **Customization:** While AI-generated, the clauses provide a solid foundation that can be easily customized to fit specific contract needs.
* **Accessibility:** A simple, web-based interface makes it accessible from any device with a browser.

---

## 🚀 Features

* **AI-Powered Clause Generation:** Get instant, context-specific legal clauses for various needs.
* **Selectable Clause Types:** Choose from pre-defined categories like `Confidentiality`, `Indemnity`, and `Termination` to guide the AI.
* **Optional Context Field:** Provide additional details to refine the generated clause's relevance.
* **Responsive & Intuitive UI:** A user-friendly interface that adapts to different screen sizes, reminiscent of Material UI's design language.
* **Dynamic Theming:** Seamlessly switch between **Light ☀️** and **Dark 🌗** modes for optimal viewing comfort.
* **Read More/Less Functionality:** Generated clauses can be expanded or collapsed for better readability and focus.
* **Ripple Effect Buttons:** Interactive buttons with a subtle ripple animation for enhanced user feedback.

---

## 🛠️ Technologies Used

### Backend (FastAPI)
* **Python:** The core programming language.
* **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
* **`words_alpha.txt`**: A large dictionary used for internal processing (though autocomplete was removed, it might still be used for other internal language model preparations or validations if needed by the LLM logic).
* **Large Language Model (LLM):** (Implicit, as it's the core of the "AI") - This would be the external or local AI service you connect to for generating clauses.

### Frontend (HTML, CSS, JavaScript)
* **HTML5:** Structure of the web application.
* **Tailwind CSS:** A utility-first CSS framework for rapid and consistent styling, providing a clean, modern, and Material UI-inspired look and feel.
* **Vanilla JavaScript:** Handles all dynamic interactions, form submissions, and UI logic.

---

## ⚙️ Setup and Installation

Follow these steps to get your Legal Clause Generator up and running on your local machine.

### Prerequisites

* Python 3.9+ installed.
* `pip` (Python package installer).

### Backend Setup

1.  **Clone the repository (or extract your project files):**
    ```bash
    git clone (https://github.com/ayush6645/LegalClauseGenerator)
    cd LegalClauseGenerator
    ```
    (If you don't have a Git repo, just ensure your `backend` folder and `words_alpha.txt` are in the main project directory.)

2.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

4.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

5.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *If you don't have `requirements.txt`, create it first:*
    ```bash
    pip install fastapi uvicorn python-multipart # Add any other libraries your backend uses
    pip freeze > requirements.txt
    ```
    *(Note: The `fuzzywuzzy` and `python-Levenshtein` libraries mentioned in previous conversations for autocomplete are no longer needed if you removed autocomplete. Ensure your `requirements.txt` only has necessary packages for the clause generation and FastAPI.)*

6.  **Ensure `words_alpha.txt` is accessible:**
    Place your `words_alpha.txt` file at the path specified in `backend/routes/autocomplete.py` (or wherever your word loading logic is). Based on our previous discussion, it was:
    `D://Downloads//PROJECTS//LegalClauseGenerator//words_alpha.txt`
    **Important:** While the autocomplete feature has been removed from the frontend, the `autocomplete.py` file might still contain the logic to load this file for other purposes (e.g., if your LLM uses it, or if it was simply a leftover from a previous iteration). Double-check if `autocomplete.py` is still part of your `main.py` routing, or remove it entirely if it serves no purpose now. For this README, I'm assuming it's part of your project's data loading, even if the direct autocomplete UI is gone.

7.  **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The server will typically run on `http://127.0.0.1:8000`. You should see confirmation in your terminal that the server has started.

### Frontend Usage

1.  **Open `index.html`:**
    Simply open the `index.html` file in your preferred web browser. There's no separate server needed for the frontend, as it directly communicates with your running FastAPI backend.

---

## 📝 How To Use This Tool (Step-by-Step)

1.  **Launch the Application:** Ensure your backend server is running (`uvicorn main:app --reload`) and open `index.html` in your web browser.
2.  **Input Your Clause Prompt:** In the large text area labeled "Enter your clause prompt," describe the essence of the legal clause you need. Be concise but clear.
    * **Example:** "A clause for protecting confidential business information."
3.  **Select the Clause Type:** From the "Clause Type" dropdown menu, choose the category that best fits your desired clause. Options include `Confidentiality`, `Indemnity`, and `Termination`.
4.  **Add Optional Context:** If your clause requires specific details or background information for better accuracy, use the "Context (optional)" text area. This helps the AI understand the nuances.
    * **Example Context:** "This applies to all employee data and trade secrets shared during the project."
5.  **Generate the Clause:** Click the "🚀 Generate Clause" button. A loading indicator will appear briefly.
6.  **Review Results:** The AI-generated clauses will appear below the form. Each suggestion is presented clearly.
7.  **Expand/Collapse:** If a clause is lengthy, use the "Read More" button to view its full content and "Read Less" to collapse it.
8.  **Theme Toggle:** Switch between light and dark modes using the "☀️ / 🌗" button at the top right corner for a comfortable viewing experience at any time of day.

---

## ⏰ When To Use This Tool?

This Legal Clause Generator is particularly useful in scenarios where you need to:

* **Draft Contracts Quickly:** For lawyers or paralegals drafting new agreements and needing standard clause language.
* **Review Existing Documents:** To compare proposed clauses with common formulations.
* **Learn Legal Drafting:** For legal students or new professionals seeking to understand the structure and content of standard clauses.
* **Standardize Clause Language:** To maintain consistency across multiple documents.
* **Generate Initial Drafts:** When you need a starting point for negotiations or internal discussions, before full customization.
* **Explore Variations:** To see different ways a particular legal concept can be articulated.

**Important Note:** This tool is designed to assist in drafting and provides AI-generated suggestions. It is **not a substitute for legal advice** from a qualified professional. Always review and adapt the generated clauses to fit your specific legal context and jurisdiction.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
(You should create a `LICENSE` file in your root directory if you haven't already, containing the MIT license text.)

---

## 🙌 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.

---
