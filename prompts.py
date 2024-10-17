mock_quiz = """
Create a Mock Quiz Based on Provided Course Content
As an experienced educator with a deep understanding of curriculum design and assessment strategies, develop a comprehensive mock quiz for a course that has been outlined here: {content}

The mock quiz should accurately reflect the key concepts, theories, and skills covered in the course. It must be challenging yet fair, allowing students to demonstrate their knowledge and understanding of the subject matter.

Quiz Format and Requirements
Design the mock quiz to comprise multiple-choice questions, short-answer questions, and possibly a few open-ended essay questions. Ensure that the questions are clear, concise, and relevant to the course content.

The quiz should include a mix of question types, such as:


Multiple-choice questions with 3-4 options (including at least one distractor)

Short-answer questions that require students to provide a brief response (around 50-100 words)

Open-ended essay questions that allow students to demonstrate their critical thinking and analytical skills

Question Distribution and Weightage
Distribute the questions to cover all the key topics and subtopics outlined in the course content. Allocate the weightage of each question type as follows:


Multiple-choice questions: 40-50% of the total marks

Short-answer questions: 30-40% of the total marks

Open-ended essay questions: 20-30% of the total marks

Question Difficulty and Validity
Ensure that the questions are of moderate to high difficulty level, challenging students to think critically and apply their knowledge. Validate the questions by referencing relevant academic sources and expert opinions.

Quiz Length and Format
Design the mock quiz to be around 30-40 minutes long, allowing students to complete it within a reasonable timeframe. Format the quiz to include:


A clear introduction and instructions

A scoring system that provides students with feedback on their performance

A section for students to provide their name and course code

Final Requirements
The final mock quiz should be:


Well-structured and easy to navigate

Free from grammatical errors and inconsistencies

Consistent in tone and language

Accessible to students with disabilities
"""

summarize_content = """
### Summarize Course Content as an Expert in Educational Pedagogy

Develop a concise and informative summary of a comprehensive online course on "Effective Learning Strategies for Academic Success."

### Task Details:

- The course should cover topics such as time management, note-taking techniques, active learning approaches, and exam preparation methods.
- The summary should highlight key takeaways, best practices, and real-world examples to illustrate the application of these strategies.
- The desired outcome is a clear, organized, and engaging summary that is easy to read and understand.
- Please focus on highlighting the most critical information, omitting unnecessary details, and maintaining a neutral tone.
- The summary should ideally be around 1-2 pages in length and written in a formal style.

### Additional Requirements:

- Use headings and subheadings to structure the content and improve readability.
- Include relevant examples or anecdotes to support key points and make the content more relatable.
- Avoid using technical jargon or complex terminology that may be unfamiliar to non-experts.
- Use a clear and concise writing style, with proper grammar, spelling, and punctuation.

### Reference Material:

You may draw upon existing course materials, including lectures, readings, and assignments, to create the summary.

### Output:

Please provide a well-structured summary that meets the above requirements, along with a brief justification for the approach taken to condense the course content.

Example:

"Effective Learning Strategies for Academic Success" is an online course that equips learners with the skills and knowledge necessary to excel in their academic pursuits. Key takeaways include...
"""

study_plan = """
### Create a Comprehensive Study Plan for a Student Preparing for the Upcoming Exams

As an expert academic counselor, develop a detailed study plan tailored to the individual academic needs of a student preparing for their upcoming exams.

The study plan should encompass a structured approach to mastering key concepts, practicing past exam questions, and managing time effectively.

Include a mix of study sessions, review materials, and practice assessments, ideally spanning over a period of 4-6 weeks.

The plan should be organized into daily, weekly, and monthly objectives, providing a clear roadmap for the student to stay on track.

The plan should also allow for flexibility to accommodate different learning styles, such as visual, auditory, or kinesthetic.

The final study plan should be concise, yet comprehensive, and include the following components:

- A detailed list of study materials and resources
- A schedule for regular review sessions and practice assessments
- Tips for effective time management and minimizing distractions
- Strategies for overcoming common obstacles and staying motivated
- A plan for seeking help and support when needed

Example:

"Welcome to your personalized study plan! To achieve academic success, let's break down our goals into manageable tasks and create a schedule that suits your learning style. Here's a suggested plan for the next 6 weeks..."
"""

chat_prompt = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question} 

Context: {context} 

Answer:
"""
