import streamlit as st

from pdf_reader import extract_text_from_pdf
from ppt_reader import extract_text_from_ppt
from docx_reader import extract_text_from_docx
from ocr import extract_text_from_image

from generator import (
    generate_summary,
    generate_quiz,
    generate_two_marks
)


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚"
)


st.title("📚 StudyMate AI")

st.write("Upload your study material")


file = st.file_uploader(
    "Choose a file",
    type=[
        "pdf",
        "pptx",
        "docx",
        "txt",
        "png",
        "jpg",
        "jpeg"
    ]
)


if file:

    text = ""

    st.success(f"Uploaded: {file.name}")


    # PDF
    if file.name.lower().endswith(".pdf"):

        text = extract_text_from_pdf(file)


    # PPT
    elif file.name.lower().endswith(".pptx"):

        text = extract_text_from_ppt(file)


    # Word
    elif file.name.lower().endswith(".docx"):

        text = extract_text_from_docx(file)


    # TXT
    elif file.name.lower().endswith(".txt"):

        text = file.read().decode("utf-8")


    # Image
    elif file.name.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):

        text = extract_text_from_image(file)


    # Extracted text
    if text.strip():

        st.success("Text extracted successfully!")


        with st.expander("📄 View Extracted Text"):

            st.text_area(
                "Study Material",
                text,
                height=300
            )


        # Generate button
        if st.button("✨ Generate Study Material"):

            with st.spinner("AI is preparing your study material..."):

                try:

                    summary = generate_summary(text)

                    quiz = generate_quiz(text)

                    two_marks = generate_two_marks(text)


                    st.subheader("🤖 AI Generated Content")


                    # Mini Tabs
                    tab1, tab2, tab3 = st.tabs(
                        [
                            "📚 Summary",
                            "📝 Quiz",
                            "✍️ 2 Marks"
                        ]
                    )


                    # Summary
                    with tab1:

                        st.markdown(summary)


                    # Quiz
                    with tab2:

                        st.markdown(quiz)


                    # 2 Marks
                    with tab3:

                        st.markdown(two_marks)


                except Exception as e:

                    st.error(
                        "Something went wrong while generating content."
                    )

                    st.write(e)


    else:

        st.warning(
            "No text found in this file."
        )