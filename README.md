# AI-Assistant

## Project status

---

This is a team project for COMP602: Software Development Practices. Progress on this project has come to a halt as 
it has reached end of the semester. The project's continuation has yet to be discussed further.


## Features

---

AI-Assistant is an application designed to help students study course material. It provides assistance by utilising AI techniques to assess course material and offers features such as:
- Summarise Course Content: Get concise summaries of your course materials.
- Create Study Plans: Receive personalized study schedules tailored to your needs.
- Generate Mock Quizzes: Test your knowledge with AI-generated quizzes.
- Interactive Chat: Engage in a conversation with an AI that understands your course material.


## Built with

---

- [Python (3.12.x)](https://www.python.org/downloads/)
- UI Framework - [Streamlit](https://streamlit.io/)
- Database - [Firebase Realtime Storage](https://console.firebase.google.com/)
- LLM Host - [GroqCloud](https://console.groq.com/keys)

## Getting Started
1. Clone the repo
```commandline
git clone https://github.com/CarneAUT/2024_S2_-W202A-_AI-Assistant.git
```
3. Install dependencies
```commandline
pip install -r requirements.txt
```
2. Get Groq API Key at https://console.groq.com/keys. Place API key in a `.env` file.
```commandline
GROQ_API_KEY=<your_key>
```
3. Upload your `firebase-sdk.json` file to the root directory. 
You can generate your key from your Firebase project settings https://firebase.google.com/docs/admin/setup#python_1
<br></br>
4. Run the application
```commandline
streamlit run app.py
```

## Roadmap

---

- [ ] User Profile Customisation
- [ ] Chat & Groupchat
- [ ] Share Content

## Contributing

---

Feel free to contribute!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Authors and acknowledgment

---

Carne - https://github.com/Carne-Soper</br>
Philip - https://github.com/bdkhi1</br>
Tao - https://github.com/tao2122</br>


Project Link: https://github.com/CarneAUT/2024_S2_-W202A-_AI-Assistant

## License

---

Distributed under the MIT License. See `LICENSE.txt` for more information.

